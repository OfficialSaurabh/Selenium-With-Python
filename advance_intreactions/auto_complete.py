from selenium import webdriver
from selenium.webdriver.common.by import By
import time

baseUrl = "https://www.goibibo.com/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(3)
partial_text = "Del"
text_to_select = "Delhi, India(DEL)"

close_loginpopup = driver.find_element(By.XPATH, "//span[contains (@class, 'logSprite')]")
close_loginpopup.click()
time.sleep(2)

text_element = driver.find_element(By.XPATH, "//div[contains (@class, 'fswFld')]" )
time.sleep(2)
text_element.click()

input_box = driver.find_element(By.XPATH, "//input[@type ='text']")
input_box.send_keys(partial_text)
time.sleep(2)

ul_element = driver.find_element(By.ID, "autoSuggest-list")
inner_html = ul_element.get_attribute("innerHTML")

li_elements = ul_element.find_elements(By.TAG_NAME, "li")

for li in li_elements:
    # print(li.text)
    if text_to_select in li.text:
        print("Selected" + li.text)
        li.click()
        break


time.sleep(2)
driver.quit()