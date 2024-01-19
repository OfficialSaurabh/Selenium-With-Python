from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeServices
from env_file_path import chrome_driver_path


class FindByLinkText():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        chromeservice = ChromeServices(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=chromeservice)
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        element_by_linktext = driver.find_element(By.LINK_TEXT, "HOME")
        if element_by_linktext is not None:
            print("Element Found By LinkText")

        element_by_partiallinktext = driver.find_element(By.PARTIAL_LINK_TEXT, "COURSES")
        if element_by_partiallinktext is not None:
            print("Element Found By Partial LinkText")

run_test = FindByLinkText()
run_test.test()
