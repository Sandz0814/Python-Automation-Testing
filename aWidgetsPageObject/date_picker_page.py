import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tools.function import BaseDriver
from selenium.webdriver import Keys


class DatePicker(BaseDriver):

    date_picker_tab = "//span[normalize-space()='Date Picker']"
    header = "//div[contains(text(),'Date Picker')]"
    select_date = "//input[@id='datePickerMonthYearInput']"
    select_month = "//option[contains(text(),'August')]"
    select_year = "//option[contains(text(),'1979')]"
    select_day = "//div[@aria-label='Choose Wednesday, August 8th, 1979']"

    date_time = "//input[@id='dateAndTimePickerInput']"
    date_time_month = ("//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]"
                       "/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]")
    date_time_month_option = ("//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div"
                              "[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[8]")
    date_time_day = "//div[@aria-label='Choose Sunday, August 8th, 2021']"
    date_time_year = ("//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]"
                      "/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/span[1]")
    date_time_year_option = "//div[9]"
    date_time_time = "//li[contains(text(),'20:30')]"

    def __init__(self, driver):
        self.driver = driver

    def test_open_tab(self):
        self.find(self.date_picker_tab).click()
        time.sleep(2)

    def test_header(self):
        headers = self.find(self.header).text
        if "Date Picker" not in headers:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url_widget + " Date Picker Header.png")
            assert True

    def test_select_date(self):
        # Wait for the page to load
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.select_date)))

        date_select = self.find(self.select_date)
        date_select.click()

        # Wait for the month dropdown to be clickable
        wait.until(EC.element_to_be_clickable((By.XPATH, self.select_month)))
        self.find(self.select_month).click()

        # Wait for the year dropdown to be clickable
        wait.until(EC.element_to_be_clickable((By.XPATH, self.select_year)))
        self.find(self.select_year).click()

        # Wait for the day to be clickable
        wait.until(EC.element_to_be_clickable((By.XPATH, self.select_day)))
        self.find(self.select_day).click()

        # Wait for the inputted date to be updated
        # wait.until(lambda driver: self.find(self.select_date).get_attribute("value") == "08/08/1979")

        # Assert the inputted date
        inputted_date = self.find(self.select_date).get_attribute("value")
        assert "08/08/1979" in inputted_date
        self.driver.save_screenshot(self.ss_url_widget + "Select date.png")

    def test_date_and_time(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.date_time)))
        self.find(self.date_time).click()

        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.date_time_year)))
        self.find(self.date_time_year).click()
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, self.date_time_year_option)))
        wait.until(EC.element_to_be_clickable((By.XPATH, self.date_time_year_option)))
        self.find(self.date_time_year_option).click()

        time.sleep(3)

        wait.until(EC.element_to_be_clickable((By.XPATH, self.date_time_month)))
        self.find(self.date_time_month).click()
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.date_time_month_option)))
        self.find(self.date_time_month_option).click()

        time.sleep(3)

        wait.until(EC.element_to_be_clickable((By.XPATH, self.date_time_day)))
        self.find(self.date_time_day).click()

        time.sleep(3)

        wait.until(EC.element_to_be_clickable((By.XPATH, self.date_time_time)))
        self.find(self.date_time_time).click()
        time.sleep(3)

    def test_date_time_input(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.date_time)))
        back_space = self.find(self.date_time)
        for _ in range(25):
            back_space.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        self.find(self.date_time).send_keys("August 08, 1979 6:13 PM")
        self.find(self.date_time).send_keys(Keys.ENTER)

        date_time = self.find(self.date_time).text
        if "August 08, 1979 6:13 PM" not in date_time:
            self.driver.save_screenshot(self.ss_url_widget + "Date time.png")
            assert True
        else:
            assert False




















