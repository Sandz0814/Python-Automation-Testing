import time
from selenium.webdriver.common.by import By
from Tools.function import BaseDriver


class RadioButton(BaseDriver):
    radio_btn = "//span[normalize-space()='Radio Button']"
    radio_btn_txt = "//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]"
    yes = "//label[@for='yesRadio']"
    impressive = "//label[@for='impressiveRadio']"

    def __init__(self, driver):
        self.driver = driver

    def test_radio_btn(self):
        self.page_scroll()
        self.wait_until_element_is_clickable(By.XPATH, self.radio_btn).click()
        # self.driver.find_element(By.XPATH, self.radio_btn).click()
        title = self.driver.find_element(By.XPATH, self.radio_btn_txt).text
        if "Radio Button" not in title:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url + "Radio button Title.png")
            assert True
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.yes).click()
        yeah = self.driver.find_element(By.XPATH, self.yes).text
        if "Yes" not in yeah:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url + "Radio button Yes.png")
            assert True

        self.driver.find_element(By.XPATH, self.impressive).click()
        time.sleep(2)
        great = self.driver.find_element(By.XPATH, self.impressive).text
        if "Impressive" not in great:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url + "Radio button Impressive.png")
            assert True
            time.sleep(2)
            self.page_scroll()











