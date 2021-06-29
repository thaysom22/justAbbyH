from django.shortcuts import (
    render, redirect, reverse, HttpResponse
)
from django.http.response import JsonResponse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

from .forms import SubscriptionForm, UserRegisterForm
from .models import Subscription

import stripe


@require_POST
def cache_inactive_user(request):
    """
    Create User record in database from POST data and 
    set User.is_active field to False 
    """
    try:
        # collect required POST data for User model
        user_form_data = {
            'username': request.POST.get('username'),
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
            'password1': request.POST.get('password1'),
            'password2': request.POST.get('password2'),
        }
        # create ModelForm instance from POST data and check validity
        user_form = UserRegisterForm(user_form_data)
        if user_form.is_valid():
            # create model instance from ModelForm and deactivate 
            user = user_form.save(commit=False)
            user.is_active = False
            user.save()  # create database record
            return JsonResponse(content=user.id, status=200)  # return id of inactive user as json
        else:
            messages.error(request, "Please check your form for errors!")
            return HttpResponse(status=400)
        
    except Exception as e:
        messages.error(request, "There was an error when creating your account! \
                                 Please try again or contact me for assistance.")
        return HttpResponse(content=e, status=400)


def subscribe(request):
    """ 
    GET: Display user and subscribe forms,
    create Stripe PaymentIntent
    POST: Create User and Subscription
    instances in respective database tables
    """
    if request.user.is_authenticated:
        messages.info(request, "Can't do that! \
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

    # POST
    

    subscription_form_data = {
        'country': request.POST.get('country'),
        'city': request.POST.get('city'),
    }
    try:
         # construct instance of Subscription model directly
        subscription = Subscription(
            **subscription_form_data,
            user=user,  # refers to User instance created above
            stripe_pid=request.POST.get('client_secret').split('_secret')[0],
        )
    except Exception as e:
        messages.error(
            request, 
            "There was an error creating your subscription. \
             Please contact us to rectify."
        )
        return redirect(reverse('subscribe'))

    # finally, add user and subscription records to database
    user.save()
    subscription.save()

    # user and subscription records created successfully
    messages.success(request, "Your payment was successful and you are now subscribed. \
                               Login now to download stories!")
    return redirect(reverse('login'))
        

