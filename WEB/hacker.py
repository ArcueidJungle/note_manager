import requests
from bs4 import BeautifulSoup

link = 'https://news.ycombinator.com/'
response = requests.get(link)
soup = BeautifulSoup(response.text, 'lxml')
table = soup.find_all('span', class_ = 'titleline')

for t in table:
    header = t.find('a').text
    linkr = t.find('a')['href']
    print(header + linkr)