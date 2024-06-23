import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def fill_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def get_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text
