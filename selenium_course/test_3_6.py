import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import auth_file
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://stepik.org/learn"
text = ''


@pytest.fixture(scope="class")
def browser():
    global text
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    print(text)
    browser.quit()


class TestMainPage1():
    @pytest.mark.smoke
    def test_login(self, browser):
        browser.get(link)
        #browser.find_element(By.CSS_SELECTOR, "#ember33").click()
        browser.find_element(By.CSS_SELECTOR, "input[name='login']").send_keys(auth_file.login_Stepik)
        browser.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(auth_file.password_Stepik)
        browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn').click()
        print("\nlogin sucsess")


    @pytest.mark.parametrize('num', [str(x) for x in range(236895, 236906) if x not in range(236900, 236903)])
    def test_input_answer(self, browser, num):
        global text
        browser.get(f'https://stepik.org/lesson/{num}/step/1')
        inp_answer = browser.find_element(By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]')
        inp_answer.clear()
        inp_answer.send_keys(str(math.log(int(time.time()))))
        browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click()
        answer = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))).text
        try:
            assert answer == "Correct!", answer
        except AssertionError:
            text += answer

