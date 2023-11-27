import time

from selenium.webdriver.common.by import By

from Tools.function import BaseDriver
from selenium.webdriver.common.action_chains import ActionChains


class ToolTip(BaseDriver):

    tool_tip_module = "//span[normalize-space()='Tool Tips']"
    tool_tip_header = "//div[@class='main-header']"
    tool_tip_btn = "//button[@id='toolTipButton']"
    tool_tip_text_field = "//input[@id='toolTipTextField']"
    contrary = "//a[normalize-space()='Contrary']"
    section = "//a[normalize-space()='1.10.32']"

    def __init__(self, driver):
        self.driver = driver

    def test_tool_tip_module(self):
        self.find(self.tool_tip_module).click()
        time.sleep(2)

    def test_hover_me(self):
        action = ActionChains(self.driver)
        hover_me = self.find(self.tool_tip_btn)
        action.move_to_element(hover_me).perform()
        time.sleep(3)
        tool_tip_text = self.find(self.tool_tip_btn).is_displayed()
        if tool_tip_text:
            self.driver.save_screenshot(self.ss_url_widget + "Hover Me to see.png")
            assert True
        else:
            assert False

    def test_contrary(self):
        action = ActionChains(self.driver)
        contrary = self.find(self.contrary)
        action.move_to_element(contrary).perform()
        time.sleep(3)
        tool_tip_text = self.find(self.contrary).is_displayed()
        if tool_tip_text:
            self.driver.save_screenshot(self.ss_url_widget + "Hover Contrary.png")
            assert True
        else:
            assert False

    def test_section(self):
        action = ActionChains(self.driver)
        section = self.find(self.section)
        action.move_to_element(section).perform()
        time.sleep(3)
        tool_tip_text = self.find(self.section).is_displayed()
        if tool_tip_text:
            self.driver.save_screenshot(self.ss_url_widget + "Hover 1.10.32.png")
            assert True
        else:
            assert False





