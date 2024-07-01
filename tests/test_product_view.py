import allure
import pytest
from pageObjects.products_page import ProductsPage
from pageObjects.single_product_page import SingleProductPage
from tests_data.test_data import PRODUCTS
@pytest.mark.usefixtures("general_setup")
class TestProductView:
    @allure.description("Verify that user can open and overview a single item")
    @allure.title("Single Product Overview Test")
    @allure.feature("Single Product Overview Tests")
    @allure.tag("Single Product Overview Tests")
    def test_tc_01(self):
        products_page = ProductsPage(self.driver)
        products_page.add_to_cart(PRODUCTS["backpack"])
        products_page.choose_product(PRODUCTS["backpack"])
        singleProduct_Page = SingleProductPage(self.driver)
        product_name = singleProduct_Page.get_text(SingleProductPage.product_name)
        assert product_name == (PRODUCTS["backpack"])

    @allure.description("Verify that user can remove a single item")
    @allure.title("Remove Single Item Test")
    @allure.feature("Single Product Overview Tests")
    @allure.tag("Single Product Overview Tests")
    def test_tc_02(self):
        singleProduct_Page = SingleProductPage(self.driver)
        assert singleProduct_Page.is_displayed(SingleProductPage.remove)






