# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User, Address, Storefront, CustomerReviews, StoreReviews, Product, Category, SubCategory, \
    ProductVideos, ProductImages, ProductQuestions, ProductReviews, Invoice, LineItem, DisputeTicket


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ["email", "username", "password", "phone_number", "shipping_address", "billing_address"]
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Additional Information',
            {
                'fields': (
                    'phone_number',
                    'shipping_address',
                    'billing_address',

                )
            }
        )
    )


# Register models here
admin.site.register(User, UserAdmin)
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
