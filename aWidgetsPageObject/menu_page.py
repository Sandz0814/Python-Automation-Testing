import time
from selenium.webdriver import ActionChains
from Tools.function import BaseDriver


class Menu(BaseDriver):

    menu_module = "//span[normalize-space()='Menu']"
    header = "//div[@class='main-header']"
    main_menu2 = "//a[normalize-space()='Main Item 2']"
    sub_menu1 = "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/ul[1]/li[2]/ul[1]/li[1]/a[1]"
    sub_menu2 = "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/ul[1]/li[2]/ul[1]/li[2]/a[1]"
    sub_list = "//a[contains(text(),'SUB SUB LIST »')]"
    sub_list1 = "//a[contains(text(),'Sub Sub Item 1')]"
    sub_list2 = "//a[contains(text(),'Sub Sub Item 2')]"
    main_menu1 = "//a[normalize-space()='Main Item 1']"
    main_menu3 = "//a[normalize-space()='Main Item 3']"

    def __init__(self, driver):
        self.driver = driver

    def test_menu_tab(self):
        self.find(self.menu_module).click()
        time.sleep(2)

    def test_header(self):
        headers = self.find(self.header).text
        assert "Menu" in headers
        self.driver.save_screenshot(self.ss_url_widget + "Menu Header.png")

    def test_menu2(self):
        action = ActionChains(self.driver)
        main = self.find(self.main_menu2)
        sub1 = self.find(self.sub_menu1)
        sub2 = self.find(self.sub_menu2)
        sublist = self.find(self.sub_list)
        sublist1 = self.find(self.sub_list1)
        sublist2 = self.find(self.sub_list2)

        (action.move_to_element(main).move_to_element(sub1).move_to_element(sub2)
         .move_to_element(sublist).move_to_element(sublist1).move_to_element(sublist2)).perform()
        time.sleep(2)
        self.driver.save_screenshot(self.ss_url_widget + "Main Item 2.png")

    def test_menu1(self):
        action = ActionChains(self.driver)
        main1 = self.find(self.main_menu1)
        (action.move_to_element(main1)).perform()
        time.sleep(3)
        self.driver.save_screenshot(self.ss_url_widget + "Main Item 1.png")

    def test_menu3(self):
        action = ActionChains(self.driver)
        main1 = self.find(self.main_menu3)
        (action.move_to_element(main1)).perform()
        time.sleep(2)
        self.driver.save_screenshot(self.ss_url_widget + "Main Item 3.png")












