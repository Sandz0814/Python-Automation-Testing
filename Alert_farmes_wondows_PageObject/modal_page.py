import time
from Tools.function import BaseDriver


class Modal(BaseDriver):

    modal_module = "//span[normalize-space()='Modal Dialogs']"
    main_header = "//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]"

    small_modal = "//button[@id='showSmallModal']"
    small_modal_id = "//div[@id='example-modal-sizes-title-sm']"
    small_modal_assert = "//div[@class='modal-body']"
    small_modal_close = "//body[1]/div[5]/div[1]/div[1]/div[3]/button[1]"

    large_modal = "//button[@id='showLargeModal']"
    large_modal_assert = "//p[contains(text(),'Lorem Ipsum is simply dummy text of the printing a')]"
    large_modal_close = "//body[1]/div[5]/div[1]/div[1]/div[3]/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def test_modal_btn(self):
        self.find(self.modal_module).click()
        time.sleep(1)

    def test_assert_header_name(self):

        header_name = self.find(self.main_header).text
        if "Modal Dialogs" not in header_name:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url_afw + "Modal.png")
            assert True

    def test_click_small_modal(self):
        self.find(self.small_modal).click()
        time.sleep(1)
        modal_body = self.find(self.small_modal_assert).text
        if "This is a small modal. It has very less content" not in modal_body:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url_afw + "Small modal Body.png")
            assert True
        time.sleep(1)
        # close the small modal
        self.find(self.small_modal_close).click()

    def test_click_large_modal(self):
        self.find(self.large_modal).click()
        time.sleep(1)

        modal_body = self.find(self.large_modal_assert).text
        word = modal_body.split()
        assert_word = word[4]
        if "dummy" not in assert_word:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url_afw + "Large modal body.png")
            assert True

        self.close()











