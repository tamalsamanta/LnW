from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/slider/")
driver.implicitly_wait(5)
slider = driver.find_element(By.XPATH, "//div[@id='slider']/span")
act = ActionChains(driver)
act.click_and_hold(slider).move_by_offset(200,0).release().perform()
sleep(5)

driver.close()