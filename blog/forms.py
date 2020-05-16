from django import forms

from blog.models import User_profile
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


class create_user(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class edit_profile(UserChangeForm):
    class Meta:
        model=User
        fields=['email','first_name','last_name']


