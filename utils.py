import time


def highlight(element, driver, duration=0.5):
    """Highlights (blinks) a Selenium Webdriver element."""
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(duration)
    apply_style(original_style)