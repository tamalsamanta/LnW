import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)

#Ques1
driver.get("https://www.google.com")
# els = driver.find_elements(By.XPATH, '//a')
# print(len(els))
# for el in els:
#     print(el.text)
#     print(el.get_attribute('href'))

assert driver.title == "Yahoo", "Assertion Error message here"
driver.close()


#=================================================================================================
