import pytest
from Alert_farmes_wondows_PageObject.alert_page import AlertPage
from Alert_farmes_wondows_PageObject.brower_window_page import BrowserWindows
from Alert_farmes_wondows_PageObject.iframe_page import FramePage
from Tools.function import BaseDriver


@pytest.mark.usefixtures("setup")
class TestElements(BaseDriver):

    def test_unit(self):

        self.page_scroll()
        # Verifying the Browser Module
        self.afw = BrowserWindows(self.driver)
        self.afw.test_afw_btn()
        self.afw.test_browser_btn()
        self.afw.test_new_tab()
        self.afw.test_new_window()
        self.afw.test_new_window_msg()

        # Verifying the Alert Module
        self.alert = AlertPage(self.driver)
        self.alert.test_alert_btn()
        self.alert.test_click_alert()
        self.alert.test_click_appear_5sec()
        self.alert.test_alert_appear_confirm_box()
        self.alert.test_alert_appear_prompt_box()

        # Verifying the Iframe module
        self.iframe = FramePage(self.driver)
        self.iframe.test_frame_module_btn()
        self.iframe.test_iframe1()
        self.iframe.test_iframe2()
