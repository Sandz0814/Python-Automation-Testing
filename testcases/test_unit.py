import pytest
from Alert_farmes_wondows_PageObject.brower_window_page import BrowserWindows
from Alert_farmes_wondows_PageObject.nested_frames_page import NestedFrames
from Tools.function import BaseDriver


@pytest.mark.usefixtures("setup")
class TestElements(BaseDriver):

    def test_unit(self):
        self.page_scroll()

        self.afw = BrowserWindows(self.driver)
        self.page_scroll()
        self.afw.test_afw_btn()

        self.nested = NestedFrames(self.driver)
        self.nested.test_nested_frame_btn()
        self.nested.test_nested_parent_iframe()
        self.nested.test_nested_child_iframe()









