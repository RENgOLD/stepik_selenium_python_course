from selenium import webdriver
from pathlib import Path
import pytest
import json

@pytest.fixture
def stepik_creds():
    """Считывание данных для авторизации на stepik из отдельного файла."""
    path = Path('creds.json')
    creds = json.loads(path.read_text())
    return creds['login'], creds['password']

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nStart chrome browser for test...")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nStart firefox browser for test...")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nQuit browser...")
    browser.quit()


