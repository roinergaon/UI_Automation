import os
import sys
import time

from utils import highlight

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_all_elements(self, locator):
        return self.driver.find_elements(*locator)

    def fill_text(self, locator, text):
        element = self.driver.find_element(*locator)
        highlight(element, self.driver)
        element.click()
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        element = self.driver.find_element(*locator)
        highlight(element, self.driver)
        element.click()

    def get_text(self, locator):
        element = self.driver.find_element(*locator)
        highlight(element, self.driver)
        return element.text

    def is_displayed(self, locator):
        element = self.driver.find_element(*locator)
        highlight(element, self.driver)
        return element.is_displayed()
    def clear_field(self, locator):
        element = self.driver.find_element(*locator)
        highlight(element, self.driver)
        element.clear()

