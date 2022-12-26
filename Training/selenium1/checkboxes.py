from selenium import webdriver

from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/checkboxradio/")
driver.implicitly_wait(5)
driver.execute_script("window.scroll(0,300)")
driver.switch_to.frame(0)
driver.execute_script("window.scroll(0,300)")
driver.find_element(By.XPATH, "//label[@for='checkbox-nested-1']").click()
checkBoxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
totalNoOfCheckboxes = len(checkBoxes)
# for i in range(totalNoOfCheckboxes):
#     checkBoxes[i].click()

# checkBoxes[1].click()
print("Total Checkboxes present: " + totalNoOfCheckboxes)
checkboxesContent = driver.find_elements(By.XPATH, "//input[@type='checkbox']/preceding-sibling::label")
nestedCheckboxContent = driver.find_elements(By.XPATH, "//input[@type='checkbox']/parent::label")
for i in range(4):
    checkboxesContent.append(nestedCheckboxContent[i])
for i in range(totalNoOfCheckboxes):
    if checkBoxes[i].is_selected():
        print("Checkbox:", checkboxesContent[i].text, " is selected")
    else:
        print("Checkbox:", checkboxesContent[i].text, " is not selected")
# driver.find_element(By.ID, "checkbox-nested-1").click()
sleep(5)
driver.close()
