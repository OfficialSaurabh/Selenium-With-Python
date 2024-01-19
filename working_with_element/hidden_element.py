import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class hidden_element():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        textbox_element = driver.find_element(By.ID, "displayed-text")
        textbox_element = textbox_element.is_displayed()
        #Exception will be thrown if the element is not displayed
        print("Is Displayed: " + str(textbox_element))
        time.sleep(2)

        #Click the hidden button
        driver.find_element(By.ID, "hide-textbox").click()
        textbox_element = textbox_element.is_displayed()
        print("Is Displayed: " + str(textbox_element))
        time.sleep(2)

        # Click the show button
        driver.find_element(By.ID, "show-textbox").click()
        textbox_element = textbox_element.is_displayed()
        print("Is Displayed: " + str(textbox_element))
        time.sleep(2)

        driver.quit()

    def testExpedia(self):
        baseUrl = "https://www.expedia.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        element = driver.find_element(By.ID, "soft_packages_flight_pill")
        element.click()

        drop_downelement = driver.find_element(By.XPATH, "//button[@aria-label='Leaving from']")
        print("Is Displayed: " + str(drop_downelement.is_displayed()))

        driver.quit()

ff = hidden_element()
# ff.test()
ff.testExpedia()