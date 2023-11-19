import pytest
from Alert_farmes_wondows_PageObject.alert_page import AlertPage
from Alert_farmes_wondows_PageObject.brower_window_page import BrowserWindows
from Alert_farmes_wondows_PageObject.iframe_page import FramePage
from Tools.function import BaseDriver


@pytest.mark.usefixtures("setup")
class TestElements(BaseDriver):

    def test_unit(self):
        self.page_scroll()

        self.afw = BrowserWindows(self.driver)
        self.page_scroll()
        self.afw.test_afw_btn()

        self.iframe = FramePage(self.driver)
        self.iframe.test_frame_module_btn()
        self.iframe.test_iframe1()
        self.iframe.test_iframe2()









