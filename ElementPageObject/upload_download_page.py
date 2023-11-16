import time
from selenium.webdriver.common.by import By
from Tools.function import BaseDriver
import os


class UploadDownloadPage(BaseDriver):

    upload_download_btn = "//span[normalize-space()='Upload and Download']"
    download_btn = "//a[@id='downloadButton']"
    upload_btn = "//input[@id='uploadFile']"
    upload_assert = "//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/p[1]"

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        return element

    def test_upload_download(self):
        self.find(self.upload_download_btn).click()
        time.sleep(1)

    def test_download(self):
        self.find(self.download_btn).click()
        time.sleep(1)
        download_path = "C:\\Users\\Sandz\\Downloads\\"
        file_name = "sampleFile.jpeg"  # Replace with the actual file name

        file_path = os.path.join(download_path, file_name)

        if os.path.exists(file_path):
            print(f"File '{file_name}' was downloaded successfully.")
        else:
            print(f"File '{file_name}' was not found in the download directory.")

    def test_uploads(self):
        self.find(self.upload_btn).send_keys("C:\\Users\\Sandz\\Pictures\\sinag.jpg")
        upload_message = self.find(self.upload_assert).is_displayed()
        if upload_message:
            self.driver.save_screenshot(self.ss_url + "upload.png")
            assert True
        else:
            print("File not uploaded")
            assert False
        time.sleep(1)







