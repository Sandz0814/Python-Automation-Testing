import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")
    # driver.execute_script("document.body.style.zoom='0.5'")
    driver.implicitly_wait(10)
    driver.maximize_window()
    # driver.execute_script("document.body.style.zoom='40%'")
    request.cls.driver = driver
    yield driver
