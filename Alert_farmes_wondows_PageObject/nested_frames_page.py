import time
from selenium.webdriver.common.by import By
from Tools.function import BaseDriver


class NestedFrames(BaseDriver):
    nested_frames_btn = "//span[normalize-space()='Nested Frames']"
    parent_iframe = "#frame1"
    parent_iframe_text = "//body"
    child_iframe = "//iframe[@id='frame1']"
    child_iframe_text = "body:nth-child(2) > p:nth-child(1)"

    def __init__(self, driver):
        self.driver = driver

    def test_nested_frame_btn(self):
        self.find(self.nested_frames_btn).click()
        time.sleep(2)

    def test_nested_parent_iframe(self):

        # Locate the parent iframe element
        parent = self.driver.find_element(By.CSS_SELECTOR, self.parent_iframe)

        # Switch to the parent iframe using the WebElement
        self.driver.switch_to.frame(parent)

        # Now you can interact with elements inside the parent iframe
        parent_text = self.find(self.parent_iframe_text).text
        if "Parent frame" not in parent_text:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url_afw + "Nested Parent Iframe.png")
            assert True

        self.driver.switch_to.default_content()

    def test_nested_child_iframe(self):
        # Locate the child iframe element
        child = self.driver.find_element(By.XPATH, self.child_iframe)

        # Switch to the child iframe using the WebElement
        self.driver.switch_to.frame(child)

        self.driver.save_screenshot(self.ss_url_afw + "Nested Child Iframe.png")

        self.driver.switch_to.default_content()






