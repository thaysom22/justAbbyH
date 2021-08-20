from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .webhook_handler import Stripe_WH_Handler

import stripe


@require_POST
@csrf_exempt  # requests originate from Stripe
def webhook_listener(request):
    """
    Listen for webhooks from Stripe and assign
    handler methods from Stripe_WH_Handler by
    event type
    """
    # setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY
    # get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # invalid payload
        return HttpResponse(content=e, status=400)
    except stripe.error.SignatureVerificationError as e:
        # invalid signature
        return HttpResponse(content=e, status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # construct instance of webhook handler with request object
    wh_handler = Stripe_WH_Handler(request)

    # map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': wh_handler.handle_payment_intent_succeeded_event,
        'payment_intent.payment_failed': wh_handler.handle_payment_intent_payment_failed_event,
    }

    # get the webhook type
    event_type = event['type']
    # get appropriate event handler function using event map
    # use generic handler by default
    event_handler = event_map.get(event_type, wh_handler.handle_other_event)

    # call event handler with the event
    response = event_handler(event)
    return response
