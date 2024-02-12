import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

CHECKBOX_1 = ("xpath", ("//input[@type='checkbox'][1]"))
CHECKBOX_2 = ("xpath", ("//input[@type='checkbox'][2]"))

driver.get('http://the-internet.herokuapp.com/checkboxes')
time.sleep(5)
driver.find_element(*CHECKBOX_1).click()
time.sleep(5)

driver.find_element(*CHECKBOX_2).click()
time.sleep(90)
