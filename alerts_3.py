import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создание экземпляра веб-драйвера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

# Переход на веб-страницу
driver.get("https://demoqa.com/alerts")

BUTTON_0 = ("xpath", "//button[@class='fc-button fc-cta-consent fc-primary-button']")
wait.until(EC.element_to_be_clickable(BUTTON_0)).click()

# time.sleep(10)

# Клик на кнопку, которая вызывает alert
BUTTON_4 = ("xpath", "//button[@id='promtButton']")
wait.until(EC.element_to_be_clickable(BUTTON_4)).click()

alert = wait.until(EC.alert_is_present())

driver.switch_to.alert

print(alert.text) # Вывод текста из алерта