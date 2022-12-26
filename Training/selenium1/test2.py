from selenium import webdriver

from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/autocomplete/")
driver.implicitly_wait(5)

driver.switch_to.frame(0)
inputField = driver.find_element(By.ID, "tags")
userInput = input("Enter a substring: ")
inputField.send_keys(userInput)
sleep(4)
suggestions = driver.find_elements(By.XPATH, "//ul/li")
for i in suggestions:
    print(suggestions.index(i)+1, ". ", i.text)
suggestions[3].click()
driver.close()
