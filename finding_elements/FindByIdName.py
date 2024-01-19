from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeServices

from env_file_path import chrome_driver_path


class FindByIdName():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        chromeservice = ChromeServices(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=chromeservice)
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        element_by_id = driver.find_element(By.ID, "displayed-text")
        if element_by_id is not None:
            print("Element Found By Id")

        element_by_name = driver.find_element(By.NAME, "show-hide")
        if element_by_name is not None:
            print("Element Found By Name")


run_test = FindByIdName()
run_test.test()
