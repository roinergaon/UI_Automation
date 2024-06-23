
from selenium.webdriver.common.by import By

from pageObjects.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #self.driver = driver

    title = (By.CSS_SELECTOR, "[class='title']")
