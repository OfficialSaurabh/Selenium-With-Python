import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class workingwith_element_list():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        radios = driver.find_elements(By.XPATH, "//input[@type='radio']")

        size = len(radios)
        print("Size of the list is: " + str(size))

        for radio in radios:
            isSelected = radio.is_selected()
            print("Radio is selected: " + str(isSelected))
            if not isSelected:
                radio.click()
                time.sleep(3)

        driver.quit()

ff = workingwith_element_list()
ff.test()
