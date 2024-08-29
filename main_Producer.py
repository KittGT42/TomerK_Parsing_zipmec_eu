import time

import requests
from lxml import etree
from bs4 import BeautifulSoup
import csv


def work_with_company_profile_name_company(soup_company_profile: BeautifulSoup):
    company_profile_name_company = \
        soup_company_profile.find_all('ul', {'class': 'uk-list uk-list-line'})[0].find_all('li')[0]
    return company_profile_name_company.contents[1]


def work_with_company_profile_city(soup_company_profile: BeautifulSoup):
    company_profile_city = soup_company_profile.find_all('ul', {'class': 'uk-list uk-list-line'})[0].find_all('li')[2]
    return company_profile_city.contents[1]


def work_with_company_profile_country(soup_company_profile: BeautifulSoup):
    company_profile_country = soup_company_profile.find_all('ul', {'class': 'uk-list uk-list-line'})[0].find_all('li')[
        5]
    return company_profile_country.contents[2]


def work_with_company_profile_business(soup_company_profile: BeautifulSoup):
    result = []
    company_profile_business = soup_company_profile.find_all('div', {'class': 'uk-panel uk-panel-box edysmabox'})
    for busines in company_profile_business:
        if 'Business' in busines.text.strip():
            busines = busines.find_all('li')
            for business in busines:
                result.append(business.contents[0])
    return result


def work_with_company_profile_tags(soup_company_profile: BeautifulSoup):
    result = []
    company_profile_tags = soup_company_profile.find_all('div', {'class': 'uk-panel uk-panel-box edysmabox'})
    for company_profile_target in company_profile_tags:
        if 'Tags' in company_profile_target.text.strip():
            for tags in company_profile_target.find_all('a'):
                result.append(tags.text.strip())
    return result


def work_with_company_profile_products():
    # Создайте список для хранения данных
    products_data = []

    products_section = soup.find_all("div", class_="uk-panel uk-panel-box edysmabox")[3]
    if products_section:
        products_table = products_section.find("table")

        # Проверьте, что таблица найдена
        if products_table:
            # Извлеките заголовки таблицы (колонки)
            headers = [header.get_text(strip=True) for header in products_table.find_all("th")]

            # Извлеките все строки таблицы, кроме заголовков
            rows = products_table.find_all("tr")[1:]  # Пропускаем заголовок

            # Пройдитесь по каждой строке таблицы
            for row in rows:
                # Извлеките все ячейки в строке
                cells = row.find_all("td")
                product_name = cells[0].get_text(strip=True)
                product_info = {}

                # Пройдитесь по каждой ячейке после названия продукта
                for i in range(1, len(cells)):
                    # Определите, является ли значение "True" или "False"
                    product_info[headers[i]] = cells[i].find("span", class_="uk-icon-check-square-o") is not None

                # Создайте словарь, где ключ — это название продукта, а значение — его характеристики
                products_data.append({product_name: product_info})
    return products_data


result = 0
for i in range(142, 160):
    countri_id = i
    with open(f'countrys/country_{countri_id}.html', 'r', encoding='utf-8') as file:
        content = file.read()

    # Парсим HTML с использованием lxml
    parser = etree.HTMLParser()
    tree = etree.fromstring(content, parser)

    # Находим все элементы с атрибутом data-campo
    elements = tree.xpath('//*[@data-campo]')

    # Извлекаем значения атрибута data-campo
    if countri_id == 83:
        data_campo_values_producer = [element.get('data-campo') for element in elements][340:]
    else:
        data_campo_values_producer = [element.get('data-campo') for element in elements]

    counter_link = 0
    for profile_link in data_campo_values_producer:
        counter_link += 1
        full_link = "https://www.zipmec.eu" + profile_link
        print(f'Work with {full_link} ...')
        response = requests.get(full_link, timeout=10)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            Company_name = work_with_company_profile_name_company(soup)
            City = work_with_company_profile_city(soup)
            Country = work_with_company_profile_country(soup)
            Business = work_with_company_profile_business(soup)
            Tags = work_with_company_profile_tags(soup)
            Products = work_with_company_profile_products()
            Fax = '-'
            Telephone = '-'
            Email = '-'
            Web_Site = '-'
            WhatsApp = '-'
            Mobile = '-'
            Linkedin = '-'

            # Находим все элементы с атрибутом data-campo
            elements = soup.find_all(attrs={"data-campo": True})
            for elem in elements:
                if elem.previous.previous.startswith('Fax'):
                    if '+' in elem.get('data-campo'):
                        Fax = elem.get('data-campo')
                    else:
                        Fax = '+' + elem.get('data-campo')
                elif elem.previous.previous[:-2] == 'Telephone':
                    if '+' in elem.get('data-campo'):
                        Telephone = elem.get('data-campo')
                    else:
                        Telephone = '+' + elem.get('data-campo')
                elif elem.previous.previous[:-2] == 'Email':
                    Email = elem.get('data-campo')
                elif elem.previous.previous[:-2] == 'Web Site':
                    Web_Site = elem.get('data-campo')
                elif elem.previous.previous[:-2] == 'WhatsApp':
                    if '+' in elem.get('data-campo'):
                        WhatsApp = elem.get('data-campo')
                    else:
                        WhatsApp = '+' + elem.get('data-campo')
                elif elem.previous.previous.startswith('Mobile'):
                    if '+' in elem.get('data-campo'):
                        Mobile = elem.get('data-campo')
                    else:
                        Mobile = '+' + elem.get('data-campo')
                elif elem.previous.previous[:-2] == 'Linkedin':
                    Linkedin = elem.get('data-campo')

            # Извлекаем все значения атрибута data-campo
            data_campo_values_profile = [element['data-campo'] for element in elements]
            print(f'{counter_link}/{len(data_campo_values_producer)}  file #{countri_id} DOWNLOAD SUCCESS')

            with open('data_cards_Producer.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(
                    [Company_name, City, Country, Business, Products, Tags, Fax, Telephone, Email, Web_Site, WhatsApp, Mobile,
                     Linkedin])
