from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeServices

from env_file_path import chrome_driver_path


class FindByXpath():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        chromeservice = ChromeServices(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=chromeservice)
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        element_by_xpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        if element_by_xpath is not None:
            print("Element Found By XPATH")

        element_by_css = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
        if element_by_css is not None:
            print("Element Found By CSS")


run_test = FindByXpath()
run_test.test()
