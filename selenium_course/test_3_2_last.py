from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

def registration(url):
    with webdriver.Chrome() as browser:
        browser.get(url)

        input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
        input3.send_keys("ivan@petrov.com")
        time.sleep(5)

        btn = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
        btn.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    return welcome_text
class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(registration(link1), "Congratulations! You have successfully registered!", 'Failed registration')

    def test_reg2(self):
        self.assertEqual(registration(link2), "Congratulations! You have successfully registered!", 'Failed registration')


if __name__ == '__main__':
    unittest.main()