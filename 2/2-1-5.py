# https://stepik.org/lesson/165493/step/5?unit=140087
# 1. Открыть страницу https://suninjuly.github.io/math.html.
# 2. Считать значение для переменной x.
# 3. Посчитать математическую функцию от x (код для этого приведён ниже).
# 4. Ввести ответ в текстовое поле.
# 5. Отметить checkbox "I'm the robot".
# 6. Выбрать radiobutton "Robots rule!".
# 7. Нажать на кнопку Submit.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    print(x)
    print(str(math.log(abs(12*math.sin(int(x))))))
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/math.html') #1

    labelx = browser.find_element(By.CSS_SELECTOR, 'label>span#input_value') #2
    inputForm = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    answer = calc(int(labelx.text)) #3
    inputForm.send_keys(answer) #4

    robotCheckbox = browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox')
    robotCheckbox.click() #5

    robotRadiobutton = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule')
    robotRadiobutton.click() #6

    submitButton = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submitButton.click() #7

finally:
    time.sleep(10)
    browser.quit()
