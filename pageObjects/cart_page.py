from selenium.webdriver.common.by import By
from pageObjects.menu_page import MenuPage

class CartPage(MenuPage):
    def __init__(self, driver):
        super().__init__(driver)

    cart_lable =  (By.CSS_SELECTOR, ".cart_item_label")
    product_name = (By.CSS_SELECTOR, ".inventory_item_name")

    def is_product_in_cart(self,name):
        elements = self.driver.find_elements(*self.cart_lable)
        for el in elements:
            product__name = el.find_element(*self.product_name).text
            if product__name == name:
                return True
            else:
                return False
