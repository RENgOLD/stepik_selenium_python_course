from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

link = 'http://selenium1py.pythonanywhere.com/'

@pytest.fixture
def browser():
    print('\nStart browser for test...')
    browser = webdriver.Chrome()
    yield browser
    print('\nQuit browser...')
    browser.quit()

class TestMainPage():
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.basket-mini .btn-group > a')