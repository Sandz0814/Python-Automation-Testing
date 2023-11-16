from selenium.webdriver.common.by import By
from Tools.function import BaseDriver


class WebTablePage(BaseDriver):

    web_table_btn = "//span[normalize-space()='Web Tables']"
    add_btn = "//button[@id='addNewRecordButton']"
    f_name = "//input[@id='firstName']"
    l_name = "//input[@id='lastName']"
    email = "//input[@id='userEmail']"
    age = "//input[@id='age']"
    salary = "//input[@id='salary']"
    department = "//input[@id='department']"
    add_submit_btn = "//button[@id='submit']"
    table_column = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]"
    web_tables_text = "//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]"
    search_filter = "//input[@id='searchBox']"
    find_search = "//span[@id='basic-addon2']//span//*[name()='svg']"
    edit_btn = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]/span[1]"
    delete_btn = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]/span[2]"
    pagination = "//input[@aria-label='jump to page']"
    page_row = "//select[@aria-label='rows per page']"

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        return element

    def test_web_table_add_employee(self):
        self.find_element(self.web_table_btn).click()
        self.find_element(self.add_btn).click()
        self.find_element(self.f_name).send_keys("Sandro")
        self.find_element(self.l_name).send_keys("Jimena")
        self.find_element(self.email).send_keys("Sandro@gmail.com")
        self.find_element(self.age).send_keys("44")
        self.find_element(self.salary).send_keys("50000")
        self.find_element(self.department).send_keys("Q.A")
        self.find_element(self.add_submit_btn).click()
        add_employee = self.find_element(self.web_tables_text).text
        if "Web Tables" not in add_employee:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url + "Add employee.png")
            assert True

    def test_search_employee(self):
        self.find_element(self.search_filter).send_keys("Sandro")
        search_employee = self.find_element(self.table_column).text
        if "Sandro" not in search_employee:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url + "Search employee.png")
            assert True

    def test_edit_employee(self):
        self.find_element(self.edit_btn).click()
        self.find_element(self.f_name).clear()
        self.find_element(self.f_name).send_keys("Drigo Bato")
        self.find_element(self.add_submit_btn).click()
        search_employee = self.find_element(self.table_column).text
        if "Drigo Bato" not in search_employee:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url + "Edit employee.png")
            assert True

    def test_delete_employee(self):
        self.find_element(self.search_filter).clear()
        self.find_element(self.search_filter).send_keys("Drigo")
        self.find_element(self.delete_btn).click()
        self.find_element(self.search_filter).clear()
        add_employee = self.find_element(self.web_tables_text).text
        if "Web Tables" not in add_employee:
            assert False
        else:
            self.driver.save_screenshot(self.ss_url + "Delete employee.png")
            assert True










