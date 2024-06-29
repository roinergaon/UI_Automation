import os
import sys

#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import allure
import pytest

from base_test import LoginBaseClass
from pageObjects.login_page import LoginPage
from pageObjects.products_page import ProductsPage
from tests_data.test_data import INVALID_LOGIN_CREDENTIALS, LOGIN_CREDENTIALS, EXPECTED_RESULTS


class TestLoginPage(LoginBaseClass):
    @allure.description("Verify that user can't log in with invalid username")
    @allure.title("Invalid username test")
    @allure.feature("Login tests")
    @allure.tag("Login tests")
    def test_tc_01(self):
        login_page = LoginPage(self.driver)
        #with allure.step("Enter invalid user name"):
        #with allure.step("Enter password"):
        with allure.step("Press login"):
            login_page.login(INVALID_LOGIN_CREDENTIALS["invalid_username"], LOGIN_CREDENTIALS["password"])
        error_message = login_page.get_text(login_page.error_label)
        assert EXPECTED_RESULTS[ "invalid_username_valid_password"] in error_message

    @allure.description("Verify that user can't log in with invalid password")
    @allure.title("Invalid password test")
    @allure.feature("Login tests")
    @allure.tag("Login tests")
    def test_tc_02(self):
        #log = self.get_logger()
        #log.info("")
        login_page = LoginPage(self.driver)
        with allure.step("Press login"):
            login_page.login(LOGIN_CREDENTIALS["username"], INVALID_LOGIN_CREDENTIALS["invalid_password"])
        error_message = login_page.get_text(login_page.error_label)
        assert EXPECTED_RESULTS[ "invalid_username_valid_password"] in error_message

    #@allure.description("Verify that user can't log in with empty username field")
    #@allure.title("Empty username test")
    #@allure.feature("Login tests")
    #@allure.tag("Login tests")
    #def test_tc_03(self):
    #    #log = self.get_logger()
    #    #log.info("Verify login functionality, check valid user name and password")
    #    login_page = LoginPage(self.driver)
    #    with allure.step("Enter user name"):
    #        user_name = self.get_test_case_data('login_page_test_data', 'test_case_3', 'username')
    #    with allure.step("Enter password"):
    #        password = self.get_test_case_data('login_page_test_data', 'test_case_3', 'password')
     #   with allure.step("Press login"):
     #       login_page.login(user_name, password)
     #   error_message = login_page.get_text(login_page.error_label)
     #   test_case_data = self.get_test_case_data('login_page_test_data', 'test_case_3', 'expected_result')
     #   assert test_case_data in error_message
    @allure.description("Verify that user can't log in with empty password field")
    @allure.title("Empty password test")
    @allure.feature("Login tests")
    @allure.tag("Login tests")
    def test_tc_04(self):
        login_page = LoginPage(self.driver)
        with allure.step("Press login"):
            login_page.login(LOGIN_CREDENTIALS["username"], "")
        error_message = login_page.get_text(login_page.error_label)
        assert EXPECTED_RESULTS["empty_password"] in error_message
    @allure.description("Verify that user can't log in with empty username and empty password fields")
    @allure.title("Empty username and password test")
    @allure.feature("Login tests")
    @allure.tag("Login tests")
    def test_tc_05(self):
        login_page = LoginPage(self.driver)
        with allure.step("Press login"):
            login_page.login("", "")
        error_message = login_page.get_text(login_page.error_label)
        assert EXPECTED_RESULTS["empty_username_password"] in error_message

    @allure.description("Verify that user can log in with valid username and password")
    @allure.title("Valid username test")
    @allure.feature("Login tests")
    @allure.tag("Login tests")
    def test_tc_06(self):
        login_page = LoginPage(self.driver)
        with allure.step("Press login"):
            login_page.login(LOGIN_CREDENTIALS ["username"], LOGIN_CREDENTIALS ["password"])
        product_pages = ProductsPage(self.driver)
        assert product_pages.is_displayed(product_pages.title)

    @allure.description("log out")
    @allure.title("log out")
    @allure.feature("Login tests")
    @allure.tag("Login tests")
    def test_tc_07(self):
        products_page = ProductsPage(self.driver)
        products_page.click_log_out()
        login_page = LoginPage(self.driver)
        is_displayed = login_page.is_displayed(login_page.login_button)
        assert is_displayed


