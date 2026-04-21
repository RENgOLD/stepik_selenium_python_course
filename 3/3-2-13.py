# https://stepik.org/lesson/36285/step/13?unit=162401
# 1. Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
# 2. Создайте новый файл
# 3. Создайте в нем класс с тестами, который должен наследоваться от unittest.
# TestCase по аналогии с предыдущим шагом
# 4. Перепишите в стиле unittest тест для страницы
# http://suninjuly.github.io/registration1.html
# 5. Перепишите в стиле unittest второй тест для страницы
# http://suninjuly.github.io/registration2.html
# 6. Оформите финальные проверки в тестах в стиле unittest, например, используя
# проверочный метод assertEqual
# 7. Запустите получившиеся тесты из файла
# 8. Просмотрите отчёт о запуске и найдите последнюю строчку
# 9. Отправьте эту строчку в качестве ответа на это задание
from operator import truediv

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR,
                                      'input[placeholder*="first name"]')
        input1.send_keys('firstName')

        input2 = browser.find_element(By.CSS_SELECTOR,
                                      'input[placeholder*="last name"]')
        input2.send_keys('lastName')

        input3 = browser.find_element(By.CSS_SELECTOR,
                                      'input[placeholder*="email"]')
        input3.send_keys('e@ma.il')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text,"Congratulations! You have successfully registered!")

    def test_registration2(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR,
                                      'input[placeholder*="first name"]')
        input1.send_keys('firstName')

        input2 = browser.find_element(By.CSS_SELECTOR,
                                      'input[placeholder*="last name"]')
        input2.send_keys('lastName')

        input3 = browser.find_element(By.CSS_SELECTOR,
                                      'input[placeholder*="email"]')
        input3.send_keys('e@ma.il')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        print(welcome_text)

        self.assertEqual(welcome_text,"Congratulations! You have successfully registered!",'Wrong message')

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")