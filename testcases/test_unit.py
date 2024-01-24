import time
import pytest
from Tools.function import BaseDriver
from book_store_app_PageOject.login_page import Register


@pytest.mark.usefixtures("setup")
class TestWidgets(BaseDriver):

    def test_unit(self):
        self.page_scroll()

        self.bs = Register(self.driver)
        self.bs.test_open_book_store_app()
        self.bs.test_open_login_tab()
        self.bs.test_header()
        self.bs.test_new_user_tab()
        self.bs.test_input_details()
        self.bs.test_login()
        self.bs.test_assert_profile()




