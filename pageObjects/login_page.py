from selenium.webdriver.common.by import By

from pageObjects.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    user = (By.CSS_SELECTOR, "#user-name")
    password = (By.CSS_SELECTOR, "#password")
    login = (By.CSS_SELECTOR, "#login-button")
    error_label = (By.CSS_SELECTOR, "[data-test='error']")

    def login(self, username, password):
        self.fillText(LoginPage.user, username)









