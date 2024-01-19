import time

from selenium import webdriver
from selenium.webdriver.common.by import By
class GetAttribute():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        attribute_value = driver.find_element(By.ID, "name")
        result = attribute_value.get_attribute("class")
        print("Attribute value is: " + result)
        time.sleep(1)
        driver.quit()


ff = GetAttribute()
ff.test()