import unittest
from bs4 import BeautifulSoup
from test_case.page_obj.login_controller import Login
from test_case.models.config import username, password

class MyTest(unittest.TestCase):

    def setUp(self):
        data = {
            'username': username,
            'password': password
            }
        login_state = Login()
        login_state.user_login(data)
        self.BeautifulSoup = BeautifulSoup

    def tearDown(self):
        login_state = Login()
        login_state.user_logout()