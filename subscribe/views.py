from django.shortcuts import (
    render, redirect, reverse,
)
from django.http import (
    HttpResponse, JsonResponse,
)
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from django.views.decorators.http import (
    require_POST, require_GET
)

from .forms import SubscriptionForm, UserRegisterForm
from .models import Subscription

import stripe


@require_GET
def subscribe(request):
    """ 
    GET: Display User and Subscribe forms and
    create Stripe paymentIntent.
    """
    if request.user.is_authenticated:
        messages.info(
            request, 
            "Sorry, can't do that! \
            Logout first to create a new subscription."
        )
        return redirect(reverse('stories'))

    # get Stripe credentials from environment
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.')

    if request.method == "GET":
        # create payment intent object
        stripe_total = round(settings.SUBSCRIPTION_COST * 100)  # fixed payment amount defined on server
        stripe.api_key = stripe_secret_key
        payment_intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # create blank forms for User and Subscription models
        user_form = UserRegisterForm()
        subscribe_form = SubscriptionForm()

        # return client secret and public_key to template
        context = {
            'user_form': user_form,
            'subscribe_form': subscribe_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': payment_intent.client_secret,
        }
        template = "subscribe/subscribe.html"
        return render(request, template, context)


@require_POST
def create_inactive_user(request):
    """
    Create user and linked subscription records in
    database before attempting payment on client. 
    Set user.is_active field is set to False.
    """
    try:
        # parse POST data to create models
        user_data = {
            'username': request.POST.get('username'),
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
            'password1': request.POST.get('password1'),
            'password2': request.POST.get('password2'),
        }
        subscription_data = {
            'country': request.POST.get('country'),
            'city': request.POST.get('city'),
        }
        user_form = UserRegisterForm(user_data)
        subscription_form = SubscriptionForm(subscription_data)
        if user_form.is_valid() and subscription_form.is_valid():
            user = user_form.save(commit=False)
            subscription = subscription_form.save(commit=False)
        else:
            messages.error(
                request,
                "Please check your form for errors and try again."
            )
            return JsonResponse(
                data={"error": "Form was invalid"},
                status=400,
            )
        stripe_pid = request.POST.get('client_secret').split('_secret')[0]
        # add fields to subscription instance
        subscription.user = user
        subscription.stripe_pid = stripe_pid
        # deactivate user
        user.is_active = False
        # save inactive user and linked subscription to database
        user.save() # user must be saved before subscription to avoid ValueError
        subscription.save()
        user_id = user.id  # default pk for user is added AFTER save
        # add user_id as metadata to paymentIntent to 
        # facilitate webhook handler functionality
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(stripe_pid, metadata={
            'user_id': user_id,
        })
        # user record and linked subscription record created
        # and metadata added to paymentIntent
        return JsonResponse(
            data={"userId": user_id},
            status=200,
        )

    except Exception as error:
        messages.error(
            request,
            "Your account could not be created. \
            Please try again or contact me for help!"
        )
        return JsonResponse(
            data={"error": error},
            status=500,
        )


@require_POST
def delete_inactive_user(request):
    """
    Delete inactive User record (and associated
    Subscription record by cascade) after payment 
    attempt was unsuccessful on client
    """
    user_id = int(request.POST.get('user_id'))  # id for previously cached user
    try:
        user = User.objects.get(id=user_id)  # get inactive user instance
        user.delete()  # subscription also deleted
    except Exception:




            # create Subscription instance from POST data
            subscription_data = {
                'country': request.POST.get('country'),
                'city': request.POST.get('city'),
                'stripe_pid': request.POST.get('client_secret').split('_secret')[0],
            }
            
            # instantiate Subscription model directly 
            # and point to User instance created above
            subscription = Subscription(
                **subscription_data,
                user=user,
            )

            # finally, commit user and subscription records to database
            user.save()
            subscription.save()

            








@require_POST
def activate_cached_user(request):
    """
    Set User.is_active field to True after payment
    completes successfully on client
    """
    user_id = int(request.POST.get('user_id'))  # id for previously cached user
    activate_success_redirect_url = '/login/'
    try:
        user = User.objects.get(id=user_id)  # get inactive user instance
        user.is_active = True
        user.save()
        messages.success(
            request,
            "Your account was created successfully. \
            Login now to download stories!"
        )

        return JsonResponse(
            {
                'redirectUrl': activate_success_redirect_url,
            },
            status=200,
        )

    except Exception:
        messages.error(
            request,
            "There was an error when creating your account! \
            Please try again or contact me for assistance."
        )
    
    return JsonResponse(
        {},
        status=500,
    )


