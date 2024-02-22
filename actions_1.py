import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

LEFT_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@id='leftClick']")
DOUBLE_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@id='doubleClick']")
RIGHT_CLICK_BUTTON_LOCATOR = ("xpath", "//button[@id='rightClick']")

driver.get("https://testkru.com/Elements/Buttons")

left_button = driver.find_element(*LEFT_CLICK_BUTTON_LOCATOR)
double_button = driver.find_element(*DOUBLE_CLICK_BUTTON_LOCATOR)
right_button = driver.find_element(*RIGHT_CLICK_BUTTON_LOCATOR)

time.sleep(3)

action.click(left_button).pause(1).double_click(double_button).pause(1).context_click(right_button).perform()
time.sleep(3)
