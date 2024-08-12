import requests
import pandas as pd
import csv
import os 
from swapi_client import SWAPIClient
from models.movie import Movie
from models.species import Species
from models.planet import Planet

#mostrar peliculas para el main
def listar_peliculas():
    movies_data = SWAPIClient.get_movies()
    movies = [Movie.from_dict(movie) for movie in movies_data]
    for movie in movies:
        print(f'\nTítulo: {movie.title}')
        print(f'Episodio: {movie.episode_id}')
        print(f'Fecha de lanzamiento: {movie.release_date}')
        print(f'Director: {movie.director}')
        print(f'Introducción: {movie.opening_crawl}')
        print('-'*70)

"""
selector de especies para el main
recorrer paginas de la api para ver todos las especies 
"""
def seleccionar_especie():
    current_page = 1
    species_data = []
    total_records = 0
    species_per_page = 10
    
    while True:
        if not species_data:
            response = requests.get(f"https://www.swapi.tech/api/species?page={current_page}&limit={species_per_page}")
            if response.status_code == 200:
                response_data = response.json()
                species_data = response_data['results']
                total_records = response_data['total_records']
                total_pages = response_data['total_pages']
            else:
                print('Error al obtener los datos de especies')
                break

        start_index = (current_page - 1) * species_per_page + 1

        print("\nEspecies disponibles:")
        for index, species in enumerate(species_data, start=start_index):
            print(f"{index}. {species['name']}")

                # Opciones de navegación
        options = "\nSelecciona una especie por número"
        if current_page > 1:
            options += " o escribe 'prev' para ver opciones anteriores"
        if current_page < total_pages:
            options += " o 'next' para ver más opciones"
        options += " (o 'q' para volver al menú principal): "

        choice = input(options)

        if choice.lower() == 'q':
            break
        elif choice.lower() == 'next' and current_page < total_pages:
            current_page += 1
            species_data = []
        elif choice.lower() == 'prev' and current_page > 1:
            current_page -= 1
            species_data = []
        else:
            try:
                choice = int(choice) - start_index
                if 0 <= choice < len(species_data):
                    species_url = species_data[choice]["url"]
                    response = requests.get(species_url)
                    if response.status_code == 200:
                        species_details = response.json()["result"]["properties"]

                        # Obtener el nombre del planeta natal
                        homeworld_url = species_details.get('homeworld')
                        if homeworld_url:
                            planet_response = requests.get(homeworld_url)
                            if planet_response.status_code == 200:
                                homeworld_name = planet_response.json()["result"]["properties"]["name"]
                            else:
                                homeworld_name = "Desconocido"
                        else:
                            homeworld_name = "N/A"

                        # Mostrar detalles de la especie
                        def traducir_valor(valor):
                            if valor == "unknown":
                                return "desconocido"
                            if valor == "N/A":
                                return "no aplica"
                            return valor
                        
                        print(f"\nDetalles para {species_details.get('name', 'N/A')}:")
                        print(f"Clasificación: {traducir_valor(species_details.get('classification', 'N/A'))}")
                        print(f"Designación: {traducir_valor(species_details.get('designation', 'N/A'))}")
                        print(f"Altura Promedio: {traducir_valor(species_details.get('average_height', 'N/A'))} cm")
                        print(f"Esperanza de Vida Promedio: {traducir_valor(species_details.get('average_lifespan', 'N/A'))} años")
                        print(f"Colores de Cabello: {traducir_valor(species_details.get('hair_colors', 'N/A'))}")
                        print(f"Colores de Piel: {traducir_valor(species_details.get('skin_colors', 'N/A'))}")
                        print(f"Colores de Ojos: {traducir_valor(species_details.get('eye_colors', 'N/A'))}")
                        print(f"Mundo Natal: {homeworld_name}")
                        print(f"Idioma: {traducir_valor(species_details.get('language', 'N/A'))}")

                        # Obtener y mostrar detalles de los personajes
                        characters = species_details.get('people', [])
                        if characters:
                            print("\nPersonajes:")
                            for character_url in characters:
                                character_response = requests.get(character_url)
                                if character_response.status_code == 200:
                                    character_details = character_response.json()["result"]["properties"]
                                    
                                    # Obtener el nombre del planeta de origen del personaje
                                    homeworld_url = character_details.get('homeworld')
                                    if homeworld_url:
                                        planet_response = requests.get(homeworld_url)
                                        if planet_response.status_code == 200:
                                            character_homeworld_name = planet_response.json()["result"]["properties"]["name"]
                                        else:
                                            character_homeworld_name = "Desconocido"
                                    else:
                                        character_homeworld_name = "N/A"
                                    
                                    # Mostrar detalles del personaje
                                    print(f" - Nombre: {traducir_valor(character_details.get('name', 'N/A'))}")
                                    print(f"   Altura: {traducir_valor(character_details.get('height', 'N/A'))} cm")
                                    print(f"   Mundo Natal: {character_homeworld_name}")
                                    print(f"   Idioma: {traducir_valor(species_details.get('language', 'N/A'))}\n")
                                else:
                                    print(" - Error al obtener detalles del personaje.")
                            print()  # Agregar una línea en blanco después de los personajes
                        else:
                            print("Personajes: N/A")
                    else:
                        print(f"Error al obtener detalles para {species_data[choice]['name']}")
                else:
                    print("Selección inválida. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número o 'q' para salir.")

"""
Selector de planetas para el main
recorrer paginas de la api para ver todos los planetas
"""

def listar_planetas():
    current_page = 1
    planets_data = []
    total_records = 0
    planets_per_page = 10

    while True:
        if not planets_data:
            response = requests.get(f'https://swapi.py4e.com/api/planets/?page={current_page}&limit={planets_per_page}')
            if response.status_code == 200:
                response_data = response.json()
                planets_data = response_data['results']
                total_records = response_data['count']
                total_page = (total_records + planets_per_page - 1) // planets_per_page #Redonde hacia arriba
            else:
                print("Error al obtener los datos de planetas")
                break
        
        start_index = (current_page - 1) * planets_per_page + 1

        print('\n Planetas disponibles')

        for index, planet in enumerate(planets_data, start = start_index):
            print(f'{index}. {planet['name']}')

        #Opciones de navegacion
        options = "\n Selecciona un planeta por número"
        if current_page > 1:
            options += " o 'next' para ver mas opciones"
        options += " (o 'q' Para volver al menú principal): "
        choice = input(options)
        if choice.lower() == 'q':
            break
        elif choice.lower() == 'next' and current_page < total_page:
            current_page += 1 
            planets_data = []
        elif choice.lower() == 'prev' and current_page > 1: 
            current_page += 1
            planets_data = []
        else:
            try:
                choice = int(choice) - start_index
                if 0 <= choice < len(planets_data):
                    planet = planets_data[choice]
                    planet_name = planet['name']
                    
                    #Obtener los episodos en los que aparece el planeta
                    films = planet.get('films', [])
                    film_titles = []

                    for film_url in films:
                        film_response = requests.get(film_url)
                        if film_response.status_code == 200:
                            film_title = film_response.json()['title']
                            film_titles.append(film_title)
                        else:
                            film_titles.append("Error al obtener el titulo del episodio")

                    #Mostrar los detalles del planeta y los episodios en los que aparece
                    print(f"\n Detalles para{planet_name}: ")
                    print(f"Periodo de orbita: {planet.get('orbital_period', 'N/A')} Dias")
                    print(f"Periodo de rotacion: {planet.get('rotation_period', 'N/A')} Horas")
                    print(f"Cantidad de habitantes: {planet.get('population'), ' N/A'}")
                    print(f"Tipo declima: {planet.get('climate', 'N/A')}")

                    print("\n Episodios en los que aparece:")
                    if film_titles:
                        for title in film_titles:
                            print(f" - {title}")
                    else:
                        print("No ha aparecido en ningun episodio")
                    print() #Espacio

                else:
                    print("Seleccion invalida. Intentelo de nuevo")
            except ValueError:
                print("Entrada no valida. Por favor, introduzca un numero o 'q' para salir") 


"""
Estadisticas sobre naves, promedios y moda
"""
def Estadisticas_sobre_Naves():
    import pandas as pd
    import csv
    import os 

    #Leer archivo CSV
    ruta_archivo = os.path.dirname(os.path.abspath(__file__))+"/csv/starships.csv"
    df = pd.read_csv(ruta_archivo)

    #Capturar estadisticas
    Hiperimpulsor_promedio = df["hyperdrive_rating"].mean()
    mglt_promedio = df["MGLT"].max()
    velocidad_maxima_atmosfera_promedio = df["max_atmosphering_speed"].max()
    costo_minimo_promedio = df["cost_in_credits"].min()
    moda_hyperdrive = df["hyperdrive_rating"].mode().iloc[0]
    moda_mglt = df["MGLT"].mode().iloc[0]
    moda_velocidadmax = df["max_atmosphering_speed"].mode().iloc[0]
    moda_costo = df["cost_in_credits"].mode().iloc[0]

    with open(ruta_archivo, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReade(file)
        
        #Limpiar pantalla e imprimir los encabezados
        os.system('cls')
        print(f'{'Clase de Nave':<30} {'Hiperimpulsor':<15} {'MGLT':<10} {'Velocidad maxima':<20} {'Costo en Creditos':<15}')
        print('-' * 95)

        #Leer cada fila del archivo CSV
        for row in csv_reader:
            clase_nave = row['name']
            hiperimpulsor = ['hyperdrive_rating']
            mglt = row['MGLT']
            velocidad_maxima = row['max_atmosphering_speed']
            costo = row['costo_in_credits']

            #Imprimir los datos por clase de nave
            print(f'{clase_nave:<30} {hiperimpulsor:<15} {mglt:<10} {velocidad_maxima:<20} {costo:<15}')

    #Imprimir el promedio y la moda de los datos
    print(' ')
    print(f'Promedio de Clasiicacion del Hierimpulsor: {Hiperimpulsor_promedio:.2f}')
    print(f'La Moda del Hiperimpulsor                 : {moda_hyperdrive}')
    print(' ')
    print(f'Maximo MGLT                              : {mglt_promedio}')
    print(f'La Moda de MGLT                          : {moda_mglt}')
    print(' ')
    print(f'Costo Minimo en Creditos                 : {costo_minimo_promedio}')
    print(f'La Moda del Costo Minimo en Creditos     : {moda_costo}')
    print(' ')



                
                    




