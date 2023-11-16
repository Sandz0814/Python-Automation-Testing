import time
from selenium.webdriver.common.by import By
from Tools.function import BaseDriver


class LinkPage(BaseDriver):

    links = "//span[normalize-space()='Links']"
    home_link = "//a[@id='simpleLink']"
    home_link_new_tab = "//body[1]/div[2]/header[1]/a[1]/img[1]"
    home_yiw6j_link = "//a[@id='dynamicLink']"
    created_link = "//a[@id='created']"
    created_link_response = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/p[10]"

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        return element

    def test_open_link(self):
        self.find_element(self.links).click()
        time.sleep(1)

    def test_home_link(self):
        self.find_element(self.home_link).click()
        time.sleep(1)
        original_window_handle = self.driver.window_handles[0]
        new_tab_handle = self.driver.window_handles[1]

        self.driver.switch_to.window(new_tab_handle)
        new_tab = self.find_element(self.home_link_new_tab).is_displayed()
        if new_tab:
            self.driver.save_screenshot(self.ss_url + "New Tab.png")
            assert True
        else:
            assert False
        time.sleep(1)
        self.driver.close()
        self.driver.switch_to.window(original_window_handle)

    def test_created_link(self):
        self.find_element(self.created_link).click()
        time.sleep(1)

        link_response = self.find_element(self.created_link_response).text
        if "Link has responded with staus 201 and status text Created" not in link_response:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url + "Link response.png")
            assert True



