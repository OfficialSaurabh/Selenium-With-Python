from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToIframe():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

        # Switch to frame using id
        driver.switch_to.frame("courses-iframe")

        # Switch to frame using name

        # Switch to frame using numbers
        time.sleep(2)

        # Search Course
        driver.find_element(By.XPATH, "//input[@id='search']").send_keys("python")
        time.sleep(2)

        # Switch back to the parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("test")


ff = SwitchToIframe()
ff.test()
