from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    pass
    userid = models.CharField(max_length=20, unique=True, primary_key=True, default="001")
    username = models.CharField(max_length=20, unique=True, default="Bob")
    password = models.CharField(max_length=20, default="Builder")
    email = models.EmailField(unique=True, default="BobBuilder@gmail.com")
    firstName = models.CharField(max_length=30, default="Bob")
    lastName = models.CharField(max_length=30, default="Builder")
    phoneNumber = models.CharField(max_length=10, default="0000000000")
    shippingAddressId = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True,
                                          related_name="userShippingAddress", blank=True)
    billingAddressId = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True,
                                         related_name="userBillingAddress", blank=True)
    registrationDate = models.DateTimeField(default= timezone.now)


class Address(models.Model):
    STATE_CHOICES = [('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'),
                     ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'),
                     ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'),
                     ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'),
                     ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'),
                     ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'),
                     ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'),
                     ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'),
                     ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'),
                     ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'),
                     ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'),
                     ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('AS', 'American Samoa'),
                     ('GU', 'Guam'), ('MP', 'Northern Mariana Islands'), ('PR', 'Puerto Rico'), ('VI', 'Virgin Islands')
                     ]

    addressId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    line1 = models.CharField(max_length=50)
    line2 = models.CharField(max_length=50)
    aptNum = models.CharField(max_length=10, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zipCode = models.CharField(max_length=5)


class Storefront(models.Model):
    storeId = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True)
    logoURL = models.URLField(max_length=100, null=True)
    bannerURL = models.URLField(max_length=100, null=True)
    videoURL = models.URLField(max_length=100, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)


class CustomerReviews(models.Model):
    reviewId = models.AutoField(primary_key=True)
    customerId = models.ForeignKey(User, on_delete=models.CASCADE)
    reviewerId = models.ForeignKey(Storefront, on_delete=models.SET_NULL, null=True)
    rating = models.PositiveIntegerField()
    comment = models.CharField(max_length=500)
    reviewDate = models.DateTimeField(auto_now_add=True)


class StoreReviews(models.Model):
    reviewId = models.AutoField(primary_key=True)
    storeId = models.ForeignKey(Storefront, on_delete=models.CASCADE)
    reviewerId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.PositiveIntegerField()
    comment = models.CharField(max_length=500)
    reviewDate = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    soldByStoreId = models.ForeignKey(Storefront, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    qoh = models.PositiveIntegerField(default=0, verbose_name='Quantity on Hand')
    categoryId = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    subCategoryId = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True)
    weight = models.FloatField()
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    dateAdded = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)


class SubCategory(models.Model):
    subCategoryId = models.AutoField(primary_key=True)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)


class ProductVideos(models.Model):
    videoId = models.AutoField(primary_key=True)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    videoURL = models.URLField(max_length=100)
    videoTitle = models.CharField(max_length=30)
    videoDescription = models.CharField(max_length=500, null=True)


class ProductImages(models.Model):
    imageId = models.AutoField(primary_key=True)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    imageURL = models.URLField(max_length=100)
    imageTitle = models.CharField(max_length=30)
    imageDescription = models.CharField(max_length=500, null=True)


class ProductQuestions(models.Model):
    questionId = models.AutoField(primary_key=True)
    askedById = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    dateAsked = models.DateTimeField(auto_now_add=True)
    answer = models.CharField(max_length=500)
    dateAnswered = models.DateTimeField(default=None)


class ProductReviews(models.Model):
    reviewId = models.AutoField(primary_key=True)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewerId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.PositiveIntegerField()
    comment = models.CharField(max_length=500)
    reviewDate = models.DateTimeField(auto_now_add=True)


class Invoice(models.Model):
    reviewId = models.AutoField(primary_key=True)
    storeId = models.ForeignKey(Storefront, on_delete=models.SET_NULL, null=True)
    customerId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    tax = models.DecimalField(max_digits=8, decimal_places=2)
    shipping = models.DecimalField(max_digits=8, decimal_places=2)
    orderStatus = models.CharField(max_length=20)
    invoiceDate = models.DateTimeField(auto_now_add=True)


class LineItem(models.Model):
    lineItemId = models.AutoField(primary_key=True)
    invoiceId = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    linePrice = models.DecimalField(max_digits=8, decimal_places=2)


class DisputeTicket(models.Model):
    initiatorId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="initiatedTickets")
    invoiceId = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    disputeDetails = models.CharField(max_length=1000)
    disputeDate = models.DateTimeField(auto_now_add=True)
    disputeStatus = models.CharField(max_length=20)
    resolvedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,  related_name="resolvedTickets")
    resolutionDetails = models.CharField(max_length=1000)
    resolutionDate = models.DateTimeField()
