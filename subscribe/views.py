from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import SubscriptionForm, UserRegisterForm
from .models import Subscription


def subscribe(request):
    """ 
    GET: Display user and subscribe forms
    POST: Process payment with Stripe
    and create User and Subscription
    instances in respective database tables
    """
    if request.user.is_authenticated:
        messages.info(request, "You are already subscribed!")
        return redirect(reverse('stories'))

    if request.method == "GET":
        user_form = UserRegisterForm()
        subscribe_form = SubscriptionForm()
        context = {
            'user_form': user_form,
            'subscribe_form': subscribe_form
        }
        template = "subscribe/subscribe.html"
        return render(request, template, context)

    # POST

    # CREATE NEW INSTANCE OF USER MODEL FROM MODELFORM
    user_form_data = {
        'username': request.POST.get('username'),
        'password1': request.POST.get('password1'),
        'password2': request.POST.get('password2'),
    }
    user_form = UserRegisterForm(user_form_data)
    if user_form.is_valid():
        user = user_form.save() 
    else:
        messages.error(request, user_form.errors)
        return redirect(reverse('subscribe'))

    # CREATE NEW INSTANCE OF SUBSCRIPTION MODEL 
    subscribe_form_data = {
        'first_name': request.POST.get('first_name'),
        'last_name': request.POST.get('last_name'),
        'email': request.POST.get('email'),
        'country': request.POST.get('country'),
        'city': request.POST.get('city'),
    }
    subscription_form = SubscriptionForm(subscribe_form_data)
    if subscription_form.is_valid():
        subscription = Subscription(
            user=user,  # refers to User instance created above
            first_name=subscribe_form_data.cleaned_data['first_name'],
            last_name=subscribe_form_data.cleaned_data['last_name'],
            email=subscribe_form_data.cleaned_data['email'],
            country=subscribe_form_data.cleaned_data['country'],
            city=subscribe_form_data.cleaned_data['city'],
        )
        subscription.save()
    else:
        messages.error(request, subscribe_form.errors)
        return redirect(reverse('subscribe'))

    # PROCESS STRIPE PAYMENT
    
    # SAVE NEW MODEL INSTANCES TO DATABASE

    # TESTS

    print(user)
    print(subscription)

    return redirect(reverse('login'))
        

