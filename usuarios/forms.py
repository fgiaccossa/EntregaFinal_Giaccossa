from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(min_length=8, max_length=16)
    password = forms.PasswordInput()

    #class Meta:
     #   model = User
      #  fields = ("Email", "Usuario")
        #field_classes = {"Usuario": UsernameField}


