from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

link = 'http://suninjuly.github.io/get_attribute.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    elem_x = browser.find_element(By.ID, 'treasure')
    x = int(elem_x.get_attribute('valuex'))


    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(calc(x))

    chekbox = browser.find_element(By.ID, 'robotCheckbox')
    chekbox.click()

    radiobox1 = browser.find_element(By.ID,'robotsRule')
    radiobox1.click()

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
finally:
    sleep(10)
    browser.quit()