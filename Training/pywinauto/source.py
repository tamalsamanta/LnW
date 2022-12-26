from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
sleep(3)

driver.switch_to.new_window('tab')
driver.get('https://demoqa.com/droppable')
driver.maximize_window()
dragged = driver.find_element(By.ID, "draggable")
dropped = driver.find_element(By.ID, "droppable")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
actions = ActionChains(driver=driver, duration=250)
actions.click_and_hold(dragged).release(dropped).perform()
sleep(3)
driver.quit()