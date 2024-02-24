from django.test import TestCase
from BackendWork.models import User
from django.test import Client
import json


class registerTest(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()

    def testCorrectRegister(self):
        resp = self.client.post("/register/",
                                json.dumps({"username": "Bob", "password1": "MikeMore123",
                                 "password2": "MikeMore123", "email": "LuvBob@gmail.com"}), content_type="application/json")
        self.assertTrue(resp.status_code == 200, "registration did not pass with correct info")

    def testIncorrectPasswordRegister(self):
        resp = self.client.post("/register/",
                                json.dumps({"username": "Bob", "password1": "MikeMore123",
                                 "password2": "Test12", "email": "LuvBob@gmail.com"}), content_type="application/json")
        self.assertTrue(resp.status_code == 401, "Test shouldn't pass due to incorrect unmatched password")

    def testIncorrectEmailRegister(self):
        resp = self.client.post("/register/",
                                json.dumps({"username": "Bob", "password1": "MikeMore123",
                                 "password2": "MikeMore123", "email": "LuvBob"}), content_type="application/json")
        self.assertTrue(resp.status_code == 401, "Test shouldn't pass due to invalid email")

    def testNullRegister(self):
        resp = self.client.post("/register/",
                                json.dumps({"username": "", "password1": "MikeMore123",
                                 "password2": "MikeMore123", "email": "LuvBob@gmail.com"}), content_type="application/json")
        self.assertTrue(resp.status_code == 401, "Test shouldn't pass due to null case")

        resp = self.client.post("/register/",
                                json.dumps({"username": "Bob", "password1": "",
                                 "password2": "MikeMore123", "email": "LuvBob@gmail.com"}), content_type="application/json")
        self.assertTrue(resp.status_code == 401, "Test shouldn't pass due to null case")

        resp = self.client.post("/register/",
                                json.dumps({"username": "Bob", "password1": "MikeMore123",
                                 "password2": "", "email": "LuvBob@gmail.com"}), content_type="application/json")
        self.assertTrue(resp.status_code == 401, "Test shouldn't pass due to null case")

        resp = self.client.post("/register/",
                                json.dumps({"username": "Bob", "password1": "MikeMore123",
                                 "password2": "MikeMore123", "email": ""}), content_type="application/json")
        self.assertTrue(resp.status_code == 401, "Test shouldn't pass due to null case")
