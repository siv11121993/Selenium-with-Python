import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get('https://www.freeconferencecall.com/global/pl/login')

# print(driver.get_cookie("country_code"))
print(driver.get_cookies())

driver.add_cookie({
    'name': "OLOLOLOLOLOLO",
    'value': 'FANTAZER'
})

print(driver.get_cookie("OLOLOLOLOLOLO"))
