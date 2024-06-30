from selenium.webdriver.common.by import By
from pageObjects.menu_page import MenuPage

class InformationPage(MenuPage):
    def __init__(self, driver):
        super().__init__(driver)


    first_name = (By.ID, "first-name")
    last_name = (By.CSS_SELECTOR, "[data-test='lastName']")
    zip_postal_code = (By.CSS_SELECTOR, "[data-test='postalCode']")
    continue_purchase = (By.CSS_SELECTOR, "[type='submit']")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")
    cancel = (By.CSS_SELECTOR, "[class='btn btn_secondary back btn_medium cart_cancel_link']")

    def continue_with_purchase(self):
        self.click_element(self.continue_purchase)
    def enter_information(self, first_name, last_name, zip_postal_code):
        self.fill_text(self.first_name, first_name)
        self.fill_text(self.last_name, last_name)
        self.fill_text(self.zip_postal_code, zip_postal_code)
        self.click_element(self.continue_purchase)

    def get_error_message(self):
        return self.get_text(self.error_message)



