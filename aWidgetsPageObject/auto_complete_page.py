import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tools.function import BaseDriver


class AutoComplete(BaseDriver):

    auto_complete_module = "//span[normalize-space()='Auto Complete']"
    header = "//body[1]/div[2]/div[1]/div[1]/div[1]"
    multiple_input = "autoCompleteMultipleInput"
    single_input = "//input[@id='autoCompleteSingleInput']"

    def __init__(self, driver):
        self.driver = driver

    def test_open_module(self):
        self.find(self.auto_complete_module).click()

    def test_header(self):
        headers = self.find(self.header).text
        if "Auto Complete" not in headers:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url_widget + "Auto complete headers.png")

    def test_multiple_color_input(self):
        # Wait for the page to load
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, self.multiple_input)))

        # Locate the autocomplete input field by its ID
        autocomplete_input = self.driver.find_element(By.ID, self.multiple_input)

        # Enter a value into the input field
        autocomplete_input.send_keys("Gre")
        time.sleep(1)
        autocomplete_input.send_keys(Keys.ENTER)
        autocomplete_input.send_keys("Blu")
        time.sleep(1)
        autocomplete_input.send_keys(Keys.ENTER)
        autocomplete_input.send_keys("Yel")
        time.sleep(1)
        autocomplete_input.send_keys(Keys.ENTER)
        time.sleep(2)
        autocomplete_input.send_keys(Keys.BACKSPACE)

        color = self.driver.find_element(By.ID, self.multiple_input).is_displayed()
        if color:
            self.driver.save_screenshot(self.ss_url_widget + "Auto complete Multiple input.png")
            assert True
        else:
            assert False

    def test_single_color_input(self):
        # Wait for the page to load
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.single_input)))

        # Locate the autocomplete input field by its ID
        autocomplete_input = self.driver.find_element(By.XPATH, self.single_input)

        # Enter a value into the input field
        autocomplete_input.send_keys("wh")
        time.sleep(1)
        autocomplete_input.send_keys(Keys.ENTER)
        time.sleep(2)

        colors = self.driver.find_element(By.XPATH, self.single_input).is_displayed()
        if colors:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url_widget + "Auto complete Single input.png")
            assert True












