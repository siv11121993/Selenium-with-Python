import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

SELECT_LOCATOR = ("xpath", "//select[@id='dropdown']")
driver.get('http://the-internet.herokuapp.com/dropdown')
DROPDOWN = Select(driver.find_element(*SELECT_LOCATOR))
time.sleep(2)

DROPDOWN.select_by_value('1')
time.sleep(2)

DROPDOWN.select_by_value('2')
time.sleep(2)
