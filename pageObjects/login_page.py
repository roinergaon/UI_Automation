import os
import sys
import allure

import utils

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage
class LoginPage(BasePage):

    user = (By.CSS_SELECTOR, "#user-name")
    password = (By.CSS_SELECTOR, "#password")
    login_button = (By.CSS_SELECTOR, "#login-button")
    error_label = (By.CSS_SELECTOR, "[data-test='error']")


    def login(self, username, password):
        self.logger.info(f"Insert username: {username}")
        with allure.step("Insert username"):
            self.fill_text(self.user, username)
        self.logger.info(f"Insert password: {password}")
        with allure.step("Insert password"):
            self.fill_text(self.password, password)
        with allure.step("press login"):
            self.click_element(self.login_button)










