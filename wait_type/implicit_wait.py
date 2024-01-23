import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class ImplicitWait():
    def test(self):
        baseUrl = "https://www.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        #Login to the website How to type and click on a web element
        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        email_filed = driver.find_element(By.ID, "email")
        email_filed.send_keys("saurabh@mailinator.com")

ff = ImplicitWait()
ff.test()
