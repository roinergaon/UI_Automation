import os
import sys
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from config import SAUCEDEMO_URL
from pageObjects.cart_page import CartPage
from pageObjects.customer_information_page import InformationPage
from pageObjects.login_page import LoginPage
from pageObjects.products_page import ProductsPage
from tests_data.test_data import LOGIN_CREDENTIALS, PRODUCTS, INFORMATION_PAGE
import pytest
@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
@pytest.fixture(scope="class")
def login_setup(request):
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--force-device-scale-factor=1.5")
    driver=webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(SAUCEDEMO_URL)
    request.cls.driver = driver
    yield
    driver.close()
@pytest.fixture(scope="class")
def general_setup(request):
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--force-device-scale-factor=1.5")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(SAUCEDEMO_URL)
    with allure.step("Press user name and password and press login"):
        login_page = LoginPage(driver)
        login_page.login(LOGIN_CREDENTIALS["username"], LOGIN_CREDENTIALS["password"])

    request.cls.driver = driver
    yield
    driver.close()
@pytest.fixture(scope="function")
def customer_information_setup(request):
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--force-device-scale-factor=1.5")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(SAUCEDEMO_URL)
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
@pytest.fixture(scope="class")
def overview_setup(request):
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--force-device-scale-factor=1.5")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(SAUCEDEMO_URL)
    with allure.step("Press user name and password and press login"):
        login_page = LoginPage(driver)
        login_page.login(LOGIN_CREDENTIALS["username"], LOGIN_CREDENTIALS["password"])
    products_page = ProductsPage(driver)
    products_page.add_to_cart(PRODUCTS["backpack"])
    products_page.open_cart()
    cart_page = CartPage(driver)
    cart_page.checkout_items()
    information_Page = InformationPage(driver)
    information_Page.enter_information(INFORMATION_PAGE["first_name"], INFORMATION_PAGE["last_name"],INFORMATION_PAGE["postal_code"])
    request.cls.driver = driver
    yield
    driver.close()