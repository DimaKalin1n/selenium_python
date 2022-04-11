import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return math.log(abs(12*math.sin(x)))
link = 'http://suninjuly.github.io/alert_accept.html'
link2 = 'http://suninjuly.github.io/alert_redirect.html?'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.TAG_NAME, 'button')
    button1.click()

    alert = browser.switch_to.alert
    alert.accept()

    browser.get(link2)

    number = browser.find_element(By.ID, 'input_value')
    number = str(calc(int(number.text)))

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(number)

    button2 = browser.find_element(By.TAG_NAME, 'button')
    button2.click()
finally:
    time.sleep(10)
    browser.quit()