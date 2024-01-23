from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ScrollView():
    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://www.letskodeit.com/practice")
        driver.implicitly_wait(2)

        #Scroll to the bottom
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(2)

        #Scroll to the top
        driver.execute_script("window.scrollBy(0, -600);")
        time.sleep(2)

        # Scroll Element Into View
        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -150);")

        #Scroll native way to element
        driver.execute_script("window.scrollBy(0, -600);")
        location = element.location_once_scrolled_into_view
        print("Element location: " + str(location))
        time.sleep(2)

        driver.quit()


ff = ScrollView()
ff.test()