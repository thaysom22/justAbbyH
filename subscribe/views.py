from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import SubscriptionForm, UserRegisterForm
from .models import Subscription

import stripe


def subscribe(request):
    """ 
    GET: Display user and subscribe forms,
    create Stripe PaymentIntent
    POST: Create User and Subscription
    instances in respective database tables
    """
    if request.user.is_authenticated:
        messages.info(request, "Can't do that! Logout first to create a new subscription.")
        return redirect(reverse('stories'))

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "GET":
        # create payment intent object
        stripe_total = round(settings.SUBSCRIPTION_COST * 100)  # fixed payment amount
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # create blank forms for User and Subscription models
        user_form = UserRegisterForm()
        subscribe_form = SubscriptionForm()
        
        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing.')

        # return client secret to template
        context = {
            'user_form': user_form,
            'subscribe_form': subscribe_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }
        template = "subscribe/subscribe.html"
        return render(request, template, context)

    # POST
    
    # Construct instance of User model from related form fields
    user_form_data = {
        'username': request.POST.get('username'),
        'password1': request.POST.get('password1'),
        'password2': request.POST.get('password2'),
    }
    user_form = UserRegisterForm(user_form_data)
    if user_form.is_valid():
        user = user_form.save(commit=False)
    else:
        messages.error(
            request, 
            f"There was an error creating your account. \
             Please contact us to rectify."
        )
        return redirect(reverse('subscribe'))

    # Construct instance of Subscription model from related form fields 
    subscription_form_data = {
        'first_name': request.POST.get('first_name'),
        'last_name': request.POST.get('last_name'),
        'email': request.POST.get('email'),
        'country': request.POST.get('country'),
        'city': request.POST.get('city'),
    }
    try:
        subscription = Subscription(
            **subscription_form_data,
            user=user,  # refers to User instance created above
            stripe_pid=request.POST.get('client_secret').split('_secret')[0],
        )
    except Exception as e:
        messages.error(
            request, 
            f"There was an error creating your subscription. \
             Please contact us to rectify."
        )
        return redirect(reverse('subscribe'))

    # add user and subscription records to database
    user.save()
    subscription.save()

    # user and subscription records created successfully
    messages.success(request, "Your payment was successful and you are now subscribed. \
                               Login now to download stories!")
    return redirect(reverse('login'))
        

