from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  # ModelForm subclass

from .models import Subscription


class UserRegisterForm(UserCreationForm):
    """
    Subclass of UserCreationForm with edits
    to UI for user form
    """
    class Meta:
        model = User
        fields = ("username", "first_name", 
                  "last_name", "email", 
                  "password1", "password2")

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, remove labels,
        set autofocus on first input, make 
        all fields required
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': 'Username*',
            'first_name': 'First Name*',
            'last_name': 'Last Name*',
            'email': 'Email Address*',
            'password1': 'Password*',
            'password2': 'Repeat Password*',
        }

        for field in self.fields:
            self.fields[field].label = False
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]
            self.fields[field].required = True

        self.fields['username'].widget.attrs['autofocus'] = True


class SubscriptionForm(forms.ModelForm):
    """
    ModelForm subclass which helps implement UI
    for subscription form on subscribe page
    """
    class Meta:
        model = Subscription
        fields = ('country', 'city',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, remove labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'city': 'City',
        }

        for field in self.fields:
            self.fields[field].label = False
            if field != 'country':
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]
        
        

    