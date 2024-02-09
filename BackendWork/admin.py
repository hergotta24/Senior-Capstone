# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import modUserCreationForm, modUserChangeForm
from .models import modUser, User, Address, Storefront, CustomerReviews, StoreReviews, Product, Category, SubCategory, \
    ProductVideos, ProductImages, ProductQuestions, ProductReviews, Invoice, LineItem, DisputeTicket


class modUserAdmin(UserAdmin):
    add_form = modUserCreationForm
    form = modUserChangeForm
    model = modUser
    list_display = ["email", "username", "password", "firstName", "lastName", "phoneNumber", "registrationDate"]


# Register models here
admin.site.register(modUser, modUserAdmin)
admin.site.register(User)
admin.site.register(Address)
admin.site.register(Storefront)
admin.site.register(CustomerReviews)
admin.site.register(StoreReviews)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ProductVideos)
admin.site.register(ProductImages)
admin.site.register(ProductQuestions)
admin.site.register(ProductReviews)
admin.site.register(Invoice)
admin.site.register(LineItem)
admin.site.register(DisputeTicket)
