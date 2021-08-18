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
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token_generator

from .forms import SubscriptionForm, UserRegisterForm

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
                'subscription_cost': round(settings.SUBSCRIPTION_COST),
                'stripe_public_key': stripe_public_key,
                'client_secret': payment_intent.client_secret,
                'page_title': 'Subscribe',
            }
            template = "subscribe/subscribe.html"
            return render(request, template, context)
        
    except Exception as e:
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
    user = None  # avoid later error when checking if user is in db
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

        # validates city and country fields only for subscription_form
        if user_form.is_valid() and subscription_form.is_valid():      
            user = user_form.save(commit=False)
            user.is_active = False  # deactivate user to prevent login
            user.save()  # user must be saved in db before it is used as subscription's foreign key
            inactive_user_id = user.id  # default pk for user is added AFTER save
            # create instance of subscription model w/o user
            subscription = subscription_form.save(commit=False)
            # add non-form subscription fields pre-save
            subscription.user = user
            stripe_pid = request.POST.get('client_secret').split('_secret')[0]
            subscription.stripe_pid = stripe_pid
            subscription.save()  # start_date field is set when saved to DB

        else:

            return JsonResponse(
                data={
                    "errors": {
                        **user_form.errors,
                        **subscription_form.errors,
                    }
                },
                status=400,
            )

        # add inactive_user_id as metadata to paymentIntent to 
        # facilitate webhook handler functionality
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            stripe_pid,
            metadata={
                'inactive_user_id': inactive_user_id,
            },
        )
        # user record and linked subscription record created
        # and metadata added to paymentIntent
        # include inactive_user_id and redirect_url in response
        return JsonResponse(
            data={
                "inactiveUserId": inactive_user_id,
                "redirectUrlPath": "/subscribe/subscription-created",
                },
            status=200,
        )

    except Exception as error:
        # delete user if try block created it in database
        if hasattr(user, 'id'):
            try:
                user.delete()
            except Exception:
                pass

        messages.error(
            request,
            "Sorry, your account could not be created right now. \
            Your card has not been charged. \
            Please try again or contact for help."
        )

        return JsonResponse(
            data={"error": str(error)},
            status=500,
        )


@require_POST
def confirm_deletion_of_inactive_user(request):
    """
    Delete or confirm non-existance of inactive User record 
    (and associated Subscription record by cascade) after payment
    attempt was unsuccessful on client
    """
    try:
        inactive_user_id = int(request.POST.get('inactive_user_id'))  # id for inactive user
        try:
            user = User.objects.get(id=inactive_user_id)  # get inactive user instance
        except User.DoesNotExist:
            return HttpResponse(
                content=f"Confirmed that no user with id:{inactive_user_id} exists in database",
                status=200,
            )
        # confirm that existing user instance to be deleted is inactive
        # this negates malicious POST requests to delete active users
        if not user.is_active:
            user.delete()  # linked subscription also deleted by CASCADE
            return HttpResponse(
                content=f"User with id:{inactive_user_id} was successfully deleted from database",
                status=200,
            )
        else:
            # page is reloaded by js, so inform user about failed payment
            messages.error(
                request,
                "I'm sorry your payment was not successful. \
                Your card has not been charged. \
                Please try again or contact for help."
            )
            return HttpResponse(
                content="Request denied: User instance is active and \
                    therefore cannot be deleted from the database.",
                status=400,
            )
    except Exception as error:
        # page is reloaded by js, so inform user about failed payment
        messages.error(
            request,
            "I'm sorry your payment failed. \
            Please try again or contact me for help!"
        )
        return HttpResponse(
            content=f"{str(error)}",
            status=500,
        )


@require_GET
def subscription_created(request):
    """ 
    Render user and subscription details in template
    """
    # parse raw url query parameters
    context = {
        'first_name': request.GET.get('first_name', ''),
        'last_name': request.GET.get('last_name', ''),
        'email': request.GET.get('email', ''),
        'username': request.GET.get('username', ''),
        'page_title': 'Subscription Created',
    }
    # decode query string values and pass to template context
    # CREDIT[8]
    for k, v in context.items():
        context[k] = urllib.parse.unquote(v)

    # add other data to context after decoding url params
    context['subscription_cost'] = round(settings.SUBSCRIPTION_COST)
    context['default_from_email'] = settings.DEFAULT_FROM_EMAIL

    template = "subscribe/subscription_created.html"
    return render(request, template, context)


@require_GET
def activate_user(request, uidb64, token):
    """
    If onetime token encoded as url parameter verifies:
    activate user account and render login template
    """
    # CREDIT[9]
    try:
        # get uid from url and use to query db
        inactive_user_id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=inactive_user_id)
    except (TypeError, ValueError,
            OverflowError, User.DoesNotExist):
        user = None

    if (user and
            account_activation_token_generator.check_token(user, token) and not
            user.is_active):
        # ACTIVATE USER
        user.is_active = True
        user.save()
        messages.success(request,
            "Your account has been activated. Please login to start reading!")
        return redirect(reverse('login'))
    else:
        messages.warning(request,
            "This activation link was already used, or is expired/invalid. Please contact me for assistance.")
        return redirect(reverse('index'))