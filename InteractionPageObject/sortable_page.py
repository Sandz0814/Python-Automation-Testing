import time
from Tools.function import BaseDriver
from selenium.webdriver import ActionChains


class Sortable(BaseDriver):

    interaction_icon = "//*[name()='path' and contains(@d,'M880 112H1')]"
    sortable_module = "//span[contains(text(),'Sortable')]"
    header = "//div[contains(text(),'Sortable')]"

    grid = "//a[@id='demo-tab-grid']"
    one = "//div[@class='create-grid']//div[@class='list-group-item list-group-item-action'][normalize-space()='One']"
    nine = "//div[contains(text(),'Nine')]"
    eight = "//div[normalize-space()='Eight']"
    four = "//div[@class='create-grid']//div[@class='list-group-item list-group-item-action'][normalize-space()='Four']"

    list = "//a[@id='demo-tab-list']"
    two = "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]"
    six = "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[6]"
    three = "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]"
    five = "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[4]"

    def __init__(self, driver):
        self.driver = driver

    def test_open_interaction_icon(self):
        self.find_wait(self.interaction_icon)
        self.find(self.interaction_icon).click()

    def test_open_sortable_module(self):
        self.find(self.sortable_module).click()

    def test_header(self):
        headers = self.find(self.header).text
        assert "Sortable" in headers
        self.driver.save_screenshot(self.ss_url_interaction + "Sortable Header.png")

    def test_grid(self):
        self.find(self.grid).click()

    def test_one_move_to_nine(self):
        move_one = self.find(self.one)
        move_nine = self.find(self.nine)

        action = ActionChains(self.driver)
        action.click_and_hold(move_one).move_to_element(move_nine).release().perform()
        time.sleep(2)
        self.driver.save_screenshot(self.ss_url_interaction + "Grid Type Move One to Nine Position.png")

    def test_four_move_to_eight(self):
        move_four = self.find(self.four)
        move_eight = self.find(self.eight)

        action = ActionChains(self.driver)
        action.click_and_hold(move_four).move_to_element(move_eight).release().perform()
        time.sleep(2)
        self.driver.save_screenshot(self.ss_url_interaction + "Grid Type Move four to eight Position.png")

    def test_list(self):
        self.find(self.list).click()

    def test_two_move_to_six(self):
        move_two = self.find(self.two)
        move_six = self.find(self.six)

        action = ActionChains(self.driver)
        action.click_and_hold(move_two).move_to_element(move_six).release().perform()
        time.sleep(2)
        self.driver.save_screenshot(self.ss_url_interaction + "List Type Move Two to six Position.png")

    def test_three_move_to_five(self):
        move_three = self.find(self.three)
        move_five = self.find(self.five)

        action = ActionChains(self.driver)
        action.click_and_hold(move_three).move_to_element(move_five).release().perform()
        time.sleep(2)
        self.driver.save_screenshot(self.ss_url_interaction + "List Type Move Three to Five Position.png")
