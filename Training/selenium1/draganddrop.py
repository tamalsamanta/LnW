from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

service = Service(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://demoqa.com/droppable')

dragged = driver.find_element(By.ID, "draggable")
dropped = driver.find_element(By.ID, "droppable")

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
actions = ActionChains(driver=driver, duration=250)
actions.click_and_hold(dragged).release(dropped).perform()

sleep(3)
driver.quit()