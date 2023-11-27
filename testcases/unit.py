import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://demoqa.com/')
driver.maximize_window()
# driver.execute_script("document.body.style.zoom='40%'")

# time.sleep(20)

inter = driver.find_element(By.XPATH, "//*[name()='path' and contains(@d,'M880 112H1')]")
inter.click()

time.sleep(10)