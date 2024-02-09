import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.wikipedia.org/')

url = driver.current_url

print('URL страницы', url)

current_title = driver.title
print('Текущий заголовок', current_title)

assert url == 'https://www.wikipedia.org/', 'Ошибка в URL. Открыта неверная страница.'

assert current_title == 'Wikipedia', 'Некорректный заголовок страниц'
time.sleep(3)
