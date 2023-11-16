import time
from selenium.webdriver.common.by import By
from Tools.function import BaseDriver
from selenium.webdriver.common.action_chains import ActionChains


class ButtonPage(BaseDriver):

    buttons_btn = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[5]/span[1]"
    double_click = "//button[@id='doubleClickBtn']"
    double_click_message = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/p[1]"
    right_click = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/button[1]"
    right_click_message = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/p[2]"
    click_me = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/button[1]"
    click_me_message = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/p[3]"

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        return element

    def test_buttons(self):
        self.find_element(self.buttons_btn).click()
        time.sleep(1)

    def test_double_clicks(self):
        dc = self.find_element(self.double_click)
        action_chains = ActionChains(self.driver)
        action_chains.double_click(dc).perform()
        time.sleep(1)

        dc_message = self.find_element(self.double_click_message).text
        if "You have done a double click" not in dc_message:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url + "Double Click.png")
            assert True

    def test_right_clicks(self):
        rc = self.find_element(self.right_click)
        action_chains = ActionChains(self.driver)
        action_chains.context_click(rc).perform()
        time.sleep(1)

        rc_message = self.find_element(self.right_click_message).text
        if "You have done a right click" not in rc_message:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url + "Right Click.png")
            assert True

    def test_click_me(self):
        self.find_element(self.click_me).click()
        time.sleep(1)
        cm_message = self.find_element(self.click_me_message).text
        if "You have done a dynamic click" not in cm_message:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url + "Click Me.png")
            assert True



