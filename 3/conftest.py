from selenium import webdriver
from pathlib import Path
import pytest
import json

@pytest.fixture
def stepik_creds():
    path = Path('creds.json')
    creds = json.loads(path.read_text())
    return creds['login'], creds['password']

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
