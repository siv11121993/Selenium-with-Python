import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=service)
service = Service(executable_path=ChromeDriverManager().install())

driver.get('https://hyperskill.org/tracks')

time.sleep(3)

driver.find_elements('class name', 'nav-link')[3].click()

time.sleep(5)
