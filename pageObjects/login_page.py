import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from selenium.webdriver.common.by import By

from pageObjects.base_page import BasePage
from pageObjects.products_page import ProductsPage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    user = (By.CSS_SELECTOR, "#user-name")
    password = (By.CSS_SELECTOR, "#password")
    login_button = (By.CSS_SELECTOR, "#login-button")
    error_label = (By.CSS_SELECTOR, "[data-test='error']")

    def login(self, username, password):
        self.fill_text(self.user, username)
        self.fill_text(self.password, password)
        self.click_element(self.login_button)










