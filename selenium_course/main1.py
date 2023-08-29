import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pyperclip

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.html')
    num = browser.find_element(By.ID, 'text_box').text
    res = eval(num)
    print(type(res))
    drop = browser.find_element(By.ID, 'selectId')
    drop.click()
    select = Select(drop)
    select.select_by_visible_text(str(res))
    time.sleep(5)
    # inp.send_keys(sum_num)
    browser.find_element(By.CLASS_NAME, 'btn').click()
    cod = browser.find_element(By.ID, 'result').text
    print(cod)
    pyperclip.copy(cod)
    time.sleep(5)