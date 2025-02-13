import requests
from bs4 import BeautifulSoup

link = 'https://webscraper.io/test-sites/e-commerce/allinone'
response = requests.get(link)
soup = BeautifulSoup(response.text, 'lxml')
table = soup.find_all('div', class_ = 'caption')

for t in table:
    title = t.find('a', class_ = 'title')['title']
    price = t.find('h4', class_ ='price float-end card-title pull-right').text
    print(title + ' ' + price)