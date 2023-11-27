import time
from Tools.function import BaseDriver
from selenium.webdriver.common.action_chains import ActionChains


class Resizable(BaseDriver):

    resizable_module = "//span[contains(text(),'Resizable')]"
    header = "//div[@class='main-header']"
    resizable_box = "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/span[1]"
    infinite_resize = "//div[@id='resizable']//span[@class='react-resizable-handle react-resizable-handle-se']"

    def __init__(self, driver):
        self.driver = driver

    def test_open_resizable_module(self):
        self.find(self.resizable_module).click()

    def test_header(self):
        headers = self.find(self.header).text
        assert "Resizable" in headers
        image = "Resizable Header.png"
        self.s_shot(self.ss_url_interaction, image)

    def test_resize_box(self):
        resize_box = self.find(self.resizable_box)

        actions = ActionChains(self.driver)
        # hover first the element
        actions.move_to_element(resize_box)
        time.sleep(2)
        # Simulate a click-and-hold on the resizable box
        actions.click_and_hold(resize_box).move_by_offset(300, 250).release().perform()
        time.sleep(2)
        image = "Resizable Box 400x250.png"
        self.s_shot(self.ss_url_interaction, image)

    def test_infinite_resize(self):
        infi_resize = self.find(self.infinite_resize)
        actions = ActionChains(self.driver)
        # hover first the element
        actions.move_to_element(infi_resize)
        time.sleep(2)
        # Simulate a click-and-hold on the resizable box
        actions.click_and_hold(infi_resize).move_by_offset(500, 300).release().perform()
        time.sleep(2)
        image = "Infinite Resizable 500x300.png"
        self.s_shot(self.ss_url_interaction, image)















