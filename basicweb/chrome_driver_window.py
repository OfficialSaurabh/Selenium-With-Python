from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeServices
from finding_elements.env_file_path import chrome_driver_path


class RunChromeTestes():
    def test(self):
        chromeservice = ChromeServices()
        driver = webdriver.Chrome(service=chromeservice)

        driver.get("https://www.letskodeit.com")


chromeruntests = RunChromeTestes()
chromeruntests.test()

