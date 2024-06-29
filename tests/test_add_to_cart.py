import allure
import pytest

from base_test import GeneralBaseClass
from pageObjects import cart_page
from pageObjects.cart_page import CartPage
from pageObjects.login_page import LoginPage
from pageObjects.menu_page import MenuPage
from pageObjects.products_page import ProductsPage
from tests_data.test_data import PRODUCTS


class TestAddProductToCart(GeneralBaseClass):
    def test_add_single_product_to_cart(self):
        login_page = LoginPage(self.driver)
        products_page = ProductsPage(self.driver)
        products_page.add_to_cart("Sauce Labs Backpack")
        products_page.open_cart()
        cart_page = CartPage(self.driver)
        is_exists = cart_page.is_product_in_cart(PRODUCTS["backpack"])
        cart_page.remove_product(PRODUCTS["backpack"])
        cart_page.return_to_products_list()
        assert is_exists

    # def test_remove_from_cart(self):
    @pytest.mark.parametrize("product_name", PRODUCTS.keys())
    def test_add_multiple_products_to_cart(self, product_name):
        products_page = ProductsPage(self.driver)
        products_page.add_to_cart(PRODUCTS[product_name])
        products_page.open_cart()
        cart_page = CartPage(self.driver)
        assert cart_page.is_product_in_cart(PRODUCTS[product_name]), f"{PRODUCTS[product_name]} is not available in the cart"
        cart_page.return_to_products_list()

    @pytest.mark.parametrize("product_name", PRODUCTS.keys())
    def test_remove_multiple_products_from_cart(self, product_name):
        products_page = ProductsPage(self.driver)
        products_page.open_cart()
        cart_page = CartPage(self.driver)
        cart_page.remove_product(PRODUCTS[product_name])
        is_found  = cart_page.is_product_in_cart(PRODUCTS[product_name])
        cart_page.return_to_products_list()

        assert not is_found, f"{PRODUCTS[product_name]} still inside the cart_page"
        pass


    # def test_continue_shopping(self):
    #     login_page = LoginPage(self.driver)
    #     products_page = ProductsPage(self.driver)
    #     products_page.add_to_cart("Sauce Labs Bike Light")
    #     products_page.open_cart()
    #     cart = CartPage(self.driver)
    #     cart.return_to_products_page()
    #     is_title_displayed = products_page.is_displayed(products_page.title)
    #     assert is_title_displayed
    #
    # def test_remove_item_from_cart(self):
    #     login_page = LoginPage(self.driver)
    #     products_page = ProductsPage(self.driver)
    #     products_page.add_to_cart("Sauce Labs Backpack")
    #     products_page.open_cart()
    #     cart = CartPage(self.driver)
    #     cart.remove_product("Sauce Labs Backpack")
    #     is_item_in_cart = cart.is_product_in_cart("Sauce Labs Backpack")
    #     cart.return_to_products_page()
    #     assert not is_item_in_cart, "item still found in the cart"
    #
    #     # cart.return_to_products_page()
    #
    # def test_add_product_to_cart_updates_cart_total(self):
    #     pass
    #
    # def test_add_product_to_cart_and_verify_cart_contents(self):
    #     pass
    #
    # def test_add_product_to_cart_and_check_cart_summary(self):
    #     pass
