# https://stepik.org/lesson/228249/step/6?unit=200781
# 1. Открыть страницу https://SunInJuly.github.io/execute_script.html.
# 2. Считать значение для переменной x.
# 3. Посчитать математическую функцию от x.
# 4. Проскроллить страницу вниз.
# 5. Ввести ответ в текстовое поле.
# 6. Выбрать checkbox "I'm the robot".
# 7. Переключить radiobutton "Robots rule!".
# 8. Нажать на кнопку "Submit".

from selenium import webdriver
from selenium.webdriver.common.bidi import browser
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/execute_script.html') #1

    valueX = browser.find_element(By.CSS_SELECTOR, 'label>span#input_value') #2
    textBox = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    answer = calc(int(valueX.text)) #3

    submitButton = browser.find_element(By.CSS_SELECTOR, 'button')
    textBox.send_keys(answer) #5

    browser.execute_script("return arguments[0].scrollIntoView(true);", submitButton) #4

    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox.click() #6

    radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radiobutton.click() #7

    submitButton.click() #8

finally:
    time.sleep(5)
    browser.quit()