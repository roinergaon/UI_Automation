import allure
import pytest
from pageObjects.cart_page import CartPage
from pageObjects.customer_information_page import InformationPage
from pageObjects.overview_page import OverViewPage
from tests_data.test_data import INFORMATION_PAGE, ERROR_MESSAGES, EXPECTED_RESULTS


@pytest.mark.usefixtures("customer_information_setup", "log_on_failure")
class TestCustomerInformationPage:
    @allure.description("Verify error message for empty first name")
    @allure.title("Empty First Name Test")
    @allure.feature("Customer Information Tests")
    @allure.tag("Customer Information Tests")
    def test_tc_01(self):
        information_Page = InformationPage(self.driver)
        information_Page.enter_information("", INFORMATION_PAGE["last_name"], INFORMATION_PAGE["postal_code"])
        error_message = information_Page.get_error_message()
        assert ERROR_MESSAGES["empty_first_name"] in error_message

    @allure.description("Verify error message for empty last name")
    @allure.title("Empty Last Name Test")
    @allure.feature("Customer Information Tests")
    @allure.tag("Customer Information Tests")
    def test_tc_02(self):
        information_Page = InformationPage(self.driver)
        information_Page.enter_information(INFORMATION_PAGE["first_name"], "", INFORMATION_PAGE["postal_code"])
        error_message = information_Page.get_error_message()
        assert ERROR_MESSAGES["empty_last_name"] in error_message

    @allure.description("Verify error message for empty postal code")
    @allure.title("Empty Postal Code Test")
    @allure.feature("Customer Information Tests")
    @allure.tag("Customer Information Tests")
    def test_tc_03(self):
        information_Page = InformationPage(self.driver)
        information_Page.enter_information(INFORMATION_PAGE["first_name"], INFORMATION_PAGE["last_name"], "")
        error_message = information_Page.get_error_message()
        assert ERROR_MESSAGES["empty_postal_code"] in error_message

    @allure.description("Verify error message for all empty fields")
    @allure.title("All Empty Fields Test")
    @allure.feature("Customer Information Tests")
    @allure.tag("Customer Information Tests")
    def test_tc_04(self):
        information_Page = InformationPage(self.driver)
        information_Page.enter_information("", "", "")
        error_message = information_Page.get_error_message()
        assert ERROR_MESSAGES["empty_all_fields"] in error_message

    @allure.description("Verify successful entry of customer information")
    @allure.title("Successful Customer Information Entry Test")
    @allure.feature("Customer Information Tests")
    @allure.tag("Customer Information Tests")
    def test_tc_05(self):
        information_Page = InformationPage(self.driver)
        information_Page.enter_information(INFORMATION_PAGE["first_name"], INFORMATION_PAGE["last_name"],
                                           INFORMATION_PAGE["postal_code"])
        overViewPage = OverViewPage(self.driver)
        is_displayed = overViewPage.is_displayed(OverViewPage.title)
        assert is_displayed

    @allure.description("Verify successful cancellation of purchase")
    @allure.title("Cancel Purchase Test")
    @allure.feature("Customer Information Tests")
    @allure.tag("Customer Information Tests")
    def test_tc_06(self):
        information_Page = InformationPage(self.driver)
        information_Page.click_element(information_Page.cancel)
        cart_page = CartPage(self.driver)
        text = cart_page.get_text(cart_page.title)
        assert text == EXPECTED_RESULTS["cart_page_validation"]
