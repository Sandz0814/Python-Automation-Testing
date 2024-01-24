import time
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BaseDriver:

    ss_url = "C:\\Users\\Change Me\\PycharmProjects\\Python-Automation-Testing\\screenshot\\"
    ss_url_afw = "C:\\Users\\Change Me\\PycharmProjects\\Python-Automation-Testing\\screenshot_afw\\"
    ss_url_widget = "C:\\Users\\Change Me\\PycharmProjects\\Python-Automation-Testing\\screenshot_widget\\"
    ss_url_interaction = "C:\\Users\\Change Me\\PycharmProjects\\Python-Automation-Testing\\screenshot_interaction\\"
    ss_url_bookstore = "C:\\Users\\Change Me\\PycharmProjects\\Python-Automation-Testing\\screenshot_bookstore\\"

    def __int__(self, driver):
        self.driver = driver

    def close(self):
        close = self.driver.close()
        return close

    def s_shot(self, url, picture):
        image = self.driver.save_screenshot(url + picture)
        return image

    def find(self, locator):
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        wait.until(EC.element_to_be_clickable((By.XPATH, locator)))

        elements = self.driver.find_element(By.XPATH, locator)
        x = self.driver.execute_script("arguments[0].scrollIntoView();", elements)
        return x

    def page_scroll(self):
        scroll_pause_time = 0.5

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        # infinite loading like FB
        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(scroll_pause_time)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def wait_presence(self, locator_type, locator):
        list_of_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def wait_clickable(self, locator_type, locator):
        elements = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((locator_type, locator)))
        return elements

    def find_wait(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        return wait

    def screenshot_image_display(self, locator, image_name):
        ss_url = "C:\\Users\\Change Me\\PycharmProjects\\Python-Automation-Testing\\screenshot\\"
        image_name = ""

        try:
            element = self.driver.find_element(By.XPATH, locator)
            if element:
                self.driver.save_screenshot(f'{ss_url}{image_name}.png')

                assert True
            else:
                assert False
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
            assert False

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


