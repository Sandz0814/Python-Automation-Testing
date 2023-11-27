import time
from selenium.webdriver.common.by import By
from Tools.function import BaseDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicPropertyPage(BaseDriver):

    dynamic_properties = "//span[normalize-space()='Dynamic Properties']"
    enable_in_5secs = "//button[@id='enableAfter']"
    change_color = "//button[@id='colorChange']"
    visible_in_5secs = "//button[@id='visibleAfter']"
    assertion = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/p[1]"

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        return element

    def wait(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
        return element

    def test_dynamic_property(self):
        self.find(self.dynamic_properties).click()
        time.sleep(5)

    def test_enable_in_5secs(self):
        self.wait(self.enable_in_5secs)
        time.sleep(5)
        self.wait(self.change_color)
        time.sleep(5)
        self.wait(self.visible_in_5secs)

    def test_assertion(self):
        asserts = self.find(self.assertion).text
        if "This text has random Id" not in asserts:
            print("Element not visible")
            assert False
        else:
            self.driver.save_screenshot(self.ss_url + "Dynamic Properties.png")
        self.page_scroll()
        self.driver.close()
        self.driver.quit()




