import os
import sys

#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import allure

from base_test import LoginBaseClass
from pageObjects.login_page import LoginPage
from pageObjects.products_page import ProductsPage

class TestLoginPage(LoginBaseClass):
    @allure.description("Verify that user can't log in with invalid username")
    @allure.title("Invalid username test")
    @allure.feature("Login tests")
    @allure.tag("Login tests")
    def test_tc_01(self):
        login_page = LoginPage(self.driver)
        with allure.step("Enter invalid user name"):
            user_name = self.get_test_case_data('login_page_test_data','test_case_1', 'username')
        with allure.step("Enter password"):
            password = self.get_test_case_data('login_page_test_data','test_case_1', 'password')
        with allure.step("Press login"):
            login_page.login(user_name, password)
        error_message = login_page.get_text(login_page.error_label)
        test_case_data = self.get_test_case_data('login_page_test_data','test_case_1', 'expected_result')
        assert test_case_data in error_message

    @allure.description("Verify that user can't log in with invalid password")
    @allure.title("Invalid password test")
    @allure.feature("Login tests")
    @allure.tag("Login tests")
    def test_tc_02(self):
        #log = self.get_logger()
        #log.info("")

        login_page = LoginPage(self.driver)
        with allure.step("Enter user name"):
            user_name = self.get_test_case_data('login_page_test_data', 'test_case_2', 'username')
        with allure.step("Enter password"):
            password = self.get_test_case_data('login_page_test_data', 'test_case_2', 'password')
        with allure.step("Press login"):
            login_page.login(user_name, password)
        error_message = login_page.get_text(login_page.error_label)
        test_case_data = self.get_test_case_data('login_page_test_data', 'test_case_2', 'expected_result')
        assert test_case_data in error_message

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
        with allure.step("Enter user name"):
            user_name = self.get_test_case_data('login_page_test_data', 'test_case_4', 'username')
        with allure.step("Enter password"):
            password = self.get_test_case_data('login_page_test_data', 'test_case_4', 'password')
        with allure.step("Press login"):
            login_page.login(user_name, password)
        error_message = login_page.get_text(login_page.error_label)
        test_case_data = self.get_test_case_data('login_page_test_data', 'test_case_4', 'expected_result')
        assert test_case_data in error_message
    @allure.description("Verify that user can't log in with empty username and empty password fields")
    @allure.title("Empty username and password test")
    @allure.feature("Login tests")
    @allure.tag("Login tests")
    def test_tc_05(self):
        login_page = LoginPage(self.driver)
        with allure.step("Enter user name"):
            user_name = self.get_test_case_data('login_page_test_data', 'test_case_5', 'username')
        with allure.step("Enter password"):
            password = self.get_test_case_data('login_page_test_data', 'test_case_5', 'password')
        with allure.step("Press login"):
            login_page.login(user_name, password)
        error_message = login_page.get_text(login_page.error_label)
        test_case_data = self.get_test_case_data('login_page_test_data', 'test_case_5', 'expected_result')
        assert test_case_data in error_message

    @allure.description("Verify that user can log in with valid username and password")
    @allure.title("Valid username test")
    @allure.feature("Login tests")
    @allure.tag("Login tests")
    def test_tc_06(self):
        login_page = LoginPage(self.driver)
        with allure.step("Enter user name"):
            user_name = self.get_test_case_data('login_page_test_data', 'test_case_6', 'username')
        with allure.step("Enter password"):
            password = self.get_test_case_data('login_page_test_data', 'test_case_6', 'password')
        with allure.step("Press login"):
            login_page.login(user_name, password)
        product_pages = ProductsPage(self.driver)
        title = login_page.get_text(product_pages.title)
        test_case_data = self.get_test_case_data('login_page_test_data', 'test_case_6', 'expected_result')
        assert test_case_data == title


