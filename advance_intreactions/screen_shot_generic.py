from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from advance_intreactions.auto_complete import driver


# from advance_intreactions.auto_complete import driver


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
        time.sleep(2)
        self.TakeScreenShot(driver)
        driver.quit()




    def TakeScreenShot(self, driver):
        file_name = str(round(time.time() * 1000)) + ".png"
        screen_shot_path ="D:\\ScreenShot_Selenium"
        destination_file = screen_shot_path + file_name
        try:
            driver.save_screenshot(destination_file)
            print("Screenshot saved" + destination_file)
        except NotADirectoryError:
            print("Not a directory error")




ff = ScreenShot()
ff.test()