import json
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

url = 'https://parsinger.ru/html/index1_page_1.html'
shema = 'http://parsinger.ru/html/'

def get_soup(url):
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

def get_nav_page(url):
    soup = get_soup(url)
    nav_page = soup.find('div', class_='nav_menu').find_all('a')
    nav_page = [f"{shema}{l['href']}" for l in nav_page]
    return nav_page

def get_pagen(url):
    soup = get_soup(url)
    pagen = soup.find('div', class_='pagen').find_all('a')
    pagen = [f"{shema}{l['href']}" for l in pagen]
    return pagen

def get_item_page(url):
    soup = get_soup(url)
    item_page = []
    item_page.extend([f'{shema}{href}' for href in [x['href'] for x in soup.find('div', class_='item_card').find_all('a', class_='name_item')]])
    return item_page

result_json = []
count_cat = {}

for url_np in get_nav_page(url):
    for url_p in tqdm(get_pagen(url_np), desc=f'Zapolnyaem kartochki iz {url_np}'):
        for item_url in get_item_page(url_p):
            soup = get_soup(item_url)
            dict_description = {x['id']: x.text.split(':')[1] for x in soup.find('ul', id='description').find_all('li')}
            merged_dict = {
                'categories': item_url.split('/')[4],
                'name': soup.find('p', id='p_header').text,
                'article': soup.find('p', class_='article').text.split(':')[1],
                'description': dict_description,
                'count': soup.find('span', id='in_stock').text.split(':')[1],
                'price': soup.find('span', id='price').text,
                'old_price': soup.find('span', id='old_price').text,
                'link': item_url
            }
            result_json.append(merged_dict)
with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)
    print(f'Fail {file} gotov \n Kol-vo tovarov = {len(result_json)}')


# item_page = []
# item_page.extend([f'{shema}{href}' for href in [x['href'] for x in soup.find('div', class_='item_card').find_all('a', class_='name_item')]])

# with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(['Наименование', 'Артикул', 'Бренд', 'Модель', 'Наличие', 'Цена', 'Старая цена',  'Ссылка на карточку с товаром'])
#     index_labels = {1: "watch", 2: "mobile", 3: "mouse", 4: "hdd", 5: "headphones"}
#     for i in range(1, 6):
#         for j in tqdm(range(1,33), desc=f'Заполняю - {index_labels[i]}'):
#             url = f'https://parsinger.ru/html/{index_labels[i]}/{i}/{i}_{j}.html'
#             response = requests.get(url=url)
#             response.encoding = 'utf-8'
#             soup = BeautifulSoup(response.text, 'lxml')
#             des = soup.find('div', class_='description').text
#             des_lst = [x.strip() for x in des.split('\n') if x]
#             formatted_list = list(map(lambda x: x.split(': ')[1] if ': ' in x else x, des_lst))
#             formatted_list[-1] = url
#             formatted_list = formatted_list[:4] + formatted_list[-4:]
#             writer.writerow(formatted_list)
# print('Файл res.csv создан')





# data = pd.read_html('https://parsinger.ru/table/5/index.html')[0]
# print(data.iloc[[0],[0]])
# dic = {i: data[i].astype(float).sum().round(3) for i in data.columns}
# print(dic)

# #num = set()
# url = 'https://parsinger.ru/table/5/index.html'
# res = requests.get(url=url)
# res.encoding = 'utf-8'
# soup = BeautifulSoup(res.text, 'lxml')
# col_num = len(soup.find_all('th'))
# sum_td = len(soup.find_all('td'))
# num = [float(x.text) * float(y.text) for x, y in zip(soup.find_all('td', "orange"), [soup.find_all('td')[i] for i in range(14, sum_td, col_num)])]
# print(sum(num), col_num, sum_td, zip(soup.find_all('td', "orange"), [soup.find_all('td')[i] for i in range(14, sum_td, col_num)]))

# totle = 0
# index_labels = {1: "watch", 2: "mobile", 3: "mouse", 4: "hdd", 5: "headphones"}
# for i in range(1, 6):
#     for j in range(1,33):
#         url = f'https://parsinger.ru/html/{index_labels[i]}/{i}/{i}_{j}.html'
#         res = requests.get(url=url)
#         if 199<res.status_code<300:
#             res.encoding = 'utf-8'
#             soup = BeautifulSoup(res.text, 'lxml')
#             totle += (int(soup.find('span', id="in_stock").text.split()[2]) * int(soup.find('span', id="price").text.split()[0]))
#         else:
#             break
# print(totle)
