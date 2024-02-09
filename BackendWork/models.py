from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


# Create your models here.
class modUser(AbstractUser):
    pass
    password = models.CharField(max_length=20, blank=True)
    firstName = models.CharField(max_length=20, blank=True)
    lastName = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=72, blank=True)
    phoneNumber = models.CharField(max_length=10, blank=True)
    registrationDate = models.DateTimeField(default=datetime.now, blank=True)
