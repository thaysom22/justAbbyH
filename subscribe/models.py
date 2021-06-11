from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class Subscription(models.Model):
    """
    Stores data about a user subscription
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=False, null=False, max_length=254)
    first_name = models.CharField(blank=False, null=False, max_length=50)
    last_name = models.CharField(blank=False, null=False, max_length=50)
    start_date = models.DateField(auto_now_add=True)
    country = CountryField(blank_label='Country', blank=True, null=True)  # relates country names to ISO codes
    city = models.CharField(blank=True, null=True, max_length=50)