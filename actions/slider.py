from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class Slider():
    def test(self):
        baseUrl = "https://jqueryui.com/slider/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        driver.switch_to.frame(0)

        element = driver.find_element(By.XPATH, "//div[@id='slider']/span")
        time.sleep(2)
        try:
            action = ActionChains(driver)
            action.drag_and_drop_by_offset(element, 100, 0).perform()
            print("Sliding Element Successful")
            time.sleep(2)
        except:
            print("Sliding Failed")

        driver.quit()

ff = Slider()
ff.test()
