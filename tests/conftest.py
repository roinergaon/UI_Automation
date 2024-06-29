import allure
import pytest
from selenium import webdriver

from pageObjects.login_page import LoginPage
from tests_data.test_data import LOGIN_CREDENTIALS


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

