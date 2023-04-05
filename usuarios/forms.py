from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    username=forms.CharField(min_length=8, max_length=16)
    password=forms.PasswordInput()
