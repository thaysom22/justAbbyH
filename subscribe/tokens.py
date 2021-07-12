# import django API for creating onetime link with user details
from django.contrib.auth.tokens import PasswordResetTokenGenerator

# six.text_type required for python 2/3 compatibility?


# CREDIT[9]
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return user.id + timestamp


# instantiate token generator to export
account_activation_token_generator = AccountActivationTokenGenerator()