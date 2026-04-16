from selenium import webdriver
from selenium.webdriver.common.bidi import browser
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/math.html')

    peopleRuleRadiobutton = browser.find_element(By.CSS_SELECTOR, 'input#peopleRule')
    people_checked = peopleRuleRadiobutton.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

    submitButton = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    time.sleep(11)
    submitButton_disabled = submitButton.get_attribute("disabled")
    assert submitButton_disabled is not None

finally:
    time.sleep(10)
    browser.quit()