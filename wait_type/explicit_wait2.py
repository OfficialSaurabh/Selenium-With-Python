from selenium import webdriver
from selenium.webdriver.common.by import By
from wait_type.explicit_wait_type import ExplicityWait

import time

class ExplicitWait12():
    def test(self):
        baseUrl = "https://www.letskodeit.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        wait =  ExplicityWait(driver)
        element = wait.wait_for_element(locator="//a[@href='/login']", locator_type="xpath")
        element.click()
        time.sleep(2)

        driver.quit()

ff = ExplicitWait12()
ff.test()