from os import error
from sys import exception

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")
    button = browser.find_element(By.ID, "submit_button")
except:
    print(exception())