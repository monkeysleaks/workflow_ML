import os
from supabase import create_client, Client
from supabase.client import ClientOptions
from icecream import ic
import json
import time

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(
    url, 
    key,
    options=ClientOptions(
        schema="official",
    )
)
def get_data(schema,tabla):
    response = (
        supabase.schema(schema).table(tabla)
        .select("*")
        .execute())
    return response.data

def insert_data(schema ,tabla, datos):
    response = (
    supabase.schema(schema).table(tabla)
    .insert(datos)
    .execute())
    ic(response)

def update_data(artista, code_voe, title):
    response = (
    supabase.table(f"{artista}_videos")
    .update({"code_voe": code_voe})
    .eq("title", title)
    .execute()
    )
    print(response.data)
    return response

def upsert_data(artista):
    response = (
    supabase.table(f"{artista}_videos")
    .upsert([{"id": 1, "nombre": "piano"}, {"id": 2, "nombre": "guitar"}])
    .execute())
    print(response.data)


def lista_carpeta():
    ruta = "E:/datos/"
    nombres = os.listdir(ruta)
    lista_nombres = []
    
    for nombre in nombres:

        if nombre != "Filemoon.csv":
            # Crear estructura de datos para cada elemento
            elemento = {"nombre": nombre}
            lista_nombres.append(elemento)
    
    return lista_nombres


def delete_data(tabla, fila, elemento):
    response = (
    supabase.table(tabla)
    .delete()
    .in_(fila, elemento)
    .execute())
    print(response)

def abrir_json(artista):
    path = f"C:/Users/diego/Desktop/Curso_Progamacion/backend_ML/backend/data/{artista}.json"
    informacion = []
    with open (path, "r") as file:
        datos = json.load(file)
        for dato in datos:
            info = {"title": f"{dato["title"]}","code_voe" : f"{dato["code_voe"]}", "code_filemoon": f"{dato["code_filemoon"]}", "length" : f"{dato["length"]}", "file_size": f"{dato["file size"]}", "img": f"{dato["img"]}", "portal": "false"}
            informacion.append(info)
    return informacion

#  ----------  main  ------------- 

with open("fallas.txt", "w" ) as file:
    file.write("error, artista, title \n")

try:
    token = os.environ.get('API_KEY_VOE')

    data_ar_official = get_data("official","artistas")

    
    for artista in data_ar_official:
        artista_name = artista["name"]
        artista_id = artista["artista_id"]
        print(f"artista_id: {artista_id}")
    
        data_ar_pruebas = get_data("pruebas", f"{artista_name}_videos")
        for dato in data_ar_pruebas:

            try:
                informacion = {"artista_id": artista_id, "title": dato["title"], "code_voe": dato["code_voe"],   "code_filemoon": dato["code_filemoon"], "length": dato["length"], "file_size": dato["file_size"], "img":    dato    ["img"], "portal": dato["portal"], "views": 0 }
                insert_data("official", "videos", informacion)
            except Exception as e:
                print(f"Error en {artista}, file: {dato['title']}")
                with open("fallas.txt", "a") as file:
                    file.write(f"{e}, {artista['name']}, {dato['title']} \n") 
            time.sleep(0.5)

                
except Exception as e:
    print(f"Error: {e}")





        
        


    


