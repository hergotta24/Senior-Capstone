# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import modUserCreationForm, modUserChangeForm
from .models import modUser


class modUserAdmin(UserAdmin):
    add_form = modUserCreationForm
    form = modUserChangeForm
    model = modUser
    list_display = ["email", "username", "password", "firstName", "lastName", "phoneNumber", "registrationDate"]


admin.site.register(modUser, modUserAdmin)
