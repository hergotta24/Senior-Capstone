from django.test import TestCase
from BackendWork.models import *
from django.test import Client


class TestProductDeletion(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create()
        self.product.save()

    def testProductDeletion(self):
        Product.objects.filter(productId=1).delete()
        self.assertFalse(Product.objects.filter(productId=1).exists())
