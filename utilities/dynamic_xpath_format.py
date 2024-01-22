import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class DynamicXpathFormat():
    def test(self):
        baseUrl = "https://www.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        #Login to the website How to type and click on a web element
        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        email = driver.find_element(By.ID, "email")
        email.send_keys("saurabh@mailinator.com")
        password = driver.find_element(By.ID, "login-password")
        password.send_keys("Indus@12")
        driver.find_element(By.ID, "login").click()
        time.sleep(3)

        courses = driver.find_element(By.XPATH, "//a[@href='/courses']")
        courses.click()

        search_box = driver.find_element(By.XPATH, "//input[@id='search']")
        search_box.send_keys("JavaScript")


        # course = "//div[@class='zen-course-list']//h4[contains (@class, 'dynamic-heading') and contains (text(), 'Cypress.io Test Automation')]"
        course = "//div[@class='zen-course-list']//h4[contains (@class,'dynamic-heading') and contains (text(),'{0}')]"
        course_locator = course.format("JavaScript for beginners")
        course_element = driver.find_element(By.XPATH, course_locator)
        course_element.click()
        time.sleep(2)

        driver.quit()


ff = DynamicXpathFormat()
ff.test()