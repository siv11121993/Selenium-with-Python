import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://demoqa.com/text-box')

time.sleep(5)

click_button = driver.find_element('xpath', "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p")
click_button.click()
time.sleep(5)

name_field = driver.find_element('xpath', "//input[@id='userName']")
name_field.send_keys('Ivan Sauchuk')

time.sleep(3)

# email_field.clear()
# time.sleep(3)
#
# email_field.send_keys('goida')
#
# time.sleep(3)
