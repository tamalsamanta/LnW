import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)

#Ques2
driver.get('https://login.yahoo.com')
driver.maximize_window()
username = driver.find_element(By.XPATH, '//input[@name="username"]')
username.send_keys('samantamal')
username.submit()
driver.implicitly_wait(5)
password = driver.find_element(By.XPATH, '//input[@name="password"]')
password.send_keys('Admin@123')
password.submit()
login = driver.find_element(By.ID, 'login-signin')
login.click()
time.sleep(3)
driver.close()