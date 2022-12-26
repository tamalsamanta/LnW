import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe") --selenium3
# driver = webdriver.Chrome(ChromeDriverManager().install()) --Selenium3 --certificate issues
# driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install())) 
# --selenium4 --certificate issues
from selenium.webdriver.support.wait import WebDriverWait

service = ChromeService(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)

#=========================================================================
# driver.get("https://opensource-demo.orangehrmlive.com")

# # driver.find_element(By.NAME, 'username').send_keys('Admin')
# # driver.find_element(By.NAME, 'password').send_keys('admin123')
# # driver.find_element(By.ID, 'btnLogin').click()

# acc_title = driver.title
# exp_title = 'OrangeHRM'

# if acc_title == exp_title:
#     print('Login Test Passed')
# else:
#     print('Login Test Failed')

# driver.quit()

#============================================================================

driver.get("https://www.google.com")
driver.maximize_window()

searchbox = driver.find_element(By.NAME,'q')
searchbox.send_keys("Selenium")
searchbox.submit()

driver.implicitly_wait(0.5) #runs for every line after this line. max wait is parameterized.
WebDriverWait(driver, 10) #works like impl but defined explicitly and has more functions n exc handling

el = driver.find_element(By.XPATH, "//h3[text()='Selenium']")
el.click()

time.sleep(10) #meh

driver.close()