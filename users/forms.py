from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        """
        Class meta gives us a nested namespace for configurations and keeps them in one place.
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']
