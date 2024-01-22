from traceback import print_stack
from utilities.handy_wrapper import HandyWrapper
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicityWait():
    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrapper(driver)

    def wait_for_element(self, locator, locator_type="id", timeout=10, poll_frequency=0.5):
        element = None
        try:
            by_type = self.hw.getByType(locator_type)
            print("Waiting for maximum :" + str(timeout) + "seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((by_type, locator)))
            print("Element Found")
        except:
            print("Element not found")
            print_stack()
        return element