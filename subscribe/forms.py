from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Subscription


class UserRegisterForm(UserCreationForm):
    """
    Subclass of UserCreationForm with edits
    to UI for user form
    """
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        help_texts = {
            'username': "",
            'password1': "",
            'password2': "",
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, remove labels,
        set autofocus on first input
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Enter a Username',
            'password1': 'Enter a Password',
            'password2': 'Repeat Password',
        }

        for field in self.fields:
            self.fields[field].label = False
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]

        self.fields['username'].widget.attrs['autofocus'] = True


class SubscriptionForm(forms.ModelForm):
    """
    ModelForm subclass which helps implement UI
    for subscription form on subscribe page
    """
    class Meta:
        model = Subscription
        fields = ('first_name', 'last_name',
                  'email', 'country', 'city',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, remove labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'city': 'City (optional)',
        }

        for field in self.fields:
            self.fields[field].label = False
            if field != 'country':
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]
        
        

    