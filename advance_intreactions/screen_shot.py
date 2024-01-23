from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ScreenShot():
    def test(self):
        baseUrl = "https://www.letskodeit.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        driver.find_element(By.ID, "email").send_keys("abc@email.com")
        driver.find_element(By.ID, "login-password").send_keys("test")
        driver.find_element(By.ID, "login").click()
        destination_file_name = "D:\\ScreenShot_Selenium\\test.png"
        time.sleep(2)

        try:
            driver.save_screenshot(destination_file_name)
            print("Screenshot saved" + destination_file_name)

        except NotADirectoryError:
            print("Not a directory error")
        driver.quit()


ff = ScreenShot()
ff.test()