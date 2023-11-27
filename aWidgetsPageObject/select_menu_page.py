import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Tools.function import BaseDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SelectMenu(BaseDriver):

    select_menu_module = "//span[normalize-space()='Select Menu']"
    header = "//div[@class='main-header']"
    select_value = "//div[@id='withOptGroup']//div[@class=' css-tlfecz-indicatorContainer']//*[name()='svg']"
    group2_option1 = "//div[contains(text(),'Group 2, option 1')]"
    select_one = "//div[@id='selectOne']//div[@class=' css-tlfecz-indicatorContainer']//*[name()='svg']"
    prof = "//div[contains(text(),'Prof.')]"
    old_style_select_menu = "//select[@id='oldSelectMenu']"
    multi_select_dropdown = "react-select-4-input"
    standard_multi_select = "//select[@id='cars']"

    def __init__(self, driver):
        self.driver = driver

    def test_open_select_menu(self):
        self.page_scroll()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.select_menu_module)))
        wait.until(EC.element_to_be_clickable((By.XPATH, self.select_menu_module)))
        self.find(self.select_menu_module).click()

    def test_header(self):
        headers = self.find(self.header).text
        assert "Select Menu" in headers
        self.driver.save_screenshot(self.ss_url_widget + "Select Menu Header.png")

    def test_select_value(self):
        self.find(self.select_value).click()
        time.sleep(1)
        self.find(self.group2_option1).click()
        self.driver.save_screenshot(self.ss_url_widget + "Select Value.png")

    def test_select_one(self):
        self.find(self.select_one).click()
        time.sleep(1)
        self.find(self.prof).click()
        self.driver.save_screenshot(self.ss_url_widget + "Select Value.png")

    def test_old_select_menu(self):
        dropdown = self.find(self.old_style_select_menu)
        select = Select(dropdown)
        select.select_by_index(3)
        self.driver.save_screenshot(self.ss_url_widget + "Select old style menu.png")

    def test_multi_dropdown(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, self.multi_select_dropdown)))
        multi_select = self.driver.find_element(By.ID, self.multi_select_dropdown)
        multi_select.send_keys("Black")
        multi_select.send_keys(Keys.ENTER)
        multi_select.send_keys("Blue")
        multi_select.send_keys(Keys.ENTER)
        multi_select.send_keys("Green")
        multi_select.send_keys(Keys.ENTER)
        multi_select.send_keys("Red")
        multi_select.send_keys(Keys.ENTER)
        self.driver.save_screenshot(self.ss_url_widget + "Multi select dropdown.png")

    def test_standard_multi_select(self):
        dropdown = self.find(self.standard_multi_select)
        select = Select(dropdown)
        select.select_by_index(0)
        select.select_by_index(1)
        select.select_by_index(2)
        select.select_by_index(3)
        time.sleep(2)
        self.driver.save_screenshot(self.ss_url_widget + "Standard Multi select.png")














