from selenium.webdriver.common.by import By
class HandyWrapper():
    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "xpath":
            return By.XPATH
        else:
            print("Locator type is not supported")
            return False
    def getElement(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.getByType(locator_type)
            element = self.driver.find_element(by_type, locator)
            print("Element Found")
        except:
            print("Element not found")
        return element

    def isElementPresent(self, locator, by_type):
        try:
            element = self.driver.find_element(by_type, locator)
            if element is not None:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False
    def elementPresenceCheck(self, locator, by_type):
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False


