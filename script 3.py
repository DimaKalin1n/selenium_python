from selenium import webdriver
from  selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/math.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    element_x = browser.find_element(By.ID,'input_value')
    x = element_x.text

    answer = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(answer)

    input2 = browser.find_element(By.CSS_SELECTOR,'[for="robotCheckbox"]')
    input2.click()

    input3 = browser.find_element(By.CSS_SELECTOR,'[for="robotsRule"]')
    input3.click()

    button = browser.find_element(By.TAG_NAME,'button')
    button.click()

finally:
    time.sleep(5)
    browser.quit()