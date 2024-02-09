import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()

prefs = {
    'download.default_directory': f'{os.getcwd()}/lesson_6'
}
chrome_options.add_experimental_option('prefs', prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
start_time = time.time()

driver.get('https://the-internet.herokuapp.com/download')
time.sleep(5)
for i in range(1, 20):
    driver.find_elements('xpath', '//a')[i].click()

time.sleep(5)
