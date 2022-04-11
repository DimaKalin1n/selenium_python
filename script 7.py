from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('Ivan')

    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('Ivanov')

    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('123qwe')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file_path = os.path.join(current_dir, 'mem.txt')
    print(file_path)
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    sleep(10)
    browser.quit()