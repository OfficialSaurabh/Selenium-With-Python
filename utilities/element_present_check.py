import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handy_wrapper import HandyWrapper

class ElementPresentCheck():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrapper(driver)
        driver.get(baseUrl)

        element_result = hw.elementPresenceCheck("name", By.ID)
        print(str(element_result))

        element_result2= hw.elementPresenceCheck("//input[@id='name']", By.XPATH)
        print(str(element_result2))
        driver.quit()


ff = ElementPresentCheck()
ff.test()