import allure
import pytest

from base_test import LoginBaseClass, GeneralBaseClass
from pageObjects.cart_page import CartPage
from pageObjects.customer_information_page import InformationPage
from pageObjects.login_page import LoginPage
from pageObjects.overview_page import OverViewPage
from pageObjects.products_page import ProductsPage
from tests_data.test_data import INVALID_LOGIN_CREDENTIALS, LOGIN_CREDENTIALS, EXPECTED_RESULTS, PRODUCTS, \
    INFORMATION_PAGE, ERROR_MESSAGES

@pytest.mark.usefixtures("customer_information_setup")
class TestCustomerInformationPage:
    @allure.description("Verify that user can't log in with empty first name")
    @allure.title("Invalid first name test")
    @allure.feature("Login tests")
    @allure.tag("Login tests")
    def test_tc_01(self):
        information_Page = InformationPage(self.driver)
        information_Page.enter_information("", INFORMATION_PAGE["last_name"], INFORMATION_PAGE["postal_code"])
        error_message = information_Page.get_error_message()
        assert ERROR_MESSAGES["empty_first_name"] in error_message

    @pytest.mark.usefixtures("customer_information_setup")
    @allure.description("Verify that user can't log in with empty last name")
    @allure.title("Invalid password test")
    @allure.feature("Login tests")
    @allure.tag("Login tests")
    def test_tc_02(self):
        information_Page = InformationPage(self.driver)
        information_Page.enter_information(INFORMATION_PAGE["first_name"], "", INFORMATION_PAGE["postal_code"])
        error_message = information_Page.get_error_message()
        assert ERROR_MESSAGES["empty_last_name"] in error_message
    @allure.description("Verify that user can't log in with empty Zip/Postal Code")
    @allure.title("Empty Zip/Postal Code test")
    @allure.feature("Login tests")
    @allure.tag("Login tests")
    def test_tc_03(self):
        information_Page = InformationPage(self.driver)
        information_Page.enter_information(INFORMATION_PAGE["first_name"], INFORMATION_PAGE["last_name"], "")
        error_message = information_Page.get_error_message()
        assert ERROR_MESSAGES["empty_postal_code"] in error_message
    @allure.description("Verify that user can't log in with empty of all fields (First Name, Last Name, Zip/Postal Code)")
    @allure.title("Empty fields test")
    @allure.feature("Login tests")
    @allure.tag("Login tests")
    def test_tc_04(self):
        information_Page = InformationPage(self.driver)
        information_Page.enter_information("", "", "")
        error_message = information_Page.get_error_message()
        assert ERROR_MESSAGES["empty_all_fields"] in error_message
    @allure.description("Verify that user can continue to overview page with valid First Name, Last Name and Zip/Postal Code")
    @allure.title("Continue to Overview page")
    @allure.feature("Login tests")
    @allure.tag("Login tests")
    def test_tc_05(self):
        information_Page = InformationPage(self.driver)
        information_Page.enter_information(INFORMATION_PAGE["first_name"], INFORMATION_PAGE["last_name"], INFORMATION_PAGE["postal_code"])
        overViewPage = OverViewPage(self.driver)
        is_displayed = overViewPage.is_displayed(OverViewPage.title)
        assert is_displayed