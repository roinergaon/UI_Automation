
from selenium.webdriver.common.by import By
from pageObjects.menu_page import MenuPage

class ProductsPage(MenuPage):
    def __init__(self, driver):
        super().__init__(driver)

    title = (By.CSS_SELECTOR, "[class='title']")
    products_title = (By.CSS_SELECTOR, ".inventory_item_name")
    products_label = (By.CSS_SELECTOR, ".inventory_item")
    products_price = (By.CSS_SELECTOR, ".inventory_item_price")
    cart = (By.CSS_SELECTOR, "#shopping_cart_container")



    def choose_product(self, name):
        elements = self.find_all_elements(*self.products_title, name)
        for el in elements:
            if el.text == name:
                el.click()
                break
    def open_cart(self):
        self.click_element(*self.cart)

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







