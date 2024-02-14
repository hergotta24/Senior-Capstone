# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username", "password", "firstName", "lastName", "phoneNumber", "registrationDate")


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "username", "password", "firstName", "lastName", "phoneNumber", "registrationDate")
