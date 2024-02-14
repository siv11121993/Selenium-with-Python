import time
from selenium import webdriver

PROXY = "31.163.192.152	:4153"  # Указываем адрес прокси-сервера

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={PROXY}")  # Добавляем прокси через опции

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://free-proxy.cz/cs/ipinfo")  # Проверяем IP-адрес

time.sleep(10)