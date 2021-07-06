from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class Subscription(models.Model):
    """
    Stores data for a subscription
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  # related_name='subscription'
    start_date = models.DateField(auto_now_add=True)
    country = CountryField(blank_label='Country', blank=True, default='')  # relates country names to ISO codes
    city = models.CharField(blank=True, max_length=50, default='')
    stripe_pid = models.CharField(max_length=254, default='')

    def __str__(self):
        return f"Subscription <created:{self.start_date}> for <user:{self.user.username}>"

    