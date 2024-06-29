from selenium.webdriver.common.by import By

from pageObjects.menu_page import MenuPage


class OverViewPage(MenuPage):
    def __init__(self, driver):
        super().__init__(driver)

    title = (By.CSS_SELECTOR, "[class='title']")



