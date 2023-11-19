import time
from selenium.webdriver.common.by import By
from Tools.function import BaseDriver


class BrowserWindows(BaseDriver):
    alert_btn = "//div[3]//div[1]//div[2]//*[name()='svg']"
    browser_window_btn = "//span[normalize-space()='Browser Windows']"
    new_tab_btn = "//button[@id='tabButton']"
    new_tab_window = "//h1[@id='sampleHeading']"
    new_window_btn = "//button[@id='windowButton']"
    new_window_link = "//h1[@id='sampleHeading']"
    new_window_msg_btn = "//button[@id='messageWindowButton']"
    new_window_msg_link = "//body"

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        return element

    def test_afw_btn(self):
        self.find(self.alert_btn).click()
        time.sleep(2)

    def test_browser_btn(self):
        self.find(self.browser_window_btn).click()
        time.sleep(2)

    def test_new_tab(self):
        self.find(self.new_tab_btn).click()

        original_window_handle = self.driver.window_handles[0]
        new_tab_handle = self.driver.window_handles[1]

        self.driver.switch_to.window(new_tab_handle)
        new_tab = self.find(self.new_tab_window).is_displayed()
        if new_tab:
            self.driver.save_screenshot(self.ss_url_afw + " Browser window New Tab.png")
            assert True
        else:
            assert False
        time.sleep(1)
        self.driver.close()
        self.driver.switch_to.window(original_window_handle)
        time.sleep(2)

    def test_new_window(self):
        # Get the current window handle (main window)
        main_window = self.driver.window_handles[0]

        # Perform an action that opens a new window
        self.find(self.new_window_btn).click()

        # Get the handles of all open windows
        all_windows = self.driver.window_handles

        # Iterate through the windows and switch to the new one
        for window in all_windows:
            if window != main_window:
                self.driver.switch_to.window(window)
                break

        # interact with elements in the new window
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        new_windows = self.find(self.new_window_link).text
        if "This is a sample page" not in new_windows:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url_afw + " New windows.png")
            assert True
            time.sleep(2)

            self.driver.close()
            self.driver.switch_to.window(main_window)
            # Continue with actions on the main window
            time.sleep(2)

    def test_new_window_msg(self):
        # Get the current window handle (main window)
        main_window = self.driver.window_handles[0]

        self.find(self.new_window_msg_btn).click()

        # Get the handles of all open windows
        new_windows = self.driver.window_handles

        # Iterate through the windows and switch to the new one
        for window in new_windows:
            if window != main_window:
                self.driver.switch_to.window(window)
                time.sleep(5)
                self.driver.close()

        self.driver.switch_to.window(main_window)
















