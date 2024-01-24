from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class DragDrop():
    def test(self):
        baseUrl = "https://jqueryui.com/droppable/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        driver.switch_to.frame(0)

        source = driver.find_element(By.ID, "draggable")
        target = driver.find_element(By.ID, "droppable")
        time.sleep(2)

        try:
            action = ActionChains(driver)
            # action.drag_and_drop(source, target).perform()
            # Action chains actions
            action.click_and_hold(source).pause(1).move_to_element(target).pause(1).release().perform()
            print("Drag and Drop Successful")
            time.sleep(2)
        except:
            print("Element not found")

        driver.quit()

ff = DragDrop()
ff.test()