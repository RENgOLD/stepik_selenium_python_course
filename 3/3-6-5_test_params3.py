from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import math
import time

@pytest.mark.parametrize('link',['https://stepik.org/lesson/236895/step/1'])
def test_stepik_auth(browser, link):
    browser.implicitly_wait(10)

    login = ''
    password = ''

    browser.get(link)
    button_login = browser.find_element(By.CSS_SELECTOR, 'a.navbar__auth_login')
    button_login.click()

    textbox_login = browser.find_element(By.CSS_SELECTOR, 'input[name="login"]')
    textbox_login.send_keys(login)

    textbox_password = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    textbox_password.send_keys(password)



    time.sleep(5)
    assert True