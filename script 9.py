from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

def calc(x):
    return math.log(abs(12*math.sin(x)))

link = 'http://suninjuly.github.io/redirect_accept.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    number = browser.find_element(By.ID, 'input_value')
    number = str(calc(int(number.text)))

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(number)

    button2 = browser.find_element(By.TAG_NAME, 'button')
    button2.click()
finally:
    sleep(10)
    browser.quit()