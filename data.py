import requests
import json
from supabase import create_client, Client
from supabase.client import ClientOptions
import os
import time
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env (solo en local)
load_dotenv()

# Crear cliente
url: str = os.environ.get("DB_URL")
key: str = os.environ.get("DB_KEY")
supabase: Client = create_client(
    url, 
    key,
    options=ClientOptions(
        schema="pruebas",
    )
)

def get_data_ar(tabla_ar):
    response = (
        supabase.table(f"{tabla_ar}")
        .select("*")
        .execute())
    return response.data

def get_data_vid(tabla_vid):
    response = (
        supabase.table(f"{tabla_vid}_videos")
        .select("*")
        .execute())
    return response.data

if __name__ == "__main__":
    with open("resultado.txt", "w") as f:
        f.write("")
        print("Iniciando")

    artistas = get_data_ar("artistas")
    for artista in artistas:
        print("iniciando artistas")
        videos = get_data_vid(artista["nombre"])
        print(artista["nombre"])
        for video in videos:
            res = requests.get(f"https://voe.sx/{video['code_voe']}")
            if res.status_code == 200:
                print(f"Encontrado {video['code_voe']}")
            else:
                with open("resultado.txt", "a") as f:
                    f.write(f"artista: {artista['nombre']}, title: {video['title']}\n") 
                print(f"No encontrado {video['title']}")
