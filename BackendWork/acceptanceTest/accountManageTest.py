from django.test import TestCase
from BackendWork.models import User
from django.test import Client
import json


class accountManageTest(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()

    def testCorrectChange(self):
        resp = self.client.post("/register/",
                                json.dumps({"username": "Bob", "password1": "MikeMore123",
                                            "password2": "MikeMore123", "email": "LuvBob@gmail.com"}),
                                content_type="application/json")

        resp = self.client.post("/account/",
                                json.dumps({"username": "Bob", "first_name": "Bob",
                                            "last_name": "Bob", "phone_number": "1234567890",
                                            "email": "LuvBob@gmail.com"}), content_type="application/json")
        self.assertTrue(resp.status_code == 200, "Info change should be accepted")

    def testIncorrectPhoneChange(self):
        resp = self.client.post("/register/",
                                json.dumps({"username": "Bob", "password1": "MikeMore123",
                                            "password2": "MikeMore123", "email": "LuvBob@gmail.com"}),
                                content_type="application/json")

        resp = self.client.post("/account/",
                                json.dumps({"username": "Bob", "first_name": "Bob",
                                            "last_name": "Bob", "phone_number": "123456789",
                                            "email": "LuvBob@gmail.com"}), content_type="application/json")
        self.assertTrue(resp.status_code == 401, "Phone number change should not pass")

    def testIncorrectEmailChange(self):
        resp = self.client.post("/register/",
                                json.dumps({"username": "Bob", "password1": "MikeMore123",
                                            "password2": "MikeMore123", "email": "LuvBob@gmail.com"}),
                                content_type="application/json")

        resp = self.client.post("/account/",
                                json.dumps({"username": "Bob", "first_name": "Bob",
                                            "last_name": "Bob", "phone_number": "1234567890",
                                            "email": "LuvBob"}), content_type="application/json")
        self.assertTrue(resp.status_code == 401, "Email change should not pass")

    def testNullChange(self):
        resp = self.client.post("/register/",
                                json.dumps({"username": "Bob", "password1": "MikeMore123",
                                            "password2": "MikeMore123", "email": "LuvBob@gmail.com"}),
                                content_type="application/json")

        resp = self.client.post("/account/",
                                json.dumps({"username": "", "first_name": "Bob",
                                            "last_name": "Bob", "phone_number": "1234567890",
                                            "email": "LuvBob@gmail.com"}), content_type="application/json")
        self.assertTrue(resp.status_code == 401, "Null username should not pass")

        resp = self.client.post("/account/",
                                json.dumps({"username": "Bob", "first_name": "",
                                            "last_name": "Bob", "phone_number": "1234567890",
                                            "email": "LuvBob@gmail.com"}), content_type="application/json")
        self.assertTrue(resp.status_code == 200, "Null first name should pass")

        resp = self.client.post("/account/",
                                json.dumps({"username": "Bob", "first_name": "Bob",
                                            "last_name": "", "phone_number": "1234567890",
                                            "email": "LuvBob@gmail.com"}), content_type="application/json")
        self.assertTrue(resp.status_code == 200, "Null last name should pass")

        resp = self.client.post("/account/",
                                json.dumps({"username": "Bob", "first_name": "Bob",
                                            "last_name": "Bob", "phone_number": "",
                                            "email": "LuvBob@gmail.com"}), content_type="application/json")
        self.assertTrue(resp.status_code == 200, "Null phone number should pass")

        resp = self.client.post("/account/",
                                json.dumps({"username": "Bob", "first_name": "Bob",
                                            "last_name": "Bob", "phone_number": "1234567890",
                                            "email": ""}), content_type="application/json")
        self.assertTrue(resp.status_code == 401, "Null email should not pass")
