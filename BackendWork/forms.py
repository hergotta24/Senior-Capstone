# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import modUser


class modUserCreationForm(UserCreationForm):
    class Meta:
        model = modUser
        fields = ("username", "email")


class modUserChangeForm(UserChangeForm):
    class Meta:
        model = modUser
        fields = ("username", "email")
