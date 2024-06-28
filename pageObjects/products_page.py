
from selenium.webdriver.common.by import By
from pageObjects.menu_page import MenuPage
from utils import highlight


class ProductsPage(MenuPage):
    def __init__(self, driver):
        super().__init__(driver)

    title = (By.CSS_SELECTOR, "[class='title']")
    products_title = (By.CSS_SELECTOR, ".inventory_item_name")
    products_label = (By.CSS_SELECTOR, ".inventory_item")
    products_price = (By.CSS_SELECTOR, ".inventory_item_price")
    cart = (By.CSS_SELECTOR, "#shopping_cart_container")
    add_product_to_cart = (By.CSS_SELECTOR, "[class='btn btn_primary btn_small btn_inventory ']")


    def choose_product(self, name):
        elements = self.find_all_elements(*self.products_title, name)
        for el in elements:
            if el.text == name:
                el.click()
                break
    def open_cart(self):
        self.click_element(self.cart)

    def get_all_prices(self):
        all_prices = []
        elements = self.find_all_elements(self.products_price)
        for el in elements:
            price = el.text
            price_without_symbol = price[1:]
            price_float = float(price_without_symbol)
            all_prices = all_prices.append(price_float)
            return all_prices

    def validated_sorted_prices(self, prices):
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                return False
    def save_product_price(self, name):
        elements = self.find_all_elements(self.products_label)
        for el in elements:
            if el.text == name:
                price = self.get_text(self.products_price)
                price_without_symbol = price[1:]
                price_float = float(price_without_symbol)
                return price_float

    def add_to_cart(self, name):
        elements = self.find_all_elements(self.products_label)
        for el in elements:
            product_name = el.find_element(*self.products_title).text
            if product_name == name:
                element = el.find_element(*self.add_product_to_cart)
                highlight(element, self.driver)
                element.click()
                break








