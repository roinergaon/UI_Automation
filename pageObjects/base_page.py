class BasePage:
    def fillText(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)