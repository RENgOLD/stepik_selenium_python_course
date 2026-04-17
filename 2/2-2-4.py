from selenium import webdriver
from selenium.webdriver.common.bidi import browser
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
script = "document.title='Script executing';alert('Robots at work');"
browser.execute_script(script)
time.sleep(5)