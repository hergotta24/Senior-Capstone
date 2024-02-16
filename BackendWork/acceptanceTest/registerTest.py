from django.test import TestCase
from BackendWork.models import User
from django.test import Client


class registerTest(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()

    def testCorrectRegister(self):
        resp = self.client.post("/register/",
                                {"username": "Bob", "password1": "Password",
                                 "password2": "Password", "email": "LuvBob@gmail.com"})
        assert (resp.status_code == 200, "registration did not pass with correct info")

    def testIncorrectPasswordRegister(self):
        resp = self.client.post("/register/",
                                {"username": "Bob", "password1": "Password",
                                 "password2": "password", "email": "LuvBob@gmail.com"})
        self.assertTrue(resp.status_code == 401, "Test shouldn't pass due to incorrect unmatched password")

    def testIncorrectEmailRegister(self):
        resp = self.client.post("/register/",
                                {"username": "Bob", "password1": "Password",
                                 "password2": "Password", "email": "LuvBob"})
        self.assertTrue(resp.status_code == 401, "Test shouldn't pass due to invalid email")

    def testNullRegister(self):
        resp = self.client.post("/register/",
                                {"username": "", "password1": "Password",
                                 "password2": "Password", "email": "LuvBob@gmail.com"})
        self.assertTrue(resp.status_code == 401, "Test shouldn't pass due to null case")

        resp = self.client.post("/register/",
                                {"username": "Bob", "password1": "",
                                 "password2": "Password", "email": "LuvBob@gmail.com"})
        self.assertTrue(resp.status_code == 401, "Test shouldn't pass due to null case")

        resp = self.client.post("/register/",
                                {"username": "Bob", "password1": "Password",
                                 "password2": "", "email": "LuvBob@gmail.com"})
        self.assertTrue(resp.status_code == 401, "Test shouldn't pass due to null case")

        resp = self.client.post("/register/",
                                {"username": "Bob", "password1": "Password",
                                 "password2": "Password", "email": ""})
        self.assertTrue(resp.status_code == 401, "Test shouldn't pass due to null case")
