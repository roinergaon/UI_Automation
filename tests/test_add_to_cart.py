import allure

from pageObjects.cart_page import CartPage
from pageObjects.login_page import LoginPage
from pageObjects.products_page import ProductsPage
from utils.base_test import BaseClass


class TestAddProductToCart(BaseClass):
    def test_add_single_product_to_car(self):
        login_page = LoginPage(self.driver)
        with allure.step("Press user name and password and prees login"):
            login_page.login("standard_user", "secret_sauce")
        products_page = ProductsPage(self.driver)
        products_page.add_to_cart("Sauce Labs Backpack")
        products_page.open_cart()
        cart = CartPage(self.driver)
        value = cart.is_product_in_cart("Sauce Labs Backpack")
        assert value == True

    def test_add_multiple_products_to_cart(self):
        pass
    def test_add_product_to_cart_updates_cart_total(self):
        pass
    def test_add_product_to_cart_and_verify_cart_contents(self):
        pass
    def test_add_product_to_cart_and_check_cart_summary(self):
        pass


