from selenium import webdriver
from selenium.webdriver.common.by import By
from sys import exception
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/find_xpath_form')
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[name="first_name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, 'input[name="last_name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, 'input.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.CSS_SELECTOR, 'input[id="country"]')
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click() 

except:
    print(str(exception()).split('\n')[0])
finally:
    time.sleep(10)
    browser.quit()