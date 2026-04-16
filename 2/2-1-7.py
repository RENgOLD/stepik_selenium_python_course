# https://stepik.org/lesson/165493/step/7?unit=140087
# 1. Открыть страницу http://suninjuly.github.io/get_attribute.html.
# 2. Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# 3. Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# 4. Посчитать математическую функцию от x (сама функция остаётся неизменной).
# 5. Ввести ответ в текстовое поле.
# 6. Отметить checkbox "I'm the robot".
# 7. Выбрать radiobutton "Robots rule!".
# 8. Нажать на кнопку "Submit".

from selenium import webdriver
from selenium.webdriver.common.bidi import browser
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/get_attribute.html') #1

    treasure_img = browser.find_element(By.CSS_SELECTOR, 'img#treasure') #2
    valueX = treasure_img.get_attribute('valuex') #3

    answer = calc(int(valueX)) #4

    textBox = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    textBox.send_keys(answer) #5

    robotCheckbox = browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox')
    robotCheckbox.click() #6

    robotRadiobutton = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule')
    robotRadiobutton.click() #7

    submitButton = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submitButton.click() #8

finally:
    time.sleep(5)
    browser.quit()