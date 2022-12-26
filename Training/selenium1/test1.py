from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/accordion/")
driver.implicitly_wait(5)
driver.switch_to.frame(0)
sections = driver.find_elements(By.XPATH, "//div[@id='accordion']/h3")
totalSections = len(sections)
print("Total sections: %d" % totalSections)
insideSection = driver.find_elements(By.XPATH, "//div[@id='accordion']/div")

for i in range(totalSections):
    sections[i].click()
    print(sections[i].text)
    sleep(2)
    print(insideSection[i].text)

driver.close()