import allure
import pytest
from selenium import webdriver

from pageObjects.cart_page import CartPage
from pageObjects.login_page import LoginPage
from pageObjects.products_page import ProductsPage
from tests_data.test_data import LOGIN_CREDENTIALS, PRODUCTS


@pytest.fixture(scope="class")
def login_setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--force-device-scale-factor=1.5")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture(scope="class")
def general_setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--force-device-scale-factor=1.5")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    with allure.step("Press user name and password and press login"):
        login_page = LoginPage(driver)
        login_page.login(LOGIN_CREDENTIALS["username"], LOGIN_CREDENTIALS["password"])

    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture(scope="function")
def customer_information_setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--force-device-scale-factor=1.5")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    with allure.step("Press user name and password and press login"):
        login_page = LoginPage(driver)
        login_page.login(LOGIN_CREDENTIALS["username"], LOGIN_CREDENTIALS["password"])
    products_page = ProductsPage(driver)
    products_page.add_to_cart(PRODUCTS["backpack"])
    products_page.open_cart()
    cart_page = CartPage(driver)
    cart_page.checkout_items()
    request.cls.driver = driver
    yield
    driver.close()



