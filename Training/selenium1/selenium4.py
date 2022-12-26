
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# serv_obj = Service()
from selenium.webdriver.common.by import By

service = Service(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://cookbook.seleniumacademy.com/Frames.html")

all_frames = driver.find_elements(by='tag name', value='frame')
for frame in all_frames:
    driver.switch_to.frame(frame)
    print(driver.page_source)
    if "This Frame doesn't have id or name" in driver.page_source:
        print("reached second frame using contents")
        # break
    else:
        driver.switch_to.default_content()
    driver.switch_to.default_content()
    print("reached parent page")

# req_frame = driver.find_element(By.XPATH, '//frame[@name="right"]')
# driver.switch_to.frame("right")

# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@name='right']")))



# driver.find_element(By.XPATH, '//frame[contains(@src, "frame_c")]') #using feame element
# driver.switch_to.frame("right")  # using id
# driver.switch_to.frame(driver.find_element(By.XPATH, '//frame[@name="right"]'))
# para = driver.find_element(By.TAG_NAME, "p")
# print(para.text)
# driver.switch_to.default_content()  # switching to the parent page

# driver.find_element(By.XPATH, '//iframe/a[@id="follow-button"]').click()

# driver.find_element(By.XPATH, '//span[contains(text(),"No, thanks")]').click()

driver.save_screenshot("./screenshots/sample.png")
driver.quit()


