from django.test import TestCase, Client
import json
from BackendWork.forms import AddProductForm
from BackendWork.models import User, Storefront, Product


class AddProductTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testUser', password='p@55w0rD', email='testuser@gmail.com')
        self.storefront = Storefront.objects.create(owner=self.user, name='Test Storefront')
        self.form_data = {
            'soldByStoreId': self.storefront.storeId,
            'name': 'Test Product',
            'description': 'Description',
            'price': 9.99,
            'qoh': 99,
            'weight': 1.0,
            'length': 1.0,
            'width': 1.0,
            'height': 1.0
        }

    def testAddProductPageAccessible(self):  # might technically be an acceptance test?
        self.client.login(username='testUser', password='p@55w0rD')
        response = self.client.get(f'/createproduct/{self.storefront.storeId}/')
        self.assertEqual(response.status_code, 200, "add product page not returning 200 OK")

    def testAddProductSuccessRedirect(self):  # might technically be an acceptance test?
        self.client.login(username='testUser', password='p@55w0rD')
        response = self.client.post(f'/createproduct/{self.storefront.storeId}/', json.dumps(self.form_data),
                                    content_type="application/json", follow=True)
        self.assertEqual(response.status_code, 200, "add product page not returning 200 OK upon success")

    def testAddProductNotLoggedIn(self):  # might technically be an acceptance test?
        response = self.client.post(f'/createproduct/{self.storefront.storeId}/', json.dumps(self.form_data),
                                    content_type="application/json", follow=True)
        self.assertTemplateUsed(response, "login.html")

    def testAddProductWrongUser(self):  # might technically be an acceptance test?
        self.user2 = User.objects.create_user(username='wrongUser', password='p@55w0rD', email='wronguser@gmail.com')
        self.storefront2 = Storefront.objects.create(owner=self.user2, name='Test Storefront 2')
        self.client.login(username='wrongUser', password='p@55w0rD')
        response = self.client.post(f'/createproduct/{self.storefront.storeId}/', json.dumps(self.form_data),
                                    content_type="application/json", follow=True)
        self.assertEqual(response.status_code, 403, "adding a product to a storefront you don't own "
                                                    "should return 403 forbidden")
        with self.assertRaises(Product.DoesNotExist, msg="newProduct should not have been added to database"):
            Product.objects.get(name='Test Product')

    def testAddProductDatabaseCheck(self):  # might technically be an acceptance test?
        self.client.login(username='testUser', password='p@55w0rD')
        self.client.post(f'/createproduct/{self.storefront.storeId}/', json.dumps(self.form_data),
                         content_type="application/json", follow=True)
        newProduct = Product.objects.get(name='Test Product')
        self.assertEqual(newProduct.soldByStoreId_id, self.form_data['soldByStoreId'], "soldByStoreId mismatch")
        self.assertEqual(newProduct.name, self.form_data['name'], "name mismatch")
        self.assertEqual(newProduct.description, self.form_data['description'], "description mismatch")
        self.assertEqual(float(newProduct.price), self.form_data['price'], "price mismatch")
        self.assertEqual(newProduct.qoh, self.form_data['qoh'], "qoh mismatch")
        self.assertEqual(newProduct.weight, self.form_data['weight'], "weight mismatch")
        self.assertEqual(newProduct.length, self.form_data['length'], "length mismatch")
        self.assertEqual(newProduct.width, self.form_data['width'], "width mismatch")
        self.assertEqual(newProduct.height, self.form_data['height'], "height mismatch")

    def testAddProductFormValid(self):
        form = AddProductForm(data=self.form_data)
        self.assertTrue(form.is_valid(), "valid form data returned false")

    def testAddDuplicateProduct(self):
        Product.objects.create(soldByStoreId=self.storefront, name='Test Product', description='Description',
                               price=9.99, qoh=99, weight=1.0, length=1.0, width=1.0, height=1.0)
        form = AddProductForm(data=self.form_data)
        self.assertFalse(form.is_valid(), "product already exists for this storefront with this name")

    def testAddProductFormInvalidName(self):
        self.form_data['name'] = ''
        form = AddProductForm(data=self.form_data)
        self.assertFalse(form.is_valid(), "form data missing product name")

    def testAddProductFormInvalidDescription(self):
        self.form_data['description'] = ''
        form = AddProductForm(data=self.form_data)
        self.assertFalse(form.is_valid(), "form data missing product description")

    def testAddProductFormInvalidPrice(self):
        self.form_data['price'] = 0
        form = AddProductForm(data=self.form_data)
        self.assertFalse(form.is_valid(), "form data has product price of $0.00")

        self.form_data['price'] = -3.14
        form = AddProductForm(data=self.form_data)
        self.assertFalse(form.is_valid(), "form data has negative product price")

    def testAddProductFormInvalidQOH(self):
        self.form_data['qoh'] = -1
        form = AddProductForm(data=self.form_data)
        self.assertFalse(form.is_valid(), "form data has negative product QOH")

    def testAddProductFormInvalidStorefront(self):
        self.form_data['soldByStoreId'] = -1
        form = AddProductForm(data=self.form_data)
        self.assertFalse(form.is_valid(), "form data has invalid storefront ID")

    def testAddProductFormInvalidWeight(self):
        self.form_data['weight'] = 0
        form = AddProductForm(data=self.form_data)
        self.assertFalse(form.is_valid(), "form data has invalid weight")

    def testAddProductFormInvalidLength(self):
        self.form_data['length'] = 0
        form = AddProductForm(data=self.form_data)
        self.assertFalse(form.is_valid(), "form data has invalid length")

    def testAddProductFormInvalidWidth(self):
        self.form_data['width'] = 0
        form = AddProductForm(data=self.form_data)
        self.assertFalse(form.is_valid(), "form data has invalid width")

    def testAddProductFormInvalidHeight(self):
        self.form_data['height'] = 0
        form = AddProductForm(data=self.form_data)
        self.assertFalse(form.is_valid(), "form data has invalid height")
