# https://stepik.org/lesson/228249/step/3?unit=200781
# 1. Открыть страницу https://suninjuly.github.io/selects1.html
# 2. Посчитать сумму заданных чисел
# 3. Выбрать в выпадающем списке значение равное расчитанной сумме
# 4. Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.common.bidi import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/selects1.html') #1

    num1 = browser.find_element(By.CSS_SELECTOR,'#num1')
    num2 = browser.find_element(By.CSS_SELECTOR,'#num2')

    answer = int(num1.text) + int(num2.text) #2

    dropdown = Select(browser.find_element(By.CSS_SELECTOR, 'select#dropdown'))
    dropdown.select_by_value(str(answer)) #3

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button')
    submit_button.click() #4

finally:
    time.sleep(5)
    browser.quit()