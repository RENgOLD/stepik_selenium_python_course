# https://stepik.org/lesson/237240/step/5?unit=209628
# 1. открыть страницу
# 2. авторизоваться на странице со своим логином и паролем (см. предыдущий шаг)
# 3. ввести правильный ответ (поле перед вводом должно быть пустым)
# 4. нажать кнопку "Отправить"
# 5. дождаться фидбека о том, что ответ правильный
# 6. проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import math
import time
import json

links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]

@pytest.mark.parametrize('link',links)
def test_stepik_auth(browser, link, stepik_creds):
    browser.implicitly_wait(20)
    login, password = stepik_creds

    browser.get(link) #1
    button_login = browser.find_element(By.CSS_SELECTOR, 'a.navbar__auth_login')
    button_login.click()

    time.sleep(5)
    textbox_login = browser.find_element(By.CSS_SELECTOR, 'input[name="login"]')
    textbox_login.send_keys(login)

    textbox_password = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    textbox_password.send_keys(password)

    button_signin = browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn')
    button_signin.click() #2

    time.sleep(5)
    textbox_answer = browser.find_element(By.CSS_SELECTOR, 'textarea.textarea')
    if textbox_answer.get_attribute('disabled'):
        button_solve_again = browser.find_element(By.CSS_SELECTOR,'button.again-btn')
        button_solve_again.click()
        time.sleep(5)

    textbox_answer = browser.find_element(By.CSS_SELECTOR, 'textarea.textarea')
    answer = math.log(int(time.time()))
    textbox_answer.send_keys(answer) #3

    time.sleep(1)
    button_submit = browser.find_element(By.CSS_SELECTOR, 'button.submit-submission')
    button_submit.click() #4

    time.sleep(5)
    label_optional = browser.find_element(By.CSS_SELECTOR, 'p.smart-hints__hint') #5

    assert 'Correct!' in label_optional.text #6
