import time


from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from Tools.function import BaseDriver
from faker import Faker
import random


class PracticeFormPage(BaseDriver):

    form_icon = "//div[@class='home-body']//div[2]//div[1]//div[2]//*[name()='svg']"
    form_module = "//span[normalize-space()='Practice Form']"
    f_name = "//input[@id='firstName']"
    l_name = "//input[@id='lastName']"
    email = "//input[@id='userEmail']"
    mobile_num = "//input[@id='userNumber']"
    dobs = "//input[@id='dateOfBirthInput']"
    upload_picture = "//input[@id='uploadPicture']"
    current_add = "//textarea[@id='currentAddress']"
    select_state = "//div[contains(@class,'css-1pahdxg-control')]//div[contains(@class,'css-1hwfws3')]"
    x = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/form[1]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]"
    select_city = "//div[contains(text(),'Select City')]"
    submit = "//button[@id='submit']"
    subject = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/form[1]/div[6]/div[2]/div[1]/div[1]"
    y = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/form[1]/div[6]/div[2]/div[1]/div[1]"
    z = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/form[1]/div[6]/div[2]/div[1]/div[1]/div[1]"
    i = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/form[1]/div[6]/div[2]/div[1]/div[1]/div[1]/div[1]"
    j = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/form[1]/div[6]/div[2]/div[1]"

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        return element

    def wait_visibility(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return element

    def wait(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
        return element

    def stale_elements(self, locator):
        try:
            element = self.find(locator)
            return element
        except StaleElementReferenceException:
            element = self.find(locator)
            return element

    def stale_element(self, locator, max_attempts=5,):
        for attempt in range(max_attempts):
            try:
                element = self.find(locator)
                element.send_keys("Math")
                return True  # Operation successful
            except StaleElementReferenceException:
                print(f"StaleElementReferenceException - Attempt {attempt + 1}")

        print("Exceeded maximum attempts. Operation unsuccessful.")
        return False

    def select_random_hobbies(self):
        hobbies = ["Sports", "Reading", "Music"]
        num_hobbies = random.randint(1, len(hobbies))
        selected_hobbies = random.sample(hobbies, num_hobbies)
        for hobby in selected_hobbies:
            hobby_radio = self.find(f"//label[text()='{hobby}']")
            hobby_radio.click()

    def test_forms(self):
        self.find(self.form_icon).click()
        self.wait(self.form_module).click()
        time.sleep(5)

    def test_student_info(self):
        faker = Faker()

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()

        self.find(self.f_name).send_keys(first_name)
        self.find(self.l_name).send_keys(last_name)
        self.find(self.email).send_keys(email)
        time.sleep(2)

    def test_random_gender(self):
        gender = random.choice(["Male", "Female", "Other"])
        self.find(f"//label[text()='{gender}']").click()
        time.sleep(2)

    def test_random_mobile(self):
        faker = Faker()
        mobile_number = faker.random_number(11)
        self.find(self.mobile_num).send_keys(mobile_number)
        time.sleep(2)

    def test_random_dob(self):
        self.find(self.dobs).click()
        self.find("//div[@aria-label='Choose Thursday, November 30th, 2023']").click()
        time.sleep(2)

    def test_random_subject(self):
        self.stale_elements(self.i).send_keys("Math", Keys.ENTER)

        time.sleep(10)
        self.driver.quit()

    def test_random_hobbies(self):
        self.select_random_hobbies()

    def upload_pic(self):
        self.find(self.upload_picture).send_keys("C:\\Users\\Sandz\\Pictures\\download (1).jfif")

    def address(self):
        faker = Faker()
        current_address = faker.address()
        self.find(self.current_add).send_keys(current_address)

    def select_state_and_city(self):
        state_dropdown = Select(self.find(self.select_state))
        state_dropdown.select_by_visible_text("NCR")

        city_dropdown = Select(self.find(self.select_city))
        city_dropdown.select_by_visible_text("Delhi")

    def submits(self):
        self.find(self.submit).click()











