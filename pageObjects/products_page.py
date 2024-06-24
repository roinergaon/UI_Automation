
from selenium.webdriver.common.by import By

from pageObjects.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    title = (By.CSS_SELECTOR, "[class='title']")
    products_title = (By.CSS_SELECTOR, ".inventory_item_name")
    products_label = (By.CSS_SELECTOR, ".inventory_item")
    cart = (By.CSS_SELECTOR, "#shopping_cart_container")


    def choose_product(self, locator, name):
        elements = self.find_all_elements(locator, name)
        for el in elements:
            if el.text == name:
                el.click()
                break


