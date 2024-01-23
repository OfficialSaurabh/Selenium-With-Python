from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://imgbb.com/upload")

driver.find_element(By.ID, "anywhere-upload-input-camera").send_keys("D:\\ScreenShot_Selenium\\test.png")
time.sleep(3)

driver.quit()

