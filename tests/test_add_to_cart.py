import allure

from pageObjects.cart_page import CartPage
from pageObjects.login_page import LoginPage
from pageObjects.products_page import ProductsPage
from utils.base_test import GeneralBaseClass


class TestAddProductToCart(GeneralBaseClass):
    def test_add_single_product_to_car(self):
        login_page = LoginPage(self.driver)
        with allure.step("Press user name and password and press login"):
            login_page.login("standard_user", "secret_sauce")
        products_page = ProductsPage(self.driver)
        products_page.add_to_cart("Sauce Labs Backpack")
        products_page.open_cart()
        cart = CartPage(self.driver)
        is_exists = cart.is_product_in_cart("Sauce Labs Backpack")
        #cart.remove_product("Sauce Labs Backpack")
        #cart.return_to_products_page()
        assert is_exists == True

    # def test_remove_from_cart(self):

    def test_add_multiple_products_to_cart(self):
        login_page = LoginPage(self.driver)
        with allure.step("Press user name and password and press login"):
            login_page.login("standard_user", "secret_sauce")
        products_page = ProductsPage(self.driver)
        products_page.add_to_cart("Sauce Labs Bike Light")
        products_page.add_to_cart("Sauce Labs Backpack")
        products_page.open_cart()
        cart = CartPage(self.driver)
        Sauce_Labs_Bike_Light_product = cart.is_product_in_cart("Sauce Labs Bike Light")
        Sauce_Labs_Backpack_product = cart.is_product_in_cart("Sauce Labs Backpack")
        #cart.return_to_products_page()
        #cart.remove_product("Sauce Labs Backpack")
        #cart.remove_product("Sauce Labs Bike Light")
        #cart.return_to_products_page()
        assert Sauce_Labs_Bike_Light_product == True
        assert Sauce_Labs_Backpack_product == True

    def test_add_product_to_cart_updates_cart_total(self):
        pass

    def test_add_product_to_cart_and_verify_cart_contents(self):
        pass

    def test_add_product_to_cart_and_check_cart_summary(self):
        pass
