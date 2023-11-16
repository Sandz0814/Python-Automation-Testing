import random
import string
from ElementPageObject.webtable_page import WebTablePage
from selenium.webdriver.common.by import By


class YourClassName:
    # Your other class methods and attributes

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        return element

    def test_web_table_add_employee(self, first_name, last_name, email, age, salary, department):
        self.find_element(self.web_table_btn).click()
        self.find_element(self.add_btn).click()
        self.find_element(self.f_name).send_keys(first_name)
        self.find_element(self.l_name).send_keys(last_name)
        self.find_element(self.email).send_keys(email)
        self.find_element(self.age).send_keys(age)
        self.find_element(self.salary).send_keys(salary)
        self.find_element(self.department).send_keys(department)
        self.find_element(self.add_submit_btn).click()


# Create an instance of your class
your_instance = YourClassName()

# Loop 100 times
for _ in range(100):
    # Generate random details
    random_first_name = ''.join(random.choice(string.ascii_letters) for _ in range(5))
    random_last_name = ''.join(random.choice(string.ascii_letters) for _ in range(5))
    random_email = f"{random_first_name}@gmail.com"
    random_age = str(random.randint(18, 65))
    random_salary = str(random.randint(30000, 80000))
    random_department = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))

    # Call the function with random details
    your_instance.test_web_table_add_employee(random_first_name, random_last_name, random_email, random_age, random_salary, random_department)
