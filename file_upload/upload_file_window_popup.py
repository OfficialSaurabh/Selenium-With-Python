from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://imgbb.com/upload")

driver.find_element(By.XPATH, "//a[contains (text(), 'browse from your computer')]").click()

time.sleep(3)

keyword = Controller()
keyword.type("D:\\ScreenShot_Selenium\\test.png")
keyword.press(Key.enter)
keyword.release(Key.enter)
time.sleep(3)


driver.quit()