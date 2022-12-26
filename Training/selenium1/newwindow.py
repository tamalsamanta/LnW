from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from time import sleep

PATH = "C:\Drivers\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://login.yahoo.com")

privacy = driver.find_element(By.CLASS_NAME, 'privacy')
privacy.click()

sleep(3)
driver.switch_to.window(driver.window_handles[0])
driver.close()

driver.switch_to.window(driver.window_handles[0])

element = driver.find_element(By.PARTIAL_LINK_TEXT, "feedback form")

sleep(2)

actions = ActionChains(driver=driver)
actions.scroll_to_element(element).perform()
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

driver.close()