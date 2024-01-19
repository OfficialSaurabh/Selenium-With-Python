from selenium import webdriver
class RunFFTestes():
    def test(self):
        driver = webdriver.Firefox()

        driver.get("https://www.letskodeit.com")


ff = RunFFTestes()
ff.test()

