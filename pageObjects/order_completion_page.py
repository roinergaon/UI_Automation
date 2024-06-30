from selenium.webdriver.common.by import By

from pageObjects.menu_page import MenuPage


class OrderCompletionPage(MenuPage):
    def __init__(self, driver):
        super().__init__(driver)

    title = (By.CSS_SELECTOR, "[class='title']")
    order_confirmation = (By.CSS_SELECTOR, "[class='complete-header']")
    return_back = (By.CSS_SELECTOR, "[class='btn btn_primary btn_small']")

