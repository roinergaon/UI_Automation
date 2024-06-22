from pageObjects.login_page import LoginPage
from utilities.base_test import BaseClass


class TestLoginPage(BaseClass):
    def test_tc_01(self):
        login_page = LoginPage(self.driver)
        login_page.login("roi", "password")
