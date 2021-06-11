from django.shortcuts import render, redirect, reverse

from .forms import SubscriptionForm, UserRegisterForm


def subscribe(request):
    """ 
    GET: Display user and subscribe forms
    POST: Process payment with Stripe
    and create User and Subscription 
    instances in respective database tables
    """
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

    # PROCESS STRIPE PAYMENT
    # CREATE NEW INSTANCE OF USER MODEL FROM USERCREATIONFORM MODELFORM
    # CREATE NEW INSTANCE OF SUBSCRIPTION MODEL FROM SUBSCRIPTIONFORM MODELFORM
    # SAVE NEW MODEL INSTANCE TO DATABASE

    return redirect(reverse('stories'))
        

