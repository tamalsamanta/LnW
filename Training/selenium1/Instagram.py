# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# service = Service(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=service)

# driver.get("https://instagram.com")
# element = WebDriverWait(driver, 3)

import numpy as np
import re
x = "derivatives are better than fixed income"
y = re.match(r'(.*) are (.*?) .*',x,re.M|re.I)
if y:
    print ("sun:",y.group())
    print ("run:",y.group(1))
    print ("fun:",y.group(2))
else:
    print("why!")