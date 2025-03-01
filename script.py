import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env (solo en local)
load_dotenv()

# Obtener API_URL y API_TOKEN desde las variables de entorno
API_URL = os.getenv("API_URL")
API_TOKEN = os.getenv("API_TOKEN")

if not API_URL or not API_TOKEN:
    print("Error: Faltan variables de entorno")
    exit(1)

# Construir la URL con el token en la query
url = f"{API_URL}{API_TOKEN}"

# Realizar la petición GET
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    balance = data["result"]["balance"]
    print(f"Saldo actual: {balance}")
else:
    print(f"Error en la consulta: {response.status_code} - {response.text}")
