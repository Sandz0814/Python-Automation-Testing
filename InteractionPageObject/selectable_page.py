import time
from Tools.function import BaseDriver


class Selectable(BaseDriver):

    selectable_module = "//span[contains(text(),'Selectable')]"
    header = "//body[1]/div[2]/div[1]/div[1]/div[1]"

    grid = "//a[@id='demo-tab-grid']"
    row1 = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]"
    one = "//li[contains(text(),'One')]"
    five = "//li[contains(text(),'Five')]"
    Nine = "//li[contains(text(),'Nine')]"
    three = "//li[normalize-space()='Three']"
    seven = "//li[normalize-space()='Seven']"

    list = "//a[@id='demo-tab-list']"
    list1 = "//li[normalize-space()='Cras justo odio']"
    list4 = "//li[normalize-space()='Porta ac consectetur ac']"

    def __init__(self, driver):
        self.driver = driver

    def test_open_selectable_module(self):
        self.find(self.selectable_module).click()

    def test_header(self):
        headers = self.find(self.header).text
        assert "Selectable" in headers
        self.driver.save_screenshot(self.ss_url_interaction + "Selectable Header.png")

    def test_grid(self):
        self.find(self.grid).click()

    def test_select_grid_13579(self):
        self.find(self.one).click()
        self.find(self.five).click()
        self.find(self.Nine).click()
        self.find(self.three).click()
        self.find(self.seven).click()
        self.driver.save_screenshot(self.ss_url_interaction + "Grid Type Selectable.png")

    def test_list(self):
        self.find(self.list).click()
        time.sleep(1)

    def test_select_list_select_14(self):
        self.find(self.list1).click()
        time.sleep(1)
        self.find(self.list4).click()
        self.driver.save_screenshot(self.ss_url_interaction + "List Type Selectable.png")











