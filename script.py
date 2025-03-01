import requests

URL = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    print(f"Título del post: {data['title']}")
else:
    print(f"Error en la consulta: {response.status_code}")
