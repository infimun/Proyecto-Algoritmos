import requests
import limpiarp

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

limpiarp.limpiar_pantalla()
nombre_parcial = input("Introduce parte del nombre del personaje: ")
print(" ")
print(f"Por favor esperar, buscando todos los Nombres con: {nombre_parcial}")
personajes = buscar_personaje(nombre_parcial)
limpiarp.limpiar_pantalla()
print("-"*40)
for personaje in personajes:
    print(f"Nombre            : {personaje['nombre']} \n")
    print(f"Planeta de Origen : {personaje['planeta_origen']} \n")
    print(f"Género            : {personaje['genero']} \n")
    print(f"Especie           : {personaje['especie']} \n")
    los_episodios=personaje['episodios']
    print(f"Episodios         :")
    if len(los_episodios) == 0:
        print("   -¡¡¡ NO TIENE EPISODIOSS !!!")
    else:
        for elementos in los_episodios:
            print(f"  -{elementos}")
    print(" ")
    las_naves=personaje['naves']
    print(f"Naves             :")
    if len(las_naves) == 0:
        print("   -¡¡¡ NO TIENE NAVES !!!")
    else:
        for elementos in las_naves:
           print(f"  -{elementos}")
    print(" ")
    los_vehiculos=personaje['vehiculos']
    print(f"Vehículos         :")
    if len(los_vehiculos) == 0:
        print("   -¡¡¡ NO TIENE VEHICULOS !!!")
    else:
       for elementos in los_vehiculos:
           print(f"  -{elementos}")
    print("-"*40)
    print(" ")