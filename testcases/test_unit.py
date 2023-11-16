import time

import pytest
from FormPageObject.Practice_form_page import PracticeFormPage
from Tools.function import BaseDriver


@pytest.mark.usefixtures("setup")
class TestElement(BaseDriver):

    def test_unit(self):

        self.page_scroll()

        self.tf = PracticeFormPage(self.driver)
        self.tf.test_forms()
        self.tf.test_student_info()
        self.tf.test_random_gender()










