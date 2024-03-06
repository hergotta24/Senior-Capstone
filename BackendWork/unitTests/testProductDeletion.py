from django.test import TestCase
from BackendWork.models import *
from django.test import Client


class TestProductDeletion(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User(username="testuser", email="email@gmail.com", password="<PASSWORD>")
        self.user.save()
        self.client.storefront = Storefront(owner=self.user, name="testname", description="testdescription")
        self.client.storefront.save()
        self.product1 = Product(price=10.02, weight=15.1, name="testProduct", length=10, width=10, height=10,
                               soldByStoreId=self.client.storefront)
        self.product1.save()
        self.product2 = Product(price=10.02, weight=15.1, name="testProduct2", length=10, width=10, height=10,
                                soldByStoreId=self.client.storefront)
        self.product2.save()

    def testProductDeletion(self):
        product_id = self.product1.productId
        # Product.objects.filter(productId=product_id).delete()
        print(product_id)
        print(int(str(product_id)))
        self.client.get("delete/" + str(product_id) + "/")
        # I need to figure out what to pass into the post, I know it will work if I find the right thing because
        # The comment before this works, and that's all that the view calls
        self.assertFalse(Product.objects.filter(productId=product_id).exists())

    def testMultipleItems(self):    # to make sure it isn't deleting everything
        product_id1 = self.product1.productId
        product_id2 = self.product2.productId
        Product.objects.filter(productId=product_id1).delete()
        self.assertTrue(Product.objects.filter(productId=product_id2).exists())

    def testMultipleDeletions(self):
        product_id1 = self.product1.productId
        product_id2 = self.product2.productId
        Product.objects.filter(productId=product_id1).delete()
        Product.objects.filter(productId=product_id2).delete()
        self.assertFalse(Product.objects.filter(productId=product_id1).exists() and
                         Product.objects.filter(productId=product_id2).exists())


