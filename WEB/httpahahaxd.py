import pprint

import requests

url = "https://api.github.com/users/ArcueidJungle"  # Правильный URL API
headers = {"User-Agent": "Mozilla/5.0"}  # Обязательный заголовок
response = requests.get(url, headers)
response_json = response.json()

pprint.pprint(response_json)

url_post = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "Hello HTTP!",
    "body": "Это тестовый POST-запрос",
    "userId": 1
}

response_post = requests.post(url_post, json = data)
print("\nPOST-запрос:")
print(f"Статус-код: {response_post.status_code}")  # Должно быть 201 (Created)
print(f"Ответ сервера: {response_post.json()}")

