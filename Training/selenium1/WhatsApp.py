from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

service = Service(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:6969")

# "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" -remote-debugging-port=9014 --user-data-dir="C:\test\Chrome_Test_Profile"

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://web.whatsapp.com")
driver.maximize_window()

driver.implicitly_wait(30)

searchBox = driver.find_element(By.CLASS_NAME, "_13NKt")
searchBox.send_keys("ninu")
searchBox.send_keys(Keys.ENTER)

textBox = driver.find_element(By.CLASS_NAME, "p3_M1")
textBox.send_keys('Test Text')
textBox.send_keys(Keys.ENTER)