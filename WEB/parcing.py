import requests
from bs4 import BeautifulSoup

link = 'https://habr.com/ru/articles/'
response = requests.get(link).text
response.encode('utf-8')
soup = BeautifulSoup(response, 'lxml')
headers = soup.find_all('h2')

n = 0
for h in headers:
    n += 1
    print(f'{n}. [{h.text.strip()}]')