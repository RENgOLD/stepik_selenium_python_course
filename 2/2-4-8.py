# https://stepik.org/lesson/181384/step/8?unit=156009
# 1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# 2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не
# меньше 12 секунд)
# 3. Нажать на кнопку "Book"
# 4. Решить уже известную нам математическую задачу (используйте ранее написанный
# код) и отправить решение

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html') #1

    label_price = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'),'$100')
    ) #2

    button_book = browser.find_element(By.CSS_SELECTOR, 'button#book')
    button_book.click() #3

    label = browser.find_element(By.CSS_SELECTOR, 'label>span#input_value')
    textbox = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    answer = calc(int(label.text))
    textbox.send_keys(answer) #4

    button_submit = browser.find_element(By.CSS_SELECTOR, 'button#solve')
    button_submit.click()


finally:
    time.sleep(5)
    browser.quit()
