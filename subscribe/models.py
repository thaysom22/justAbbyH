from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class Subscription(models.Model):
    """
    Stores data for a subscription
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    start_date = models.DateField(auto_now_add=True)
    country = CountryField(blank_label='Country (optional)', blank=True, null=True)  # relates country names to ISO codes
    city = models.CharField(blank=True, null=True, max_length=50)
    stripe_pid = models.CharField(max_length=254, default='')

    def __str__(self):
        return f"Subscription <id:{self.id}> <user:{self.user.username}>"

    