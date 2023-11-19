import time

from selenium.webdriver.common.by import By

from Tools.function import BaseDriver


class FramePage(BaseDriver):
    frames_btn = "//span[normalize-space()='Frames']"
    iframe1 = "frame1"
    iframe1_element = "sampleHeading"
    iframe2 = "frame2"
    iframe2_element = "sampleHeading"

    def __init__(self, driver):
        self.driver = driver

    def test_frame_module_btn(self):
        self.find(self.frames_btn).click()
        time.sleep(2)

    def test_iframe1(self):
        # Locate the iframe element
        iframe_element = self.driver.find_element(By.ID, self.iframe1)

        # Switch to the iframe using the WebElement
        self.driver.switch_to.frame(iframe_element)

        # Now you can interact with elements inside the iframe
        iframe_text = self.driver.find_element(By.ID, self.iframe1_element).text
        if "This is a sample page" not in iframe_text:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url_afw + "Iframe1 element.png")
            assert True

        # Switch back to the main content
        self.driver.switch_to.default_content()

    def test_iframe2(self):
        # Locate the iframe element
        iframe_element2 = self.driver.find_element(By.ID, self.iframe2)

        # Switch to the iframe using the WebElement
        self.driver.switch_to.frame(iframe_element2)

        # Now you can interact with elements inside the iframe
        iframe2_text = self.driver.find_element(By.ID, self.iframe2_element).text
        if "This is a sample page" not in iframe2_text:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url_afw + "Iframe2 element.png")
            assert True

        # Switch back to the main content
        self.driver.switch_to.default_content()





