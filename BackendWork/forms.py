# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import User, Product, Storefront


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username", "first_name", "last_name", "phone_number", "shipping_address", "billing_address")

    def clean_confirm_password(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('password2')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class StorefrontForm(forms.ModelForm):
    class Meta:
        model = Storefront
        fields = ['name', 'description', 'bannerImage', 'logoImage']


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['soldByStoreId', 'name', 'description', 'price', 'qoh', 'category', 'weight',
                  'length', 'width', 'height', 'image']
