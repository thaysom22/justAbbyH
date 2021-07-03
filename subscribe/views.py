from django.shortcuts import (
    render, redirect, reverse, HttpResponse
)
from django.http.response import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from django.views.decorators.http import require_POST

from .forms import SubscriptionForm, UserRegisterForm
from .models import Subscription

import stripe


@require_POST
def cache_inactive_user(request):
    """
    Create User and Subscription records from POST data
    with User.is_active field set to False
    """
    user_data = {
        'username': request.POST.get('username'),
        'first_name': request.POST.get('first_name'),
        'last_name': request.POST.get('last_name'),
        'email': request.POST.get('email'),
        'password1': request.POST.get('password1'),
        'password2': request.POST.get('password2'),
    }
    try:
        # create User instance from POST data
        user_form = UserRegisterForm(user_data)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_active = False
            user_id = user.id
    
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

            # user and subscription records created successfully
            # trigger ajax success on client return id of user parsed as json 
            # to activate user after payment
            return JsonResponse(
                {'userId': user_id},
                status=200
            )  
        else:
            # user form not valid
            messages.error(request, "Please check your form for errors and try again.")
        
    except Exception:
        messages.error(
            request,
            "There was an error when creating your account! \
            Please try again or contact me for assistance."
        )

    # trigger ajax failure on client
    return JsonResponse(
        {},  # ajax parser expects non-empty first parameter
        status=400,
    )


@require_POST
def activate_cached_user(request):
    """
    Set User.is_active field to True when payment
    completes successfully on client
    """
    # when this code runs payment has already completed on client
    user_id = request.POST.get('user_id')  # id for previously cached user
    # try:
    inactive_user = User.objects.get(id=user_id)

@require_POST
def delete_cached_user(request):
    """
    Delete User record (and associated 
    Subscription record by cascade) from database 
    when payment is unsuccessful on client
    """


def subscribe(request):
    """ 
    Display user and subscribe forms and
    create Stripe PaymentIntent
    """
    if request.user.is_authenticated:
        messages.info(request, "Sorry, can't do that! \
            Logout first to create a new subscription.")
        return redirect(reverse('stories'))

    # get Stripe credentials from environment
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.')

    if request.method == "GET":
        # create payment intent object
        stripe_total = round(settings.SUBSCRIPTION_COST * 100)  # fixed payment amount
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
