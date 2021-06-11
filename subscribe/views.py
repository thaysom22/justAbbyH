from django.shortcuts import render, redirect, reverse

from .forms import SubscriptionForm, UserRegisterForm


def subscribe(request):
    """ 
    GET: Display user and subscribe forms
    POST: Process payment with Stripe
    and create User and Subscription
    instances in respective database tables
    """
    if request.user.is_authenticated():
        # ADD MESSAGE: USER ALREADY SUBSCRIBED
        return redirect(reverse('stories'))

    if request.method == "GET":
        user_form = UserRegisterForm()
        subscription_form = SubscriptionForm()
        context = {
            'user_form': user_form,
            'subscribe_form': subscription_form
        }
        template = "subscribe/subscribe.html"
        return render(request, template, context)

    # POST
    subscription_form_data = {
        'first_name': request.POST.get('first_name'),
        'last_name': request.POST.get('last_name'),
        'email': request.POST.get('email'),
        'country': request.POST.get('country'),
        'city': request.POST.get('city'),
    }
    subscription_form = SubscriptionForm(subscription_form_data)
    if subscription_form.is_valid():
            subscription = subscription_form.save(commit=False)  # instance of model in memory only

    # PROCESS STRIPE PAYMENT
    # CREATE NEW INSTANCE OF USER MODEL FROM USERCREATIONFORM MODELFORM
    # CREATE NEW INSTANCE OF SUBSCRIPTION MODEL FROM SUBSCRIPTIONFORM MODELFORM
    
    # SAVE NEW MODEL INSTANCE TO DATABASE

    return redirect(reverse('stories'))
        

