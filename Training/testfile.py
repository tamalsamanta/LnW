from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

from selenium.webdriver.common.by import By

service = Service(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.spicejet.com")
sleep(2)
print(driver.title)

inputField = driver.find_elements(By.CLASS_NAME, "css-1cwyjr8")
fromField = inputField[0]
toField = inputField[1]

fromField.click()
sleep(1)
fromField.send_keys("CCU")
sleep(1)
toField.send_keys("BOM")
sleep(3)
driver.find_element(By.XPATH, "").click()

driver.quit()
