from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(x))))


link = 'http://suninjuly.github.io/execute_script.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    argument_x = browser.find_element(By.ID, 'input_value')
    x = int(argument_x.text)
    print(x)
    answer = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(answer)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    chekbox = browser.find_element(By.ID, 'robotCheckbox')
    chekbox.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    button.click()

finally:
    time.sleep(10)
    browser.quit()