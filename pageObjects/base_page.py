import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_all_elements(self, locator):
        return self.driver.find_elements(*locator)

    def fill_text(self, locator, text):
        element = self.find_element(locator)
        element.click()
        self.clear_field(self, locator)
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    def is_displayed(self, locator):
        element = self.find_element(locator)
        return element.is_displayed()
    def clear_field(self, locator):
        element = self.find_element(locator)
        element.clear()

