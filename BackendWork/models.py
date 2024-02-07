from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class modUser(AbstractUser):
    pass
    firstName = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    address = models.CharField(max_length=72)
    phoneNumber = models.CharField(max_length=10)
    registrationDate = models.CharField(max_length=10)
