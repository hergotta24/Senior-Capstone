from django.test import TestCase
from BackendWork.models import User
from django.test import Client


class LoginTest(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()
        self.userList = {"Mike": "Mike", "Bob": "Bob"}

        for i in self.userList.keys():
            temp = User(username=i, password=i)
            temp.save()

    def testCorrectLogin(self):
        for i in self.userList.keys():
            resp = self.client.post("/login/", {"username": i, "password": i})
            print(self.client.get("username"))
            assert (resp.status_code == 200, "username not passed from Login to list")


class TestIncorrectLogin(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()
        self.userList = {"Mike": "Mike", "Bob": "Bob"}

        for i in self.userList.keys():
            temp = User(username=i, password=i)
            temp.save()

    def test_incorrectPassword(self):
        for i in self.userList.keys():
            resp = self.client.post("/login/", {"username": "Mike", "password": "Bob"}, follow=True)
            self.assertTrue(resp.status_code == 401, "Test shouldn't pass due to incorrect username.")

    def test_incorrectUsername(self):
        for i in self.userList.keys():
            resp = self.client.post("/login/", {"username": "Low", "password": "Mike"}, follow=True)
            self.assertTrue(resp.status_code == 401, "Test shouldn't pass due to incorrect password.")
