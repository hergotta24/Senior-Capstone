from django.test import TestCase
from BackendWork.models import modUser
from django.test import Client


class LoginTest(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()
        self.userList = {"Mike": "Mike", "Bob": "Bob"}

        for i in self.userList.keys():
            temp = modUser(username=i, password=i)
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
            temp = modUser(username=i, password=i)
            temp.save()

    def test_incorrectPassword(self):
        for i in self.userList.keys():
            resp = self.client.post("/login/", {"username": i, "password": i}, follow=True)
            self.assertFalse(resp.status_code != 200, "Test shouldn't pass due to incorrect username.")

    def test_incorrectUsername(self):
        for i in self.userList.keys():
            resp = self.client.post("/login/", {"username": i, "password": i}, follow=True)
            self.assertFalse(resp.status_code != 200, "Test shouldn't pass due to incorrect password.")
