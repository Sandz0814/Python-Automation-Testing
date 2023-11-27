import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tools.function import BaseDriver
from selenium.webdriver.common.action_chains import ActionChains


class Slider(BaseDriver):
    slider_module = "//span[normalize-space()='Slider']"
    slider_range = "//input[@type='range']"
    header = "//div[@class='main-header']"

    def __init__(self, driver):
        self.driver = driver

    def test_open_slider_module(self):
        self.page_scroll()
        self.find(self.slider_module).click()

    def test_header(self):
        headers = self.find(self.header).text
        if "Slider" in headers:
            self.driver.save_screenshot(self.ss_url_widget + "slider header.png")
            assert True
        else:
            assert False

    def test_slider(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.slider_range)))
        slider = self.find(self.slider_range)
        # desired_position = 0
        action = ActionChains(self.driver)
        time.sleep(3)
        action.click_and_hold(slider).move_by_offset(100, 0).release().perform()



