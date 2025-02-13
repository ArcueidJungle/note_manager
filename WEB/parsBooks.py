import requests
from bs4 import BeautifulSoup

link = 'https://books.toscrape.com/'
response = requests.get(link)
soup = BeautifulSoup(response.text, 'lxml')
table = soup.find_all('h3', )

for t in table:
    print(t.find('a')['title'])
