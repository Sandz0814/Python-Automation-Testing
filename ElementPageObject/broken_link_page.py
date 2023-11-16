from selenium.webdriver.common.by import By
from Tools.function import BaseDriver


class BrokenLink(BaseDriver):

    broken_links = "//span[normalize-space()='Broken Links - Images']"
    click_here_for_valid_link = "//a[normalize-space()='Click Here for Valid Link']"
    click_here_for_broken_link = "//a[normalize-space()='Click Here for Broken Link']"
    status_code = "//body[1]/div[2]/div[1]/div[1]/h3[1]"

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        return element

    def test_broken_link(self):
        self.find_element(self.broken_links).click()

    def test_click_for_valid_link(self):
        self.find_element(self.click_here_for_valid_link).click()
        self.driver.back()

    def test_click_for_broken_link(self):
        self.find_element(self.click_here_for_broken_link).click()
        stats_code = self.find_element(self.status_code).text
        if "Status Codes" not in stats_code:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url + "Broken Link.png")

        self.driver.back()






