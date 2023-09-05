import pickle
from auth_file import login_ATI, password_ATI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from threading import Timer
import csv


def add_cookie_ati():
    try:
        cookies = pickle.load(open("cookies_ati.pkl", "rb"))
        url = "https://ati.su/"
        driver.get(url)
        # delete the current cookies
        driver.delete_all_cookies()
        # add cookies from pickled-txt or a txt file
        for cookie in cookies:
            driver.add_cookie(cookie)
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
    except Exception as e:
        print(f'Ошибка в куках {e}')
def ati_update_car():
    try:
        driver.get('https://trucks.ati.su/EditPages/OwnItems.aspx?EntityType=Truck&utm_source=header&utm_campaign=new_header&_gl=1*vuk7zt*_gcl_au*Mjg4MTQ4MTYuMTY4Nzk1OTEzOA..&_ga=2.56998954.1218699995.1693487573-1757310457.1684768002')
        driver.find_element(By.ID, 'item_cRate_0_Image14_0').click()
        time.sleep(5)
    except Exception as e:
        print(f'Ошибка обновления авто {e}')


def new_msk_kld_zad():
    try:
        global gruzi
        driver.get('https://loads.ati.su/#?filter=%7B%22from%22:%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0,%20%D0%A0%D0%A4%22,%22fromGeo%22:%222_3611%22,%22fromRadius%22:300,%22exactFromGeos%22:true,%22to%22:%22%D0%9A%D0%B0%D0%BB%D0%B8%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB.,%20%D0%A0%D0%A4%22,%22toGeo%22:%221_71%22,%22exactToGeos%22:true,%22firmListsExclusiveMode%22:false,%22loadingType%22:%224%22,%22withAuction%22:false%7D')
        gruzi = driver.find_elements(By.CSS_SELECTOR, 'div[data-app="pretty-load"]')
        with open('gruzi.csv', 'w', encoding='utf-8-sig', newline='') as file:
            for gruz in gruzi:
                print(''.join(gruz.text.split('\n')))
                print(gruz.text.split("\n"))
                writer = csv.writer(file, delimiter=';')
                writer.writerow(gruz.text.split("\n"))

    except Exception as e:
        print(f'Ошибка в грузах {e}')

def get_cook_ati(): # Функция для записи куков АТИ
    driver.find_element(By.CSS_SELECTOR, 'button.header-login').click()
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='Login popup']")))
    driver.find_element(By.ID, 'login').send_keys(login_ATI)
    driver.find_element(By.ID, 'password').send_keys(password_ATI)
    driver.find_element(By.ID, 'action-login').click()
    time.sleep(15)
    driver.switch_to.default_content()
    pickle.dump(driver.get_cookies(), open("cookies_ati.pkl", "wb"))

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    # Dobavlyaem cookie dlya authorization
    add_cookie_ati()

    # Global variable
    gruzi = []

    # Запуск периодической проверки
    job = Timer(3700, ati_update_car())
    #job1 = Timer(300, new_msk_kld_zad())
    job.start()
    #job1.start()
