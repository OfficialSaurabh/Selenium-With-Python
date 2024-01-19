import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class radio_checkbox():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        bmwRadioBtn = driver.find_element(By.ID, "bmwradio")
        bmwRadioBtn.click()
        time.sleep(2)

        benzRadioBtn = driver.find_element(By.ID, "benzradio")
        benzRadioBtn.click()
        time.sleep(2)

        hondaRadioBtn = driver.find_element(By.ID, "hondaradio")
        hondaRadioBtn.click()
        time.sleep(2)

        bmwCheckbox = driver.find_element(By.ID, "bmwcheck")
        bmwCheckbox.click()
        time.sleep(2)



        benzCheckbox = driver.find_element(By.ID, "benzcheck")
        benzCheckbox.click()
        time.sleep(2)

        hondaCheckbox = driver.find_element(By.ID, "hondacheck")
        hondaCheckbox.click()
        time.sleep(2)

        print("Bmw radio button is selected: " + str(bmwRadioBtn.is_selected()))
        print("Benz radio button is selected: " + str(benzRadioBtn.is_selected()))
        print("Honda radio button is selected: " + str(hondaRadioBtn.is_selected()))
        print("Bmw checkbox is selected: " + str(bmwCheckbox.is_selected()))
        print("Benz checkbox is selected: " + str(benzCheckbox.is_selected()))
        print("Honda checkbox is selected: " + str(hondaCheckbox.is_selected()))

        driver.quit()

ff = radio_checkbox()
ff.test()

