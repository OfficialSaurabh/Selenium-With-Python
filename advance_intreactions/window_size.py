from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WindowSize():
    def test(self):
        driver = webdriver.Firefox()
        driver.get(" https://www.letskodeit.com")
        driver.implicitly_wait(2)

        height = driver.get_window_size()["height"]
        width = driver.get_window_size()["width"]
        print("Height: " + str(height))
        print("Width: " + str(width))
        print(driver.get_window_size())
        driver.quit()


ff = WindowSize()
ff.test()