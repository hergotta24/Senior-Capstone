from django.test import TestCase
from BackendWork.models import User
from django.test import Client

class TestAccountManage(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()
        self.user = User(username="Jeff", email="example@gmail.com", password="Password", first_name="Jeff",
                    last_name="Jefferson", phone_number=4144144414)
        self.user.save()
        login = self.client.login(username="Jeff", password="Password")

    def testChangeUsername(self):
        resp = self.client.post("/Account/Manage/", data={"username": "newYearNewJeff"})
        assert self.user.username == "newYearNewJeff"

    def testChangeEmail(self):
        resp = self.client.post("/Account/Manage/", data={"email": "newemail@gmail.com"})
        assert self.user.email == "newemail@gmail.com"

    def testChangePhoneNumber(self):
        resp = self.client.post("/Account/Manage/", data = {"phone_number": "1111111111"})
        assert self.user.phone_number == "1111111111"

    def testChangeFirstName(self):
        resp = self.client.post("/Account/Manage/", data={"firstname": "Jeffrey"})
        assert self.user.first_name == "Jeffrey"

    def testChangeLastName(self):
        resp = self.client.post("/Account/Manage/", data={"lastname": "Namey"})
        assert self.user.last_name == "Namey"

    def testChangeAll(self):
        resp = self.client.post("/Account/Manage/", data={"username": "newYearNewJeff", "email": "newemail@gmail",
                                                          "phone_number": "1111111111", "firstname": "Jeffrey",
                                                          "lastname": "Namey"})
        assert (self.user.first_name == "Jeffrey" and self.user.last_name == "Namey" and
                self.user.phone_number == "1111111111" and self.user.email == "newemail@gmail.com" and
                self.user.username == "newYearNewJeff" and self.user)

    def testBadPhoneNumber(self):
        resp = self.client.post("/Account/Manage/", data = {"phone_number": "0"})
        self.assertTrue(resp.status_code == 401, "test shouldn't pass with invalid phone number")

    def testBadEmail(self):
        resp = self.client.post("/Account/Manage/", data = {"email": "230894"})
        self.assertTrue(resp.status_code == 401, "test shouldn't pass with invalid email")

