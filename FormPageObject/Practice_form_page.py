import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    select_state = "//div[@id='state']"
    selected_state = "//div[contains(text(),'Uttar Pradesh')]"
    x = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/form[1]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]"
    select_city = ("//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/div[2]/form"
                   "[1]/div[10]/div[3]/div[1]/div[1]/div[2]/div[1]/*[1]")
    selected_city = "//div[contains(text(),'Agra')]"
    submit = "//button[@id='submit']"
    confirmation_btn = '//*[@id="closeLargeModal"]'
    confirmation_text = '//*[@id="example-modal-sizes-title-lg"]'
    subject_input = "//input[@id='subjectsInput']"

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
        time.sleep(1)

    def test_random_gender(self):
        gender = random.choice(["Male", "Female", "Other"])
        self.find(f"//label[text()='{gender}']").click()
        time.sleep(1)

    def test_random_mobile(self):
        faker = Faker()
        mobile_number = faker.random_number(11)
        self.find(self.mobile_num).send_keys(mobile_number)
        time.sleep(5)

    def test_random_dob(self):
        self.find(self.dobs).click()
        self.find("//div[@aria-label='Choose Tuesday, January 30th, 2024']").click()
        time.sleep(2)

    def test_random_subject(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, self.subject_input)))
        # Locate the autocomplete input field by its xpath
        autocomplete_input = self.driver.find_element(By.XPATH, self.subject_input)
        # Enter a value into the input field
        autocomplete_input.send_keys("Mat")
        autocomplete_input.send_keys(Keys.ENTER)
        autocomplete_input.send_keys("Sci")
        autocomplete_input.send_keys(Keys.ENTER)
        autocomplete_input.send_keys("Eng")
        autocomplete_input.send_keys(Keys.ENTER)

    def test_random_hobbies(self):
        self.select_random_hobbies()
        time.sleep(2)

    def test_upload_pic(self):
        self.find(self.upload_picture).send_keys("C:\\Users\\Change Me\\Pictures\\sinag.jpg")

    def test_address(self):
        faker = Faker()
        current_address = faker.address()
        self.find(self.current_add).send_keys(current_address)
        time.sleep(2)

    def test_select_state_and_city(self):
        self.find(self.select_state).click()
        self.find(self.selected_state).click()
        time.sleep(2)
        self.find(self.select_city).click()
        self.find(self.selected_city).click()


    def test_submits(self):
        self.find(self.submit).click()
        time.sleep(2)

    def test_confirmation(self):
        confirm = self.find(self.confirmation_text).text
        if "Thanks for submitting the form" not in confirm:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url + "Form submit confirmation.png")
            assert True

        self.find(self.confirmation_btn).click()

        time.sleep(1)
        self.page_scroll()
        self.driver.close()












