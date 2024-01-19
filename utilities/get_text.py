import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class get_text():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        open_tab_element = driver.find_element(By.ID, "opentab")
        element_text = open_tab_element.text
        print("Text on the element is: " + element_text)
        time.sleep(2)

        driver.quit()


ff = get_text()
ff.test()