from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SwitchToWindow():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)

        #Find parent handel -> Main Window
        parent_handel = driver.current_window_handle
        print("Parent Handel: " + parent_handel)

        #Find Open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        #Find call handels. there should two handles after clicking open
        handels =driver.window_handles

        #Switch to window and search for courses
        for handel in handels:
            print("Handel:" + handel)
            if handel not in parent_handel:
                driver.switch_to.window(handel)
                print("Switched to " + handel)
                driver.find_element(By.XPATH, "//input[@id='search']").send_keys("python")
                time.sleep(2)
                driver.close()
                break

        #Switch back to the parent handel
        driver.switch_to.window(parent_handel)
        driver.find_element(By.ID, "name").send_keys("test")
        time.sleep(2)


        # handles = driver.window_handles
        # print(handles)
        # driver.switch_to.window(handles[1])
        # driver.find_element(By.ID, "search-courses").send_keys("python")



ff = SwitchToWindow()
ff.test()