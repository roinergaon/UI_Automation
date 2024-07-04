from selenium.webdriver.common.by import By

from pageObjects.menu_page import MenuPage


class OverViewPage(MenuPage):
    def __init__(self, driver):
        super().__init__(driver)


    title = (By.CSS_SELECTOR, "[class='title']")
    cancel = (By.CSS_SELECTOR, "[class='btn btn_secondary back btn_medium cart_cancel_link']")
    finish = (By.CSS_SELECTOR, "[class='btn btn_action btn_medium cart_button']")



