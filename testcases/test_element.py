import time
import pytest
from ElementPageObject.textbox_page import TextBox
from ElementPageObject.checkbox_page import CheckBox
from ElementPageObject.radiobutton_page import RadioButton
from ElementPageObject.upload_download_page import UploadDownloadPage
from ElementPageObject.webtable_page import WebTablePage
from ElementPageObject.buttons_page import ButtonPage
from ElementPageObject.link_page import LinkPage
from ElementPageObject.broken_link_page import BrokenLink
from ElementPageObject.dynamic_property_page import DynamicPropertyPage
from Tools.function import BaseDriver


@pytest.mark.usefixtures("setup")
class TestElement(BaseDriver):

    def test_element(self, setup):
        self.driver = setup
        self.page_scroll()

        # Verifying the text box funtion
        self.tb = TextBox(self.driver)
        self.tb.test_element()
        self.tb.test_text_box()

        # Verifying the CheckBox funtion
        self.cb = CheckBox(self.driver)
        self.cb.test_check_boxs()

        # Verifying the Radio Button function
        self.rb = RadioButton(self.driver)
        self.rb.test_radio_btn()

        # Verifying the Add employee function
        self.wt = WebTablePage(self.driver)
        self.wt.test_web_table_add_employee()
        self.wt.test_search_employee()
        self.wt.test_edit_employee()
        self.wt.test_delete_employee()

        # Verifying the Button Functions
        self.btn = ButtonPage(self.driver)
        self.btn.test_buttons()
        self.btn.test_double_clicks()
        self.btn.test_right_clicks()
        self.btn.test_click_me()

        # Verifying the Link functions
        self.lp = LinkPage(self.driver)
        self.lp.test_open_link()
        self.lp.test_home_link()
        self.lp.test_created_link()
        self.page_scroll()

        # Verifying the Broken Link Functions
        self.bl = BrokenLink(self.driver)
        self.bl.test_broken_link()
        self.bl.test_click_for_valid_link()
        self.bl.test_click_for_broken_link()
        self.page_scroll()

        # Verifying the Download and Upload function
        self.ud = UploadDownloadPage(self.driver)
        self.ud.test_upload_download()
        self.ud.test_download()
        self.ud.test_uploads()
        self.page_scroll()

        # Verifying the Dynamic properties function
        self.dp = DynamicPropertyPage(self.driver)
        self.dp.test_dynamic_property()
        self.dp.test_enable_in_5secs()
        self.dp.test_assertion()

        time.sleep(10)

