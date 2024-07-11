import time
import logging
from tests_data.test_data import PRODUCTS


def highlight(element, driver, duration=0.5):
    """Highlights (blinks) a Selenium Webdriver element."""
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(duration)
    apply_style(original_style)


def add_multiple_products_to_cart(items_list, products_page):
    for item in items_list:
        products_page.add_to_cart(PRODUCTS[item])


def get_logger():
    logger = logging.getLogger('UI Automate testing')
    logger.setLevel(logging.INFO)  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

    # Create a file handler that overwrites the log file each time
    file_handler = logging.FileHandler("log_info.log", mode='w')
    file_handler.setLevel(logging.INFO)

    # Create a logging format
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    file_handler.setFormatter(formatter)

    if logger.hasHandlers():
        logger.handlers.clear()

    # Add the file handler to the logger
    logger.addHandler(file_handler)
    return logger