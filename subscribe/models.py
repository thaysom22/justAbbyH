from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class Subscription(models.Model):
    """
    Stores data for a subscription
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # related_name='subscription'
    start_date = models.DateField(auto_now_add=True)
    country = CountryField(blank_label='Country')  # relates country names to ISO codes
    city = models.CharField(max_length=100, default='')
    stripe_pid = models.CharField(max_length=254, unique=True, default='')

    def __str__(self):
        if hasattr(self, 'id'):
            return f"Subscription <id:{self.id}>"
        else:
            return "Unsaved Subscription object"

    