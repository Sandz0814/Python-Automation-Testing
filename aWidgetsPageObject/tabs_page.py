import time
from Tools.function import BaseDriver


class Tabs(BaseDriver):

    tabs_module = "//span[normalize-space()='Tabs']"
    header = "//div[@class='main-header']"
    what = "//a[@id='demo-tab-what']"
    what_tab = "//p[contains(text(),'Lorem Ipsum is simply dummy text of the printing a')]"
    origin = "//a[@id='demo-tab-origin']"
    origin_tab = "//p[contains(text(),'Contrary to popular belief, Lorem Ipsum is not sim')]"
    use = "//a[@id='demo-tab-use']"
    use_tab = "//p[contains(text(),'It is a long established fact that a reader will b')]"

    def __init__(self, driver):
        self.driver = driver

    def test_tab_module(self):
        self.find(self.tabs_module).click()
        time.sleep(2)
        headers = self.find(self.header).text
        assert "Tabs" in headers
        self.driver.save_screenshot(self.ss_url_widget + "Tabs Header.png")

    def test_what(self):
        self.find(self.what).click()
        what_word = self.find(self.what_tab).text
        paragraph = what_word.split()
        word = paragraph[4]
        assert "dummy" in word
        self.driver.save_screenshot(self.ss_url_widget + "What Tab.png")

    def test_origin(self):
        self.find(self.origin).click()
        origin_word = self.find(self.origin_tab).text
        paragraph = origin_word.split()
        word = paragraph[3]
        assert "belief" in word
        self.driver.save_screenshot(self.ss_url_widget + "Origin Tab.png")

    def test_use(self):
        self.find(self.use).click()
        use_word = self.find(self.use_tab).text
        paragraph = use_word.split()
        word = paragraph[4]
        assert "established" in word
        self.driver.save_screenshot(self.ss_url_widget + "Use Tab.png")
