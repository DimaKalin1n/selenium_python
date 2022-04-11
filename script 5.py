import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def calc(x,y):
    return x+y

link = 'http://suninjuly.github.io/selects1.html?'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elem1 = browser.find_element(By.ID,'num1')
    x = int(elem1.text)

    elem2 = browser.find_element(By.ID, 'num2')
    y = int(elem2.text)

    answer = calc(x, y)
    print(answer)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(str(answer))

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()