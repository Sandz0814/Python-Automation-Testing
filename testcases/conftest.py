import time
import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    # driver.execute_script("document.body.style.zoom='0.5'")
    # time.sleep(20)

    request.cls.driver = driver
    yield driver


