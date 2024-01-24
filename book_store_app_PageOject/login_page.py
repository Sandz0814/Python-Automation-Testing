import time
from selenium.webdriver.common.alert import Alert
from Tools.function import BaseDriver
from faker import Faker
import random


class Register(BaseDriver):

    book_store_app = "//div[6]//div[1]//div[2]//*[name()='svg']"
    login_tab = "//span[normalize-space()='Login']"
    header = "//div[@class='main-header']"

    new_user_btn = "//button[@id='newUser']"
    f_name = "//input[@id='firstname']"
    l_name = "//input[@id='lastname']"
    user_name = "//input[@id='userName']"
    pass_word = "//input[@id='password']"
    captcha = "//div[@class='recaptcha-checkbox-border']"
    register = "//button[@id='register']"
    back_login_btn = "//button[@id='gotologin']"
    login_btn = "//button[@id='login']"
    profile_name = "//label[@id='userName-value']"

    def __init__(self, driver):
        self.driver = driver

    def test_open_book_store_app(self):
        self.find_wait(self.book_store_app)
        self.find(self.book_store_app).click()

    def test_open_login_tab(self):
        self.find_wait(self.login_tab)
        self.find(self.login_tab).click()

    def test_header(self):
        headers = self.find(self.header).text
        assert "Login" in headers
        image = "Books Store Login.png"
        self.s_shot(self.ss_url_bookstore, image)

    def test_new_user_tab(self):
        self.find(self.new_user_btn).click()
        headers = self.find(self.header).text
        assert "Register" in headers
        image = "Books Store Register.png"
        self.s_shot(self.ss_url_bookstore, image)

    def test_input_details(self):
        faker = Faker()
        first_name = faker.first_name()
        last_name = faker.last_name()
        username = faker.user_name()
        password = faker.password()

        self.find(self.f_name).send_keys(first_name)
        self.find(self.l_name).send_keys(last_name)
        self.find(self.user_name).send_keys(username)
        self.find(self.pass_word).send_keys(password)

        print("Please click the captcha, then press enter")
        time.sleep(20)
        self.find(self.register).click()
        time.sleep(2)

    def test_login(self):
        # self.find(self.f_name).send_keys("Drigo")
        # self.find(self.l_name).send_keys("Bato")
        self.find(self.back_login_btn).click()
        self.find(self.user_name).send_keys("Drigong Bato08")
        self.find(self.pass_word).send_keys("Drigo123*")
        self.find(self.login_btn).click()

    def test_assert_profile(self):

        profile = self.find(self.profile_name).text
        assert "Drigong Bato08" in profile
        image = "Profile Name.png"
        self.s_shot(self.ss_url_bookstore, image)





















