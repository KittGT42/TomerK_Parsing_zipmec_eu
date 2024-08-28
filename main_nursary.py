import time

import requests
from bs4 import BeautifulSoup
from lxml import etree
import csv


def work_with_company_profile_name_company(soup_company_profile: BeautifulSoup):
    company_profile_name_company = soup_company_profile.find_all('ul', {'class': 'uk-list uk-list-line'})[0].find_all('li')[0]
    return company_profile_name_company.contents[1]


def work_with_company_profile_city(soup_company_profile: BeautifulSoup):
    company_profile_city = soup_company_profile.find_all('ul', {'class': 'uk-list uk-list-line'})[0].find_all('li')[2]
    return company_profile_city.contents[1]


def work_with_company_profile_country(soup_company_profile: BeautifulSoup):
    company_profile_country = soup_company_profile.find_all('ul', {'class': 'uk-list uk-list-line'})[0].find_all('li')[5]
    return company_profile_country.contents[2]


def work_with_company_profile_business(soup_company_profile: BeautifulSoup):
    result = []
    company_profile_business = soup_company_profile.find_all('ul', {'class': 'uk-list uk-list-line'})[2].find_all('li')
    for busines in company_profile_business:
        result.append(busines.contents[0])
    return result


# Открываем файл и читаем его содержимое
with open('cards_Nursery.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Парсим HTML с использованием lxml
parser = etree.HTMLParser()
tree = etree.fromstring(content, parser)

# Находим все элементы с атрибутом data-campo
elements = tree.xpath('//*[@data-campo]')

# Извлекаем значения атрибута data-campo
data_campo_values_nursery = [element.get('data-campo') for element in elements]

headers_csv = ['Company name', 'City', 'Country', 'Business', 'Fax', 'Telephone', 'Email', 'Web Site', 'WhatsApp',
               'Mobile', 'Linkedin']

with open('data_cards_Nursery.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers_csv)

counter_link = 0
for profile_link in data_campo_values_nursery:
    counter_link += 1
    full_link = "https://www.zipmec.eu" + profile_link
    response = requests.get(full_link)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        Company_name = work_with_company_profile_name_company(soup)
        City = work_with_company_profile_city(soup)
        Country = work_with_company_profile_country(soup)
        Business = work_with_company_profile_business(soup)
        Fax = '-'
        Telephone = '-'
        Email = '-'
        Web_Site = '-'
        WhatsApp = '-'
        Mobile = '-'
        Linkedin = '-'

        # Находим все элементы с атрибутом data-campo
        elements = soup.find_all(attrs={"data-campo": True})
        # name_spans = soup.find_all('span', {'class': 'uk-text-bold'})
        for elem in elements:
            if elem.previous.previous[:-2] == 'Fax':
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
            elif elem.previous.previous[:-2] == 'Mobile':
                if '+' in elem.get('data-campo'):
                    Mobile = elem.get('data-campo')
                else:
                    Mobile = '+' + elem.get('data-campo')
            elif elem.previous.previous[:-2] == 'Linkedin':
                Linkedin = elem.get('data-campo')

        # Извлекаем все значения атрибута data-campo
        data_campo_values_profile = [element['data-campo'] for element in elements]
        print(f'{counter_link}/{len(data_campo_values_nursery)}   DOWNLOAD SUCCESS')

        with open('data_cards_Nursery.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(
                [Company_name, City, Country, Business, Fax, Telephone, Email, Web_Site, WhatsApp, Mobile, Linkedin])
