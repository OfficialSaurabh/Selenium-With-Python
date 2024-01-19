import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class drop_down():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        element = driver.find_element(By.ID, "carselect")
        select = Select(element)


        select.select_by_value("benz")
        print("Selected benz")
        time.sleep(2)

        select.select_by_index(2)
        print("Selected Honda")
        time.sleep(2)

        select.select_by_visible_text("BMW")
        print("Selected bmw")
        time.sleep(2)

        select.select_by_index(2)
        print("Selected Honda")
        time.sleep(2)

        driver.quit()


ff = drop_down()
ff.test()