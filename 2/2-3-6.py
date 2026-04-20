# https://stepik.org/lesson/184253/step/6?unit=158843
# 1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
# 2. Нажать на кнопку
# 3. Переключиться на новую вкладку
# 4. Пройти капчу для робота и получить число-ответ

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html') #1

    button = browser.find_element(By.CSS_SELECTOR, 'button')
    button.click() #2

    browser.switch_to.window(browser.window_handles[1]) #3

    label = browser.find_element(By.CSS_SELECTOR, 'label>span#input_value')
    textbox = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    answer = calc(int(label.text))
    textbox.send_keys(answer) #4

    button = browser.find_element(By.CSS_SELECTOR, 'button')
    button.click()

finally:
    time.sleep(5)
    browser.quit()