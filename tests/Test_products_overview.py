import allure
import pytest
from pageObjects.cart_page import CartPage
from pageObjects.customer_information_page import InformationPage
from pageObjects.order_completion_page import OrderCompletionPage
from pageObjects.overview_page import OverViewPage
from pageObjects.products_page import ProductsPage
from tests_data.test_data import EXPECTED_RESULTS, INFORMATION_PAGE

@pytest.mark.usefixtures("overview_setup")
class TestProductOverviewPage():
    @allure.description("Verify that user can cancel order and return to the home page")
    @allure.title("Cancel Order and Return to Home Page Test")
    @allure.feature("Products Overview Tests")
    @allure.tag("Products Overview Tests")
    def test_tc_01(self):
        overViewPage = OverViewPage(self.driver)
        overViewPage.click_element(overViewPage.cancel)
        products_page = ProductsPage(self.driver)
        title_name = products_page.get_text(products_page.title)
        assert title_name == EXPECTED_RESULTS["products_page_validation"]

    @allure.description("Verify that user can continue with purchase")
    @allure.title("Continue with Purchase Test")
    @allure.feature("Products Overview Tests")
    @allure.tag("Products Overview Tests")
    def test_tc_02(self):
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
        assert order_confirmation_message == EXPECTED_RESULTS["order_validation"]



