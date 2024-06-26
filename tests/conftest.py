import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def login_setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture(scope="function")
def general_setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    request.cls.driver = driver
    yield
    driver.close()

