import requests 
import os 

def initial_films():
    peliculas=requests.get("https://swapi.dev/api/films")
    return peliculas.json ()
     
las_peliculas=initial_films()

peliculas = []
for film in las_peliculas['results']:
    pelicula = {"titulo": film['title'], 
                "numero_de_episodio": film['episode_id'],
                "fecha_de_lanzamiento": film['release_date'],
                "opening_crawl": film['opening_crawl'],
                "director": film['director']}
    peliculas.append(pelicula)


print("-------------------------------------")
for pelicula in peliculas:
    print(f"Título: {pelicula['titulo']} \n")
    print(f"Número de Episodio: {pelicula['numero_de_episodio']} \n")
    print(f"Fecha de Lanzamiento: {pelicula['fecha_de_lanzamiento']} \n")
    print(f"Director: {pelicula['director']} \n")
    print(f"Opening Crawl: {pelicula['opening_crawl']} \n")
    print("-------------------------------------\n")
opcion = input("Presione una tecla para continuar")