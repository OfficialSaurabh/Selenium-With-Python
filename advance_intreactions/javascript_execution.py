from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class JavaScript():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.execute_script("window.location = 'https://www.letskodeit.com/practice';")

        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("test")
        driver.quit()
        

ff = JavaScript()
ff.test()