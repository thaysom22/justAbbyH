from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField

import uuid


class Subscription(models.Model):
    """
    Stores data for a subscription
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # related_name='subscription'
    start_date = models.DateField(auto_now_add=True)
    country = CountryField(blank_label='Country')  # relates country names to ISO codes
    city = models.CharField(max_length=50)
    stripe_pid = models.CharField(max_length=254, unique=True)

    def __str__(self):
        if hasattr(self, 'id'):
            return f"Subscription <uuid:{self.id}>"
        else:
            return "Unsaved Subscription object"

    