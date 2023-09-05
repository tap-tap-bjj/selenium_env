from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h5#price'), '$100'))
    browser.find_element(By.CSS_SELECTOR, 'button#book').click()
    #browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(x)
    inp = browser.find_element(By.ID, 'answer')
    inp.send_keys(y)
    browser.find_element(By.CSS_SELECTOR, 'button#solve').click()

    text_answer = browser.switch_to.alert.text.split(':')[-1]
    pyperclip.copy(text_answer)


except Exception as e:
    print(f'Ошибка {e}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
