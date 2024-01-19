import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handy_wrapper import HandyWrapper
class UsingWrapper():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        hw = HandyWrapper(driver)

        text_field1 = hw.getElement("name")
        text_field1.send_keys("test")
        time.sleep(2)

        text_field2 = hw.getElement("//input[@id='name']", locator_type="xpath")
        text_field2.clear()
        text_field2.send_keys("test2")
        time.sleep(1)
        driver.quit()


ff = UsingWrapper()
ff.test()