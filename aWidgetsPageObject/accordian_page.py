import time
from Tools.function import BaseDriver


class Widgets(BaseDriver):

    widgets_btn = "//div[4]//div[1]//div[2]//*[name()='svg']"
    accordian_module_tab = "//span[normalize-space()='Accordian']"
    main_header = "//div[contains(text(),'Accordian')]"
    accordion1 = "//div[@id='section1Heading']"
    accordion2 = "//div[@id='section2Heading']"
    accordion3 = "//div[@id='section3Heading']"

    def __init__(self, driver):
        self.driver = driver

    def test_click_widgets_icon(self):
        self.find(self.widgets_btn).click()
        time.sleep(2)

    def test_open_accordian_module(self):
        self.find(self.accordian_module_tab).click()
        time.sleep(2)

    def test_header_main(self):
        header = self.find(self.main_header).text
        if "Accordian" not in header:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url_widget + "Accordian header.png")
        time.sleep(2)

    def test_accordion1_header(self):
        self.find(self.accordion1).click()
        time.sleep(2)
        assertion = self.find(self.accordion1).text
        if "What is Lorem Ipsum?" not in assertion:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url_widget + " What is Lorem Ipsum collapse.png")
            assert True

    def test_accordion2_header(self):
        self.find(self.accordion2).click()
        time.sleep(2)
        content = self.find(self.accordion2).text
        if "Where does it come from?" not in content:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url_widget + "Where does if come from expand.png")
            assert True

    def test_accordion3_header(self):
        self.find(self.accordion3).click()
        time.sleep(2)
        content = self.find(self.accordion3).text
        if "Why do we use it?" not in content:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url_widget + "Why do we use it expand.png")
            assert True

            







