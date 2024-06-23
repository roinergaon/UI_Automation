import os
import sys

#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import allure
from pageObjects.login_page import LoginPage
from pageObjects.products_page import ProductsPage
from utils.base_test import BaseClass

class TestLoginPage(BaseClass):
    def test_tc_01(self):
            login_page = LoginPage(self.driver)
            with allure.step("Enter user name"):
                user_name = self.get_test_case_data('test_case_1', 'username')
            with allure.step("Enter password"):
                password = self.get_test_case_data('test_case_1', 'password')
            with allure.step("Press login"):
                login_page.login(user_name, password)
            product_page = ProductsPage(self.driver)
            title = login_page.get_text(product_page.title)
            test_case_data = self.get_test_case_data('test_case_1', 'expected_result')
            assert test_case_data == title

    def test_tc_02(self):
        login_page = LoginPage(self.driver)
        with allure.step("Enter invalid user name"):
            user_name = self.get_test_case_data('test_case_2', 'username')
        with allure.step("Enter password"):
            password = self.get_test_case_data('test_case_2', 'password')
        with allure.step("Press login"):
            login_page.login(user_name, password)
        error_message = login_page.get_text(login_page.error_label)
        test_case_data = self.get_test_case_data('test_case_2', 'expected_result')
        assert test_case_data in error_message



