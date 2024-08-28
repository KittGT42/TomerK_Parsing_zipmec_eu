import requests
from lxml import etree

cookies = {
    'cc_cookie': '{"categories":["necessary"],"revision":0,"data":null,"rfc_cookie":false,"consent_date":"2024-08-27T08:45:11.101Z","consent_uuid":"5b5c6534-444e-4b7f-af4a-22910eb29e48","last_consent_update":"2024-08-27T08:45:11.101Z"}',
    'joomla_user_state': 'logged_in',
    '__gads': 'ID=d3a1400aca238d3b:T=1724748308:RT=1724781278:S=ALNI_MaXefj_-xkEjDiAfJNJ85zeEU9fuQ',
    '__gpi': 'UID=00000ea8ded5d757:T=1724748308:RT=1724781278:S=ALNI_MZ_3hc-cdJcGeZXcxXVFKmoz7_Zwg',
    '__eoi': 'ID=9884c315bc6b2a49:T=1724748308:RT=1724781278:S=AA-AfjZdbwtrCLWvqd-RtcSDPLZ9',
    '895bc47f19a19e246b54daafcf951e1a': 'tfl3274pkkaso5u62e4l3dvlsn',
    'joomla_remember_me_d7f12ac5c8ac53df36f3e40e8e7fcb86': 'spSR4ejy1VEjGBUy.QhmK5XFb4Rp2yEMZHMkt',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8,uk-UA;q=0.7,uk;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'cc_cookie={"categories":["necessary"],"revision":0,"data":null,"rfc_cookie":false,"consent_date":"2024-08-27T08:45:11.101Z","consent_uuid":"5b5c6534-444e-4b7f-af4a-22910eb29e48","last_consent_update":"2024-08-27T08:45:11.101Z"}; joomla_user_state=logged_in; __gads=ID=d3a1400aca238d3b:T=1724748308:RT=1724781278:S=ALNI_MaXefj_-xkEjDiAfJNJ85zeEU9fuQ; __gpi=UID=00000ea8ded5d757:T=1724748308:RT=1724781278:S=ALNI_MZ_3hc-cdJcGeZXcxXVFKmoz7_Zwg; __eoi=ID=9884c315bc6b2a49:T=1724748308:RT=1724781278:S=AA-AfjZdbwtrCLWvqd-RtcSDPLZ9; 895bc47f19a19e246b54daafcf951e1a=tfl3274pkkaso5u62e4l3dvlsn; joomla_remember_me_d7f12ac5c8ac53df36f3e40e8e7fcb86=spSR4ejy1VEjGBUy.QhmK5XFb4Rp2yEMZHMkt',
    'origin': 'https://www.zipmec.eu',
    'priority': 'u=0, i',
    'referer': 'https://www.zipmec.eu/en/loai-jriesat-farm-co_96939.html',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}
result = 0
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
    result += len(data_campo_values)
print(result)