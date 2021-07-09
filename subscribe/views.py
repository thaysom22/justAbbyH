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

import urllib
import stripe


@require_GET
def subscribe(request):
    """ 
    GET: Display User and Subscribe forms and
    create Stripe paymentIntent.
    """
    try:
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
            # fixed payment amount defined on server
            stripe_total = round(settings.SUBSCRIPTION_COST * 100)
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
        
    except Exception:
        messages.error(
            request,
            "There was a server error. \
            Please try again or contact me for help!"
        )
        return redirect(reverse('index'))



@require_POST
def create_inactive_user(request):
    """
    Create user and linked subscription records in
    database before attempting payment on client. 
    Set user.is_active field is set to False.
    """

    print("request made to create_inactive_user")  # TEST

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

        print("user form data", user_form.data)  # TEST
        print("user form isvalid", user_form.is_valid())  # TEST
        print("user form errors", user_form.errors)  # TEST

        print("subscription form data", subscription_form.data)  # TEST
        print("subscription form isvalid", subscription_form.is_valid())  # TEST
        print("subscription form errors", subscription_form.errors)  # TEST

        # validates city and country fields only for subscription_form
        if user_form.is_valid() and subscription_form.is_valid():

            print("user_form and subscription_form both validate")
            
            user = user_form.save(commit=False)
            user.is_active = False  # deactivate user to prevent login
            user.save()  # user must be saved in database before it is used as subscription's foreign key
            user_id = user.id  # default pk for user is added AFTER save

            # create instance of subscription model w/o user
            subscription = subscription_form.save(commit=False)
            # add non-form subscription fields pre-save
            subscription.user = user
            stripe_pid = request.POST.get('client_secret').split('_secret')[0]
            subscription.stripe_pid = stripe_pid

            print("subscription with user and stripe_pid", subscription)  # TEST

            subscription.save()  # start_date field is set when saved to DB

        else:
            messages.error(
                request,
                "Please check your form for errors and try again."
            )
            return JsonResponse(
                data={
                    "errors": {
                        **user_form.errors,
                        **subscription_form.errors,
                    }
                },
                status=400,
            )

        
        # add user_id as metadata to paymentIntent to 
        # facilitate webhook handler functionality
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(stripe_pid, metadata={
            'user_id': user_id,
        })
        # user record and linked subscription record created
        # and metadata added to paymentIntent
        # return user_id and redirect_url for 
        # if payment is successful in response
        return JsonResponse(
            data={
                "userId": user_id,
                "redirectUrlPath": "/subscribe/subscription-created",
                },
            status=200,
        )

    except Exception as error:
        messages.error(
            request,
            "Your account could not be created. \
            Please try again or contact me for help!"
        )
        
        print(error)  # TEST

        return JsonResponse(
            data={"error": str(error)},
            status=500,
        )


@require_POST
def delete_inactive_user(request):
    """
    Delete inactive User record (and associated
    Subscription record by cascade) after payment 
    attempt was unsuccessful on client
    """

    print("request made to delete_inactive_user")  # TEST

    try:
        user_id = int(request.POST.get('user_id'))  # id for inactive user
        try:
            user = User.objects.get(id=user_id)  # get inactive user instance
        except User.DoesNotExist:
            messages.error(
                request,
                "There was an error creating your account. \
                Please try again or contact me for help!"
            )
            return HttpResponse(
                content="Error: User record was not \
                    found and therefore could not be \
                    deleted from database.",
                status=400,
            )
        # confirm that user instance to be deleted is inactive
        # this prevents malicious POST requests to delete active
        # user accounts
        if not user.is_active:
            user.delete()  # linked subscription also deleted by CASCADE
            return HttpResponse(
                content=f"user with id:{user_id} was deleted from database",
                status=200,
            )
        else:
            messages.error(
                request,
                "There was an error creating your account. \
                Please try again or contact me for help!"
            )
            return HttpResponse(
                content="Error: User record is active and \
                    therefore cannot be deleted from the database.",
                status=400,
            )
    except Exception as error:
        messages.error(
            request,
            "Your account could not be created. \
            Please try again or contact me for help!"
        )
        return HttpResponse(
            content=f"Error: {str(error)}",
            status=500,
        )


@require_GET
def subscription_created(request):
    """ 
    Render user and subscription details in template
    """

    print("request made to subscription_created")  # TEST

    # parse raw url query parameters and pass to template context
    context = {
        'first_name': request.GET.get('first_name', ''),
        'last_name': request.GET.get('last_name', ''),
        'email': request.GET.get('email', ''),
        'city': request.GET.get('city', ''),
        'country_verbose': request.GET.get('country_verbose', ''),
    }
    # decode values
    # CREDIT[8]
    for k, v in context.items():
        context[k] = urllib.parse.unquote(v)

    template = "subscribe/subscription_created.html"
    return render(request, template, context)


