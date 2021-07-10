from django.http import HttpResponse
from django.contrib.auth.models import User

import time


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
        try:
            # get id of inactive user in db from payment intent metadata
            intent = event.data.object
            inactive_user_id = int(intent.metadata.get('inactive_user_id'))
            inactive_user_found = False
            activation_email_sent = False
            attempt = 1
            while attempt <= 10:
                try:
                    user = User.objects.get(id=inactive_user_id)  # get inactive user instance
                    inactive_user_found = True
                except User.DoesNotExist:
                    attempt += 1
                    time.sleep(.5)
                    continue

                if not user.is_active:
                    try:
                        # send email to activate user instance (or just set user.is_active = True)
                        activation_email_sent = True
                        break
                    except Exception as e:
                        email_error = e  # capture Exception info
                        attempt += 1
                        time.sleep(.5)  # wait 500 ms before reattempt to send email
                        continue
                else:
                    return HttpResponse(
                        content=f"Webhook received: {event["type"]} | FAILED \
                            Request denied: User instance is already activated",
                        status=400,)

            if inactive_user_found:
                if activation_email_sent:
                    return HttpResponse(
                        content=f"Webhook received: {event["type"]} | SUCCESS: \
                            User with id:{inactive_user_id} was found and an \
                            activation email was sent",
                        status=200,)
                else:
                    return HttpResponse(
                        content=f"Webhook received: {event["type"]} | ERROR: \
                            Activation email could not be sent: {str(email_error)}",
                        status=500,)
            else:
                return HttpResponse(
                        content=f"Webhook received: {event["type"]} | FAILED \
                            Inactive user instance could not be found in database",
                        status=400,)
        except Exception as e:
            return HttpResponse(
                content=f"Webhook received: {event["type"]} | ERROR {str(e)}",
                status=500,)

    def handle_payment_intent_payment_failed_event(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        Check if a record identified by inactive_user_id from payment intent's
        metadata exists in the database, if so make up to 10 attempts
        to delete, at 500ms intervals
        """
        try:
            # get id of inactive user in db from payment intent metadata
            intent = event.data.object
            inactive_user_id = int(intent.metadata.get('inactive_user_id'))
            confirm_inactive_user_deleted = False
            attempt = 1
            while attempt <= 10:
                try:
                    user = User.objects.get(id=inactive_user_id)  # get inactive user instance
                except User.DoesNotExist:
                    confirm_inactive_user_deleted = True
                    break
                if not user.is_active:
                    try:
                        user.delete()
                    except Exception as e:
                        deletion_error = e
                        attempt += 1
                        time.sleep(.5)  # wait 500 ms before retrying delete
                        continue
                else:
                    return HttpResponse(
                        content=f"Webhook received: {event["type"]} | FAILED \
                            Request denied: User instance is active and \
                            therefore cannot be deleted from the database",
                        status=400,)

            if confirm_inactive_user_deleted:
                return HttpResponse(
                    content=f"Webhook received: {event["type"]} | SUCCESS: \
                        Confirmed that no user with id:{inactive_user_id} \
                        exists in database",
                    status=200,)
            else:
                return HttpResponse(
                    content=f"Webhook received: {event["type"]} | ERROR \
                        Could not confirm deletion of inactive user \
                        from database: {str(deletion_error)}",
                    status=500,)
        except Exception as e:
            return HttpResponse(
                content=f"Webhook received: {event["type"]} | ERROR {str(e)}",
                status=500,)
