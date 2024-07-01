import allure
import pytest
from pageObjects.cart_page import CartPage
from pageObjects.customer_information_page import InformationPage
from pageObjects.order_completion_page import OrderCompletionPage
from pageObjects.overview_page import OverViewPage
from pageObjects.products_page import ProductsPage
from tests_data.test_data import INFORMATION_PAGE, PRODUCTS, EXPECTED_RESULTS
from utils import add_multiple_products_to_cart
@pytest.mark.usefixtures("overview_setup", "log_on_failure")
class TestLoginPage():
    @allure.description("Verify user can buy a single item")
    @allure.title("Single Item Purchase Test")
    @allure.feature("Order Completion Tests")
    @allure.tag("Order Completion Tests")
    def test_tc_01(self):
        products_page = ProductsPage(self.driver)
        products_page.open_cart()
        cart_page = CartPage(self.driver)
        cart_page.checkout_items()
        information_Page = InformationPage(self.driver)
        information_Page.enter_information(INFORMATION_PAGE["first_name"], INFORMATION_PAGE["last_name"], INFORMATION_PAGE["postal_code"])
        overViewPage = OverViewPage(self.driver)
        overViewPage.click_element(overViewPage.finish)
        orderCompletion_Page = OrderCompletionPage(self.driver)
        order_confirmation_message = orderCompletion_Page.get_text(orderCompletion_Page.order_confirmation)
        orderCompletion_Page.click_element(OrderCompletionPage.return_back)
        assert order_confirmation_message == EXPECTED_RESULTS["order_validation"]

    @allure.description("Verify user can buy multiple items")
    @allure.title("Multiple Items Purchase Test")
    @allure.feature("Order Completion Tests")
    @allure.tag("Order Completion Tests")
    def test_tc_02(self):
        products_page = ProductsPage(self.driver)
        add_multiple_products_to_cart(PRODUCTS.keys(), products_page)
        products_page.open_cart()
        cart_page = CartPage(self.driver)
        cart_page.checkout_items()
        information_Page = InformationPage(self.driver)
        information_Page.enter_information(INFORMATION_PAGE["first_name"], INFORMATION_PAGE["last_name"], INFORMATION_PAGE["postal_code"])
        overViewPage = OverViewPage(self.driver)
        overViewPage.click_element(overViewPage.finish)
        orderCompletion_Page = OrderCompletionPage(self.driver)
        order_confirmation_message = orderCompletion_Page.get_text(orderCompletion_Page.order_confirmation)
        assert order_confirmation_message == EXPECTED_RESULTS["order_validation"]

    @allure.description("Verify user can buy multiple items")
    @allure.title("Multiple Items Purchase Test")
    @allure.feature("Order Completion Tests")
    @allure.tag("Order Completion Tests", )
    def test_tc_02(self):
        products_page = ProductsPage(self.driver)
        add_multiple_products_to_cart(PRODUCTS.keys(), products_page)
        products_page.open_cart()
        cart_page = CartPage(self.driver)
        cart_page.checkout_items()
        information_Page = InformationPage(self.driver)
        information_Page.enter_information(INFORMATION_PAGE["first_name"], INFORMATION_PAGE["last_name"], INFORMATION_PAGE["postal_code"])
        overViewPage = OverViewPage(self.driver)
        overViewPage.click_element(overViewPage.finish)
        orderCompletion_Page = OrderCompletionPage(self.driver)
        order_confirmation_message = orderCompletion_Page.get_text(orderCompletion_Page.order_confirmation)
        assert order_confirmation_message == EXPECTED_RESULTS["order_validation_fail_scenario"]

