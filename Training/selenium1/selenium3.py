import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://cookbook.seleniumacademy.com/Alerts.html")
driver.find_element(By.XPATH, '//*[@id="confirm"]').click()
alert = driver.switch_to.alert
alert_message = alert.text
print(alert_message)
time.sleep(5)
alert.accept()
# driver.save_screenshot("../screenshots/sample.png")
driver.close()