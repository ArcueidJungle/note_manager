import requests
from bs4 import BeautifulSoup

link = 'https://ru.wikipedia.org/wiki/Python'
response = requests.get(link)
soup = BeautifulSoup(response.text, 'lxml')
soup.encode('utf-8')

headers = soup.find_all('h2')

for h in headers:
    print(h.text.strip())