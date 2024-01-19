import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class clickAndSendKey():
    def test(self):
        baseUrl = "https://www.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        loginlink = driver.find_element(By.XPATH, "//a[@href='/login']" )
        loginlink.click()
        emailfield = driver.find_element(By.ID, "email")
        emailfield.send_keys("test")

        passwordfield =driver.find_element(By.ID, "login-password")
        passwordfield.send_keys("test")
        time.sleep(3)
        emailfield.clear()

        time.sleep(3)

        emailfield.send_keys("test")


ff = clickAndSendKey()
ff.test()