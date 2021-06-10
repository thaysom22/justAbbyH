from django.shortcuts import render, redirect, reverse


def subscribe(request):
    """ 
    GET: Display subscribe form 
    POST: Process payment with Stripe
    and create subscription in database
    """
    if request.method == "GET":
        context = {
            # CREATE NEW INSTANCE OF MODELFORM
        }
        template = "subscribe/subscribe.html"
        return render(request, template, context)

    # POST

    # PROCESS STRIPE PAYMENT
    # CREATE NEW INSTANCE OF SUBSCRIPTION MODEL FROM MODELFORM
    # SAVE NEW MODEL INSTANCE TO DATABASE

    return redirect(reverse('stories'))
        

