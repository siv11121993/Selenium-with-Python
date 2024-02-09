from selenium import webdriver
from webdriver_manager.safari import SafariDriverManager
from selenium.webdriver.safari.service import Service

service = Service(executable_path=SafariDriverManager().install())
driver = webdriver.Safari(service=service)

