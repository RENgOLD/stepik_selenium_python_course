# https://stepik.org/lesson/184253/step/4?unit=158843
# 1. Открыть страницу http://suninjuly.github.io/alert_accept.html
# 2. Нажать на кнопку
# 3. Принять confirm
# 4. На новой странице решить капчу для роботов, чтобы получить число с ответом

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html') #1

    button = browser.find_element(By.CSS_SELECTOR, 'button') #2
    button.click()

    modal_alert = browser.switch_to.alert
    modal_alert.accept() #3

    label = browser.find_element(By.CSS_SELECTOR, 'label>span#input_value')
    textbox = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    answer = calc(int(label.text))
    textbox.send_keys(answer) #4

    button = browser.find_element(By.CSS_SELECTOR, 'button') #2
    button.click()

finally:
    time.sleep(5)
    browser.quit()