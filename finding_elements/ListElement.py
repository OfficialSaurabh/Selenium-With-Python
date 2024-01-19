import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeServices
from env_file_path import chrome_driver_path


class ListElement():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        chromeservice = ChromeServices(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=chromeservice)
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        element_by_classname = driver.find_elements(By.CLASS_NAME, 'inputs')
        length = len(element_by_classname)
        if element_by_classname is not None:
            print("Size of list : " + str(length))

        element_by_tagname = driver.find_elements(By.TAG_NAME, "h1")
        length2= len(element_by_tagname)
        if element_by_tagname is not None:
            print("Size of the List:" + str(length2))
        time.sleep(5)


run_test = ListElement()
run_test.test()
