import time

from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage


class MenuPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    all_items = (By.CSS_SELECTOR, "#inventory_sidebar_link")
    log_out = (By.CSS_SELECTOR, "#logout_sidebar_link")
    expand_menu = (By.CSS_SELECTOR, "#react-burger-menu-btn")

    def return_to_products_list(self):
        self.click_element(self.expand_menu)
        time.sleep(1)
        self.click_element(self.all_items)

    def click_log_out(self):
        self.click_element(self.expand_menu)
        time.sleep(1)
        self.click_element(self.log_out)









