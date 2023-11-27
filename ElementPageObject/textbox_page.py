from selenium.webdriver.common.by import By
from Tools.function import BaseDriver


class TextBox(BaseDriver):
    element = "//*[name()='path' and contains(@d,'M16 132h41')]"
    textbox = "//span[normalize-space()='Text Box']"
    name_field = "//input[@id='userName']"
    email_field = "//input[@id='userEmail']"
    current_add_field = "//textarea[@id='currentAddress']"
    permanent_add_field = "//textarea[@id='permanentAddress']"
    submit_btn = "//button[@id='submit']"
    details = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/form[1]/div[6]/div[1]"
    # ss_url = "C:\\Users\\Sandz\\PycharmProjects\\DEMO_QA\\screenshot\\"

    def __init__(self, driver):
        self.driver = driver

    def test_element(self):

        # self.driver.find_element(By.XPATH, self.element).click()
        self.find(self.element).click()

    def test_text_box(self):

        self.driver.find_element(By.XPATH, self.textbox).click()
        self.driver.find_element(By.XPATH, self.name_field).send_keys("Sandro")

        self.driver.find_element(By.XPATH, self.email_field).send_keys("sandro@gmail.com")

        self.driver.find_element(By.XPATH, self.current_add_field).send_keys(" NPA")

        self.driver.find_element(By.XPATH, self.permanent_add_field).send_keys("NPA")

        self.page_scroll()

        self.driver.find_element(By.XPATH, self.submit_btn).click()

        field = self.driver.find_element(By.XPATH, self.details).text
        if "Sandro" not in field:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url + "text box.png")
            assert True




