from django.http import HttpResponse


class Stripe_WH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_other_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded_event(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """

    def handle_payment_intent_payment_failed_event(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        # get id of inactive user in db from payment intent metadata
        intent = event.data.object
        inactive_user_id = intent.metadata.get('inactive_user_id')

        

