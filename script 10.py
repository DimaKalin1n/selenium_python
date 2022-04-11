import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

def calc(x):
    return math.log(abs(12*math.sin(x)))


link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)



    price = WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"), '100'))

    button = browser.find_element(By.ID, 'book')
    button.click()

    input1 = browser.find_element(By.ID, 'input_value').text
    number = str(calc(int(input1)))

    input2 = browser.find_element(By.ID, 'answer')
    input2.send_keys(number)

    button2 = browser.find_element(By.ID, 'solve')
    button2.click()

finally:
    time.sleep(10)
    browser.quit()