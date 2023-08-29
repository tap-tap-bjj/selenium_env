from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(x)
    inp = browser.find_element(By.ID, 'answer')
    inp.send_keys(y)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    text_answer = browser.switch_to.alert.text.split(':')[-1]
    pyperclip.copy(text_answer)


except Exception as e:
    print(f'Ошибка {e}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
