from selenium.webdriver.common.by import By
from pageObjects.menu_page import MenuPage
from utils import highlight


class CartPage(MenuPage):
    def __init__(self, driver):
        super().__init__(driver)

    title =  (By.CSS_SELECTOR, "[data-test='title']")
    cart_lable =  (By.CSS_SELECTOR, ".cart_item_label")
    product_name = (By.CSS_SELECTOR, ".inventory_item_name")
    continue_shopping = (By.CSS_SELECTOR, "#continue-shopping")
    remove_product_from_cart = (By.CSS_SELECTOR, "[class='btn btn_secondary btn_small cart_button']")
    checkout = (By.CSS_SELECTOR, "#checkout")

    def is_product_in_cart(self,name):
        elements = self.driver.find_elements(*self.cart_lable)
        for el in elements:
            product__name = el.find_element(*self.product_name).text
            if product__name == name:
                highlight(el, self.driver)
                return True
        return False

    def remove_product(self,name):
        elements = self.driver.find_elements(*self.cart_lable)
        for el in elements:
            product__name = el.find_element(*self.product_name).text
            if product__name == name:
                highlight(el, self.driver)
                self.click_element(self.remove_product_from_cart)
                break

    def return_to_products_page(self):
        self.click_element(self.continue_shopping)

    def checkout_items(self):
        self.click_element(self.checkout)

