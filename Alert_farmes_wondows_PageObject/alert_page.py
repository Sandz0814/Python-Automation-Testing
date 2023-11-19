import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from Tools.function import BaseDriver


class AlertPage(BaseDriver):

    alert_btn = "//span[normalize-space()='Alerts']"
    module_assert = "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]"
    click_alert = "//button[@id='alertButton']"
    alert_appear_5sec = "//button[@id='timerAlertButton']"
    alert_appear_confirm_box = "//button[@id='confirmButton']"
    confirmation_msg = "//span[@id='confirmResult']"
    alert_appear_prompt_box = "//button[@id='promtButton']"
    prompt_result = "//span[@id='promptResult']"

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        return element

    def test_alert_btn(self):
        self.find(self.alert_btn).click()
        alert_page = self.find(self.module_assert).text
        if "Alerts" not in alert_page:
            print("No such text found")
            assert False
        else:
            self.driver.save_screenshot(self.ss_url_afw + "Alert Page.png")
            assert True

    def test_click_alert(self):
        self.find(self.click_alert).click()
        alert = Alert(self.driver)
        time.sleep(3)
        alert.accept()

    def test_click_appear_5sec(self):
        self.find(self.alert_appear_5sec).click()
        time.sleep(5)
        alert = Alert(self.driver)
        time.sleep(3)
        alert.accept()

    def test_alert_appear_confirm_box(self):
        self.find(self.alert_appear_confirm_box).click()
        alert = Alert(self.driver)
        alert.accept()

        selected_ok = self.find(self.confirmation_msg).is_displayed()
        if selected_ok:
            self.driver.save_screenshot(self.ss_url_afw + "Confirm Alert Box Ok.png")
            assert True
        else:
            assert False

        time.sleep(2)

        self.find(self.alert_appear_confirm_box).click()
        alert = Alert(self.driver)
        alert.dismiss()

        selected_cancel = self.find(self.confirmation_msg).is_displayed()
        if selected_cancel:
            self.driver.save_screenshot(self.ss_url_afw + "Confirm Alert Box Cancel.png")
            assert True
        else:
            assert False

    def test_alert_appear_prompt_box(self):
        self.find(self.alert_appear_prompt_box).click()
        alert = Alert(self.driver)
        alert.send_keys("Luna and Panini pretty")
        alert.accept()
        confirm_send_key = self.find(self.prompt_result).is_displayed()
        if confirm_send_key:
            self.driver.save_screenshot(self.ss_url_afw + "Prompt Box send Key.png")
            assert True
        else:
            assert False

        time.sleep(2)











