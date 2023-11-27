import time
from selenium.webdriver.common.by import By
from Tools.function import BaseDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProgressBar(BaseDriver):

    progress_bar_module = "//span[normalize-space()='Progress Bar']"
    header = "//div[@class='main-header']"
    start_btn = "//button[@id='startStopButton']"
    reset_btn = "//button[@id='resetButton']"

    def __init__(self, driver):
        self.driver = driver

    def test_progress_bar(self):
        self.find(self.progress_bar_module).click()
        time.sleep(2)

    def test_header(self):
        progress_header = self.find(self.header).text
        if "Progress Bar" in progress_header:
            self.driver.save_screenshot(self.ss_url_widget + "Progress Bar Header.png")
        else:
            assert False

    def test_start_btn(self):
        self.find(self.start_btn).click()
        time.sleep(5)  # for 50%
        self.find(self.start_btn).click()
        progress = self.find(self.start_btn).is_displayed()
        if progress:
            self.driver.save_screenshot(self.ss_url_widget + "Progress Bar percent.png")
            assert True
        else:
            assert False

        time.sleep(1)
        self.find(self.start_btn).click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.reset_btn)))
        wait.until(EC.element_to_be_clickable((By.XPATH, self.reset_btn)))
        time.sleep(3)

        reset = self.find(self.reset_btn).is_displayed()
        if reset:
            self.driver.save_screenshot(self.ss_url_widget + "Reset Button.png")
            assert True
        else:
            assert False

        self.find(self.reset_btn).click()






