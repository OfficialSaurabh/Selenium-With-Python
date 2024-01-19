from selenium import  webdriver

class BrowserIntreaction():
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()

        #Maximize the browser
        driver.maximize_window()

        #Open the URL
        driver.get(baseUrl)

        #Get the title of the page
        title = driver.title
        print("Title of the page is: " + title)

        #Get current URL
        currentUrl = driver.current_url
        print("Current Url of the page is:" + currentUrl)

        #Browser Refresh
        driver.refresh()
        print("Browser Refreshed")

        #Browser back
        driver.back()
        print("Browser Back")

        #Browser forward
        driver.forward()
        print("Browser Forward")
        driver.get(driver.current_url)

        # Open another URL
        driver.get("https://www.letskodeit.com/courses")
        print("Another URL Opened")


        #Browser Back
        driver.back()
        print("Browser Back")

        #Browser Forward
        driver.forward()
        print("Browser Forward")

        #Browser close
        driver.close()

ff = BrowserIntreaction()
ff.test()