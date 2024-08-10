import requests

def obtener_especies():
    url = "https://swapi.dev/api/species/"
    especies = []

    while url:
        response = requests.get(url)
        data = response.json()
        for especie in data['results']:
            nombre_planeta = obtener_nombre_planeta(especie['homeworld'])
            nombres_personajes = obtener_nombres_personajes(especie['people'])
            nombres_episodios = obtener_nombres_episodios(especie['films'])
            
            especie_info = {
                "nombre": especie['name'],
                "altura_promedio": especie['average_height'],
                "clasificacion": especie['classification'],
                "planeta_origen": nombre_planeta,
                "lengua_materna": especie['language'],
                "personajes": nombres_personajes,
                "episodios": nombres_episodios
            }
            especies.append(especie_info)
        
        url = data['next']
    
    return especies

def obtener_nombre_planeta(url):
    if url:
        response = requests.get(url)
        data = response.json()
        return data['name']
    return "Desconocido"

def obtener_nombres_personajes(urls):
    nombres = []
    for url in urls:
        response = requests.get(url)
        data = response.json()
        nombres.append(data['name'])
    return nombres

def obtener_nombres_episodios(urls):
    nombres = []
    for url in urls:
        response = requests.get(url)
        data = response.json()
        nombres.append(data['title'])
    return nombres


especies = obtener_especies()
print("-------------------------------------")
for especie in especies:
    print(f"Nombre: {especie['nombre']} \n")
    print(f"Altura Promedio: {especie['altura_promedio']} \n")
    print(f"Clasificación: {especie['clasificacion']} \n")
    print(f"Planeta de Origen: {especie['planeta_origen']} \n")
    print(f"Lengua Materna: {especie['lengua_materna']} \n")
    los_personajes = especie['personajes']
    print(f"Personajes:")
    for elementos in los_personajes:
        print(f"     -{elementos}")
    los_episodios = especie['episodios']
    print(" ")
    print(f"Episodios:")
    for elementos in los_episodios:
        print(f"     -{elementos}")
    print("-------------------------------------\n")
