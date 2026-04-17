from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/selects1.html')

    dropdown = browser.find_element(By.CSS_SELECTOR, 'select')
    select = Select(dropdown)
    select.select_by_value('1')


finally:
    time.sleep(5)
    browser.quit()