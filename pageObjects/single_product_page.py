from selenium.webdriver.common.by import By

from pageObjects.menu_page import MenuPage

class SingleProductPage(MenuPage):
    def __init__(self, driver):
        super().__init__(driver)

    product_name = (By.CSS_SELECTOR, "[class = 'inventory_details_name large_size']")
    cart_addition = (By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory")
    back = (By.CSS_SELECTOR, ".btn.btn_secondary.back.btn_large.inventory_details_back_button")
    def get_item_name(self):
        return self.get_text(self.product_name)

    def add_to_cart(self):
        self.click_element(self.cart_addition)
    def back(self):
        self.click_element(self.back)








