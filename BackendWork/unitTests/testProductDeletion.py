from django.test import TestCase
from BackendWork.models import *
from django.test import Client


class TestProductDeletion(TestCase):
    def setUp(self):
        self.client = Client()

        #  self.client.storefront = Storefront()
        #  self.product = Product(price=10.02, weight=15.1, name="testProduct", length=10, width=10, height=10, soldByStoreId=5)
        #  self.product.save()

    def testProductDeletion(self):
        product_id = self.product.productId
        print(product_id)
        Product.objects.filter(productId=product_id).delete()
        self.assertFalse(Product.objects.filter(productId=product_id).exists())
