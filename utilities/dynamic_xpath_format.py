from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from handy_wrapper import HandyWrapper

class DynamicXpathFormat():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        #Login to the website How to type and click on a web element
        driver.find_element(By.LINK_TEXT, "Sign In").click()
        email = driver.find_element(By.ID, "email")

        driver.quit()