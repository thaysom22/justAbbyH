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
        Add labels,
        make all fields required
        """
        super().__init__(*args, **kwargs)
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'password1': 'Password',
            'password2': 'Repeat Password',
        }

        self.fields["password1"].help_text = 'Your password must contain at least 8 characters.'
        for field in self.fields:
            self.fields[field].widget.attrs.pop("autofocus", None)
            self.fields[field].label = labels[field]


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
        Add labels and remove autofocus from all fields
        """
        super().__init__(*args, **kwargs)
        labels = {
            'city': 'City',
            'country': 'Country',
        }

        for field in self.fields:
            self.fields[field].widget.attrs.pop("autofocus", None)
            self.fields[field].label = labels[field]
            if field == 'country':
                current_classes = self.fields['country'].widget.attrs.get(
                    'class', '')
                if current_classes:
                    self.fields['country'].widget.attrs.update(
                        {'class': f'{current_classes} form-select'})
                else:
                    self.fields['country'].widget.attrs['class'] = 'form-select'
