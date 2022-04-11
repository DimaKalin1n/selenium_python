from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = 'http://suninjuly.github.io/registration1.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR,'form>div.first_block>div.form-group.first_class>input')
    input1.send_keys('Ivan')

    # input2 = browser.find_element(By.CSS_SELECTOR, 'form>div.first_block>div.form-group.second_class>input')
    # input2.send_keys('Ivanov')

    input3 = browser.find_element(By.CSS_SELECTOR, 'form>div.first_block>div.form-group.third_class>input')
    input3.send_keys('DM')

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    welcome_text = welcome_text_elt.text


    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(5)
    browser.quit()