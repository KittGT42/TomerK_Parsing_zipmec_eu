import time

import requests
from bs4 import BeautifulSoup
from lxml import etree
import csv

# Открываем файл и читаем его содержимое
# with open('cards_Nursery.html', 'r', encoding='utf-8') as file:
#     content = file.read()
#
# # Парсим HTML с использованием lxml
# parser = etree.HTMLParser()
# tree = etree.fromstring(content, parser)
#
# # Находим все элементы с атрибутом data-campo
# elements = tree.xpath('//*[@data-campo]')
#
# # Извлекаем значения атрибута data-campo
# data_campo_values_nursery = [element.get('data-campo') for element in elements]

# Выводим полученные значения
# print(data_campo_values_nursery)
headers_csv = ['Fax', 'Telephone', 'Email', 'Web Site', 'WhatsApp', 'Mobile', 'Linkedin']

with open('data_cards_Producer.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers_csv)

for i in range(1, 150):
    countri_id = i
    with open(f'countrys/country_{countri_id}.html', 'r', encoding='utf-8') as file:
        content = file.read()

    # Парсим HTML с использованием lxml
    parser = etree.HTMLParser()
    tree = etree.fromstring(content, parser)

    # Находим все элементы с атрибутом data-campo
    elements = tree.xpath('//*[@data-campo]')

    # Извлекаем значения атрибута data-campo
    data_campo_values = [element.get('data-campo') for element in elements]

    # Выводим полученные значения
    print(f'From siti #{countri_id} data camps :{len(data_campo_values)}')

    counter_link = 0
    for profile_link in data_campo_values:
        counter_link += 1
        full_link = "https://www.zipmec.eu" + profile_link
        response = requests.get(full_link)

        if response.status_code == 200:
            all_cat_of_info = []
            Fax = '-'
            Telephone = '-'
            Email = '-'
            Web_Site = '-'
            WhatsApp = '-'
            Mobile = '-'
            Linkedin = '-'
            soup = BeautifulSoup(response.content, 'lxml')
            # all_block_with_info = (soup.find_all('div', {'class': 'uk-panel uk-panel-box edysmabox'})[1]
            #                        .find_all('span', {'class': 'uk-text-bold'}))
            # for block in all_block_with_info:
            #     all_cat_of_info.append(block.text[:-1])

            # Находим все элементы с атрибутом data-campo
            elements = soup.find_all(attrs={"data-campo": True})
            # name_spans = soup.find_all('span', {'class': 'uk-text-bold'})
            for elem in elements:
                if elem.previous.previous[:-2] == 'Fax':
                    Fax = elem.get('data-campo')
                elif elem.previous.previous[:-2] == 'Telephone':
                    Telephone = elem.get('data-campo')
                elif elem.previous.previous[:-2] == 'Email':
                    Email = elem.get('data-campo')
                elif elem.previous.previous[:-2] == 'Web Site':
                    Web_Site = elem.get('data-campo')
                elif elem.previous.previous[:-2] == 'WhatsApp':
                    WhatsApp = elem.get('data-campo')
                elif elem.previous.previous[:-2] == 'Mobile':
                    Mobile = elem.get('data-campo')
                elif elem.previous.previous[:-2] == 'Linkedin':
                    Linkedin = elem.get('data-campo')

            # Извлекаем все значения атрибута data-campo
            data_campo_values_profile = [element['data-campo'] for element in elements]
            print(f'{counter_link}/{len(data_campo_values)}   DOWNLOAD SUCCESS')

            with open('data_cards_Producer.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([Fax, Telephone, Email, Web_Site, WhatsApp, Mobile, Linkedin])
