from django import forms
from .models import Contacts
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Message(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['firstname', 'lastname', 'country', 'message']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
