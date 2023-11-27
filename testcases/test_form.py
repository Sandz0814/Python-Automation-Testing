import pytest
from FormPageObject.Practice_form_page import PracticeFormPage
from Tools.function import BaseDriver


@pytest.mark.usefixtures("setup")
class TestElement(BaseDriver):
    def test_form(self, setup):
        self.driver = setup
        self.page_scroll()

        self.tf = PracticeFormPage(self.driver)

        self.tf.test_forms()
        self.tf.test_student_info()
        self.tf.test_random_gender()
        self.tf.test_random_mobile()
        self.tf.test_random_dob()
        self.tf.test_random_subject()
        self.tf.test_random_hobbies()
        self.tf.test_upload_pic()
        self.tf.test_address()
        self.tf.test_select_state_and_city()
        self.tf.test_submits()
        self.tf.test_confirmation()



