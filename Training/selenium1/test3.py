from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://jqueryui.com/datepicker/"
driver.get(url)     
print(driver.title)
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, value="demo-frame"))
date_picker = driver.find_element(By.ID, value="datepicker")
date_picker.click()
dates = driver.find_elements(By.XPATH, value="//table//td")
# print month
print("Month is", driver.find_element(By.CLASS_NAME, value='ui-datepicker-month').text)
# print("Month is", driver.find_element(By.XPATH, value="//span[@class='ui-datepicker-month']").text)
driver.find_element(By.XPATH, value="//a[@title='Next']").click()
dates = driver.find_elements(By.XPATH, value="//table//td")  # if not used, StaleElementReferenceException
print("Selected Month is", driver.find_element(By.CLASS_NAME, value='ui-datepicker-month').text)
for datee in dates:
    if datee.text == "26":
        datee.click()
        break
sleep(2)
print("Selected date is", date_picker.get_attribute('value'))
driver.close()
