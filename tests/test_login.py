import allure
import pytest
from pageObjects.login_page import LoginPage
from pageObjects.products_page import ProductsPage
from tests_data.test_data import INVALID_LOGIN_CREDENTIALS, LOGIN_CREDENTIALS, EXPECTED_RESULTS
@pytest.mark.usefixtures("login_setup", "log_on_failure")
class TestLoginPage():
    @allure.description("Verify that user can't log in with invalid username")
    @allure.title("Invalid Username Test")
    @allure.feature("Login Tests")
    @allure.tag("Login Tests")
    def test_tc_01(self):
        login_page = LoginPage(self.driver)
        login_page.login(INVALID_LOGIN_CREDENTIALS["invalid_username"], LOGIN_CREDENTIALS["password"])
        error_message = login_page.get_text(login_page.error_label)
        assert EXPECTED_RESULTS[ "invalid_username_valid_password"] in error_message

    @allure.description("Verify that user can't log in with invalid password")
    @allure.title("Invalid Password Test")
    @allure.feature("Login Tests")
    @allure.tag("Login Tests")
    def test_tc_02(self):
        login_page = LoginPage(self.driver)
        login_page.login(LOGIN_CREDENTIALS["username"], INVALID_LOGIN_CREDENTIALS["invalid_password"])
        error_message = login_page.get_text(login_page.error_label)
        assert EXPECTED_RESULTS["invalid_username_valid_password"] in error_message
    @allure.description("Verify that user can't log in with empty password field")
    @allure.title("Empty Password Test")
    @allure.feature("Login Tests")
    @allure.tag("Login Tests")
    def test_tc_03(self):
        login_page = LoginPage(self.driver)
        login_page.login(LOGIN_CREDENTIALS["username"], "")
        error_message = login_page.get_text(login_page.error_label)
        assert EXPECTED_RESULTS["empty_password"] in error_message
    @allure.description("Verify that user can't log in with empty username and empty password fields")
    @allure.title("Empty Username and Password Test")
    @allure.feature("Login Tests")
    @allure.tag("Login Tests")
    def test_tc_04(self):
        login_page = LoginPage(self.driver)
        login_page.login("", "")
        error_message = login_page.get_text(login_page.error_label)
        assert EXPECTED_RESULTS["empty_username_password"] in error_message

    @allure.description("Verify that user can't log in with empty username and empty password fields - failed scenario")
    @allure.title("Empty Username and Password Test")
    @allure.feature("Login Tests")
    @allure.tag("Login Tests")
    def test_tc_05(self):
        login_page = LoginPage(self.driver)
        login_page.login("", "")
        error_message = login_page.get_text(login_page.error_label)
        assert EXPECTED_RESULTS["order_validation_fail_scenario"] in error_message
    @allure.description("Verify that user can log in with valid username and password")
    @allure.title("Valid Username and Password Test")
    @allure.feature("Login Tests")
    @allure.tag("Login Tests")
    def test_tc_06(self):
        login_page = LoginPage(self.driver)
        login_page.login(LOGIN_CREDENTIALS ["username"], LOGIN_CREDENTIALS ["password"])
        product_pages = ProductsPage(self.driver)
        assert product_pages.is_displayed(product_pages.title)
    @allure.description("Log out")
    @allure.title("Log Out Test")
    @allure.feature("Login Tests")
    @allure.tag("Login Tests")
    def test_tc_07(self):
        products_page = ProductsPage(self.driver)
        products_page.click_log_out()
        login_page = LoginPage(self.driver)
        is_displayed = login_page.is_displayed(login_page.login_button)
        assert is_displayed


