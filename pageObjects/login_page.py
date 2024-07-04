import os
import sys
import allure
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage
class LoginPage(BasePage):

    user = (By.CSS_SELECTOR, "#user-name")
    password = (By.CSS_SELECTOR, "#password")
    login_button = (By.CSS_SELECTOR, "#login-button")
    error_label = (By.CSS_SELECTOR, "[data-test='error']")


    def login(self, username, password):
        with allure.step("Insert username"):
            self.fill_text(self.user, username)
        with allure.step("Insert password"):
            self.fill_text(self.password, password)
        with allure.step("press login"):
            self.click_element(self.login_button)










