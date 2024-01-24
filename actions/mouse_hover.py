from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class MouseHover():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(2)

        element = driver.find_element(By.ID, "mousehover")
        item_to_clock = "//div[@class='mouse-hover-content']//a[text()='Top']"
        try:
            action = ActionChains(driver)
            action.move_to_element(element).perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            top_link = driver.find_element(By.XPATH, item_to_clock)
            action.move_to_element(top_link).click().perform()
            print("Clicked on Top link")
        except:
            print("Element not found")
        driver.quit()

ff = MouseHover()
ff.test()