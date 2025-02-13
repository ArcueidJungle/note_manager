import requests
from bs4 import BeautifulSoup

link = 'https://cbr.ru/currency_base/daily/'
response = requests.get(link)
soup = BeautifulSoup(response.text, 'lxml')
soup.encode('utf-8')

table = soup.find('table', class_ = 'data')
rows = table.find_all('tr')[1:]

for row in rows:
    cols = row.find_all('td')
    if len(cols) >= 5:
        code = cols[1].text.strip()
        name = cols[3].text.strip()
        rare = cols[4].text.strip()
        if code in ['EUR', 'USD']:
            print(f'{code}, {name}, {rare} руб')
