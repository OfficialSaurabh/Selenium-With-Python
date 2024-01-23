from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class PopUp_Model():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        driver.find_element(By.ID, "name").send_keys("Saurabh")
        time.sleep(2)
        driver.find_element(By.ID, "alertbtn").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Test")
        driver.find_element(By.ID, "confirmbtn").click()
        time.sleep(2)

        alert2 = driver.switch_to.alert
        alert2.dismiss()

ff = PopUp_Model()
ff.test()
