from selenium import webdriver
from selenium.webdriver.common.by import By

class elementstate():
    def test(self):
        baseUrl = "https://google.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)
        e1 = driver.find_element(By.ID, "APjFqb")
        e1.send_keys("letskodeit")
        e1state = e1.is_enabled()
        print("E1 is Enabled:" + str(e1state))
        driver.quit()


ff = elementstate()
ff.test()