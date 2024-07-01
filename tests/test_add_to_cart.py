import allure
import pytest
from pageObjects.cart_page import CartPage
from pageObjects.products_page import ProductsPage
from tests_data.test_data import PRODUCTS
@pytest.mark.usefixtures("general_setup")
class TestAddProductToCart():
    @allure.description("Test adding a single item to the cart")
    @allure.title("Add Single Item to Cart Test")
    @allure.feature("Cart Tests")
    @allure.tag("Cart Tests")
    def test_tc_01(self):
        products_page = ProductsPage(self.driver)
        products_page.add_to_cart(PRODUCTS["backpack"])
        products_page.open_cart()
        cart_page = CartPage(self.driver)
        is_exists = cart_page.is_product_in_cart(PRODUCTS["backpack"])
        cart_page.remove_product(PRODUCTS["backpack"])
        cart_page.return_to_products_list()
        assert is_exists
    @allure.description("Test removing a single product from the cart")
    @allure.title("Remove Single Item from Cart Test")
    @allure.feature("Cart Tests")
    @allure.tag("Cart Tests")
    def test_tc_02(self):
        products_page = ProductsPage(self.driver)
        products_page.add_to_cart(PRODUCTS["backpack"])
        products_page.open_cart()
        cart_page = CartPage(self.driver)
        cart_page.remove_product(PRODUCTS["backpack"])
        is_found = cart_page.is_product_in_cart(PRODUCTS["backpack"])
        cart_page.return_to_products_list()
        assert not is_found, f'{PRODUCTS["backpack"]} still inside the cart_page'
    @allure.description("Test adding multiple products to the cart")
    @allure.title("Add Multiple Products to Cart Test")
    @allure.feature("Cart Tests")
    @allure.tag("Cart Tests")
    @pytest.mark.parametrize("product_name", PRODUCTS.keys())
    def test_tc_03(self, product_name):
        products_page = ProductsPage(self.driver)
        products_page.add_to_cart(PRODUCTS[product_name])
        products_page.open_cart()
        cart_page = CartPage(self.driver)
        assert cart_page.is_product_in_cart(PRODUCTS[product_name]), f"{PRODUCTS[product_name]} is not available in the cart"
        cart_page.return_to_products_list()
    @allure.description("Test removing multiple items from the cart")
    @allure.title("Remove Multiple Items from Cart Test")
    @allure.feature("Cart Tests")
    @allure.tag("Cart Tests")
    @pytest.mark.parametrize("product_name", PRODUCTS.keys())
    def test_tc_04(self, product_name):
        products_page = ProductsPage(self.driver)
        products_page.open_cart()
        cart_page = CartPage(self.driver)
        cart_page.remove_product(PRODUCTS[product_name])
        is_found  = cart_page.is_product_in_cart(PRODUCTS[product_name])
        cart_page.return_to_products_list()
        assert not is_found, f"{PRODUCTS[product_name]} still inside the cart_page"
    @allure.description("Test continue shopping functionality")
    @allure.title("Continue Shopping Test")
    @allure.feature("Cart Tests")
    @allure.tag("Cart Tests")
    def test_tc_05(self):
        products_page = ProductsPage(self.driver)
        products_page.add_to_cart(PRODUCTS["backpack"])
        products_page.open_cart()
        cart = CartPage(self.driver)
        cart.return_to_products_page()
        is_title_displayed = products_page.is_displayed(products_page.title)
        assert is_title_displayed