import requests
import os

def buscar_personaje(nombre_parcial):
    url = "https://swapi.dev/api/people/"
    personajes = []

    while url:
        response = requests.get(url)
        data = response.json()
        for personaje in data['results']:
            if nombre_parcial.lower() in personaje['name'].lower():
                nombre_planeta = obtener_nombre_planeta(personaje['homeworld'])
                nombres_episodios = obtener_nombres_episodios(personaje['films'])
                especie = obtener_especie(personaje['species'])
                naves = obtener_nombres_naves(personaje['starships'])
                vehiculos = obtener_nombres_vehiculos(personaje['vehicles'])
                
                personaje_info = {
                    "nombre": personaje['name'],
                    "planeta_origen": nombre_planeta,
                    "episodios": nombres_episodios,
                    "genero": personaje['gender'],
                    "especie": especie,
                    "naves": naves,
                    "vehiculos": vehiculos
                }
                personajes.append(personaje_info)
        
        url = data['next']
    
    return personajes

def obtener_nombre_planeta(url):
    if url:
        response = requests.get(url)
        data = response.json()
        return data['name']
    return "Desconocido"

def obtener_nombres_episodios(urls):
    nombres = []
    for url in urls:
        response = requests.get(url)
        data = response.json()
        nombres.append(data['title'])
    return nombres

def obtener_especie(urls):
    if urls:
        response = requests.get(urls[0])
        data = response.json()
        return data['name']
    return "Desconocido"

def obtener_nombres_naves(urls):
    nombres = []
    for url in urls:
        response = requests.get(url)
        data = response.json()
        nombres.append(data['name'])
    return nombres

def obtener_nombres_vehiculos(urls):
    nombres = []
    for url in urls:
        response = requests.get(url)
        data = response.json()
        nombres.append(data['name'])
    return nombres

nombre_parcial = input("Introduce parte del nombre del personaje: ")
personajes = buscar_personaje(nombre_parcial)
for personaje in personajes:
    print(f"Nombre: {personaje['nombre']}")
    print(f"Planeta de Origen: {personaje['planeta_origen']}")
    print(f"Episodios: {', '.join(personaje['episodios'])}")
    print(f"Género: {personaje['genero']}")
    print(f"Especie: {personaje['especie']}")
    print(f"Naves: {', '.join(personaje['naves'])}")
    print(f"Vehículos: {', '.join(personaje['vehiculos'])}")
    print("\n")