from selenium.webdriver.common.by import By

from pageObjects.menu_page import MenuPage

class SingleProductPage(MenuPage):
    def __init__(self, driver):
        super().__init__(driver)

    product_name = (By.CSS_SELECTOR, "[class = 'inventory_details_name large_size']")
    cart_addition = (By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory")
    back = (By.CSS_SELECTOR, ".btn.btn_secondary.back.btn_large.inventory_details_back_button")
    remove = (By.CSS_SELECTOR, "#remove")




