import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
API_URL = f"https://voe.sx/api/account/info?key={API_TOKEN}"

if not API_TOKEN:
    print("Error: No se encontró el token de API")
    exit(1)

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

response = requests.get(API_URL, headers=headers)

if response.status_code == 200:
    data = response.json()
    balance = data["result"]["balance"]
    print(f"Saldo actual: {balance}")
else:
    print(f"Error en la consulta: {response.status_code}")
