import time
from selenium.webdriver.common.by import By
from Tools.function import BaseDriver


class CheckBox(BaseDriver):
    check_box = "//span[normalize-space()='Check Box']"
    dropdown = "//button[@title='Toggle']//*[name()='svg']"
    home = "//span[contains(text(),'Home')]"
    you_have_selected = "//span[normalize-space()='You have selected :']"
    drop_up = "//*[name()='path' and contains(@d,'M7.41 7.84')]"
    expand_icon = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/button[1]"
    collapse_icon = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/button[2]"

    private_txt = '//*[@id="tree-node"]/ol/li/ol/li[2]/ol/li[2]/ol/li[2]/span/label/span[3]'

    desktop = "//label[@for='tree-node-desktop']//span[@class='rct-checkbox']//*[name()='svg']"
    documents = "//label[@for='tree-node-documents']//span[@class='rct-checkbox']//*[name()='svg']"
    downloads = "//label[@for='tree-node-downloads']//span[@class='rct-checkbox']//*[name()='svg']"

    def __init__(self, driver):
        self.driver = driver

    def test_check_boxs(self):
        self.driver.find_element(By.XPATH, self.check_box).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.dropdown).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.home).click()
        time.sleep(1)
        status = self.driver.find_element(By.XPATH, self.you_have_selected).text
        if "You have selected" not in status:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url + "check box.png")
            assert True

        time.sleep(1)
        self.driver.find_element(By.XPATH, self.expand_icon).click()
        time.sleep(1)
        private_text = self.driver.find_element(By.XPATH, self.private_txt).text
        if "Private" not in private_text:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url + "expand all.png")
            assert True
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.collapse_icon).click()
        time.sleep(1)










