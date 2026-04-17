# https://stepik.org/lesson/228249/step/8?unit=200781
# 1. Открыть страницу http://suninjuly.github.io/file_input.html
# 2. Заполнить текстовые поля: имя, фамилия, email
# 3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# 4. Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html') #1

    textBox_firstname = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    textBox_firstname.send_keys('firstname') #2

    textBox_lastname = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    textBox_lastname.send_keys('lastname') #2

    textBox_email = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    textBox_email.send_keys('e@ma.il') #2

    file = Path('test.txt')
    print(file.absolute().as_posix())
    button_uploadFile = browser.find_element(By.CSS_SELECTOR, '#file')
    button_uploadFile.send_keys(file.absolute().as_posix()) #3

    button_submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button_submit.click() #4

finally:
    time.sleep(5)
    browser.quit()