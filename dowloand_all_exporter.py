import requests

cookies = {
    'cc_cookie': '{"categories":["necessary"],"revision":0,"data":null,"rfc_cookie":false,"consent_date":"2024-08-27T08:45:11.101Z","consent_uuid":"5b5c6534-444e-4b7f-af4a-22910eb29e48","last_consent_update":"2024-08-27T08:45:11.101Z"}',
    'joomla_user_state': 'logged_in',
    '__gads': 'ID=d3a1400aca238d3b:T=1724748308:RT=1724781278:S=ALNI_MaXefj_-xkEjDiAfJNJ85zeEU9fuQ',
    '__gpi': 'UID=00000ea8ded5d757:T=1724748308:RT=1724781278:S=ALNI_MZ_3hc-cdJcGeZXcxXVFKmoz7_Zwg',
    '__eoi': 'ID=9884c315bc6b2a49:T=1724748308:RT=1724781278:S=AA-AfjZdbwtrCLWvqd-RtcSDPLZ9',
    '895bc47f19a19e246b54daafcf951e1a': 'vehvjcruuojea2kk02u4asfs3n',
    'joomla_remember_me_d7f12ac5c8ac53df36f3e40e8e7fcb86': 'WDAkLE0GR18MDeRV.QhmK5XFb4Rp2yEMZHMkt',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8,uk-UA;q=0.7,uk;q=0.6',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'cc_cookie={"categories":["necessary"],"revision":0,"data":null,"rfc_cookie":false,"consent_date":"2024-08-27T08:45:11.101Z","consent_uuid":"5b5c6534-444e-4b7f-af4a-22910eb29e48","last_consent_update":"2024-08-27T08:45:11.101Z"}; joomla_user_state=logged_in; __gads=ID=d3a1400aca238d3b:T=1724748308:RT=1724781278:S=ALNI_MaXefj_-xkEjDiAfJNJ85zeEU9fuQ; __gpi=UID=00000ea8ded5d757:T=1724748308:RT=1724781278:S=ALNI_MZ_3hc-cdJcGeZXcxXVFKmoz7_Zwg; __eoi=ID=9884c315bc6b2a49:T=1724748308:RT=1724781278:S=AA-AfjZdbwtrCLWvqd-RtcSDPLZ9; 895bc47f19a19e246b54daafcf951e1a=vehvjcruuojea2kk02u4asfs3n; joomla_remember_me_d7f12ac5c8ac53df36f3e40e8e7fcb86=WDAkLE0GR18MDeRV.QhmK5XFb4Rp2yEMZHMkt',
    'origin': 'https://www.zipmec.eu',
    'priority': 'u=0, i',
    'referer': 'https://www.zipmec.eu/en/cards.html',
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

for i in range(1, 150):
    print(f'Processing page {i}')

    data = {
        'searchType': 'guidata',
        'searchText': '',
        'product_id': '-1',
        'farming_id': '-1',
        'macro_activity_id': '4',
        'activity_id': '1',
        'country_id': i,
        'quantity': '6353',
        'ip': '91.203.63.72',
        'user_id': '37260',
    }

    response = requests.post(
        'https://www.zipmec.eu/en/cards.html?_gl=1*dxm58d*_up*MQ..*_ga*MTU2MzMzNTkzNC4xNzI1MDkzNjEx*_ga_J2JX61HXMW*MTcyNTA5MzYxMS4xLjAuMTcyNTA5MzYxMS4wLjAuMA..',
        cookies=cookies,
        headers=headers,
        data=data,
    )

    with open(f'exporter_countrys/cards_Exporter{i}.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
