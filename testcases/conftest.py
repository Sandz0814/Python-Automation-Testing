import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Edge()
    driver.get("https://demoqa.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()

    request.cls.driver = driver
    yield driver


