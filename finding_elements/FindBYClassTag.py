import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeServices
from env_file_path import chrome_driver_path


class FindByClassTag():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        chromeservice = ChromeServices(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=chromeservice)
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        element_by_classname = driver.find_element(By.CLASS_NAME, "inputs")
        if element_by_classname is not None:
            print("Element Found By Class Name")
            element_by_classname.send_keys("Testing")

        element_by_tagname = driver.find_element(By.TAG_NAME, "a")
        if element_by_tagname is not None:
            print("Element Found By Tag Name" + element_by_tagname.text)

        time.sleep(5)

run_test = FindByClassTag()
run_test.test()
