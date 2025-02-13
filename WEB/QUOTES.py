import requests
from bs4 import BeautifulSoup

link = 'https://quotes.toscrape.com/'
response = requests.get(link)
soup = BeautifulSoup(response.text, 'lxml')
table = soup.find_all('div', class_= 'quote')

for t in table[0:5]:
    text = t.find('span', class_ = 'text').text.strip()
    author = t.find('small', class_ = 'author').text.strip()
    print(f'{text} by {author}')