import requests
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


"""selector de personajes para el main 
busque coincidencias con escrito
"""

def buscar_personaje():
    all_characters = []
    page = 1

    # Obtener todos los personajes a través de las páginas
    while True:
        characters_response = requests.get(f"https://www.swapi.tech/api/people?page={page}&limit=10")
        if characters_response.status_code == 200:
            response_data = characters_response.json()
            characters_data = response_data["results"]
            all_characters.extend(characters_data)
            
            # Verificar si hay más páginas
            if response_data["next"] is None:
                break
            page += 1
        else:
            print("Error al obtener personajes.")
            return

    while True:
        search_term = input("\nIntroduce el nombre del personaje (o parte del nombre) a buscar (o 'q' para volver al menú principal): ").strip()
        if search_term.lower() == 'q':
            break

        matching_characters = []

        # Buscar personajes que coincidan con el término de búsqueda
        for character in all_characters:
            if search_term.lower() in character["name"].lower():
                matching_characters.append(character)

        if matching_characters:
            if len(matching_characters) == 1:
                # Si solo hay una coincidencia, mostrar la información directamente
                character_url = matching_characters[0]["url"]
                response = requests.get(character_url)
                if response.status_code == 200:
                    character_details = response.json()["result"]["properties"]

                    # Obtener el nombre del planeta natal
                    homeworld_url = character_details.get('homeworld')
                    if homeworld_url:
                        planet_response = requests.get(homeworld_url)
                        if planet_response.status_code == 200:
                            homeworld_name = planet_response.json()["result"]["properties"]["name"]
                        else:
                            homeworld_name = "Desconocido"
                    else:
                        homeworld_name = "N/A"

                    # Mostrar detalles del personaje
                    print(f"\nDetalles para {character_details.get('name', 'N/A')}:")
                    print(f"Altura: {character_details.get('height', 'N/A')} cm")
                    print(f"Peso: {character_details.get('mass', 'N/A')} kg")
                    print(f"Color de cabello: {character_details.get('hair_color', 'N/A')}")
                    print(f"Color de piel: {character_details.get('skin_color', 'N/A')}")
                    print(f"Color de ojos: {character_details.get('eye_color', 'N/A')}")
                    print(f"Año de nacimiento: {character_details.get('birth_year', 'N/A')}")
                    print(f"Género: {character_details.get('gender', 'N/A')}")
                    print(f"Mundo natal: {homeworld_name}")

                    # Obtener y mostrar detalles de las naves, vehículos y episodios desde la API secundaria
                    secondary_api_response = requests.get("https://swapi.py4e.com/api/people/")
                    if secondary_api_response.status_code == 200:
                        secondary_characters_data = secondary_api_response.json()["results"]
                        for sec_character in secondary_characters_data:
                            if sec_character["name"].lower() == character_details["name"].lower():
                                starships = sec_character.get('starships', [])
                                vehicles = sec_character.get('vehicles', [])
                                films = sec_character.get('films', [])
                                
                                if starships or vehicles or films:
                                    if starships:
                                        print("\nNaves:")
                                        for starship_url in starships:
                                            starship_response = requests.get(starship_url)
                                            if starship_response.status_code == 200:
                                                starship_name = starship_response.json()["name"]
                                                print(f" - {starship_name}")
                                            else:
                                                print(" - Error al obtener detalles de la nave.")
                                    if vehicles:
                                        print("\nVehículos:")
                                        for vehicle_url in vehicles:
                                            vehicle_response = requests.get(vehicle_url)
                                            if vehicle_response.status_code == 200:
                                                vehicle_name = vehicle_response.json()["name"]
                                                print(f" - {vehicle_name}")
                                            else:
                                                print(" - Error al obtener detalles del vehículo.")

                                    if films:
                                        print("\nEpisodios:")
                                        for film_url in films:
                                            film_response = requests.get(film_url)
                                            if film_response.status_code == 200:
                                                film_title = film_response.json()["title"]
                                                print(f" - {film_title}")
                                            else:
                                                print(" - Error al obtener detalles del episodio.")
                                    print()  # Agregar una línea en blanco después de las naves, vehículos y episodios
                                else:
                                    print("No se encontraron naves, vehículos o episodios asociados con este personaje.")
                                break
                    else:
                        print("Error al obtener información adicional desde la API secundaria.")

                else:
                    print(f"Error al obtener detalles para {matching_characters[0]['name']}")
            else:
                print("\nPersonajes encontrados:")
                for index, character in enumerate(matching_characters, start=1):
                    print(f"{index}. {character['name']}")

                choice = input("\nSelecciona un personaje por número para ver detalles (o 'q' para volver al menú principal): ")

                if choice.lower() == 'q':
                    break

                try:
                    choice = int(choice) - 1
                    if 0 <= choice < len(matching_characters):
                        character_url = matching_characters[choice]["url"]
                        response = requests.get(character_url)
                        if response.status_code == 200:
                            character_details = response.json()["result"]["properties"]

                            # Obtener el nombre del planeta natal
                            homeworld_url = character_details.get('homeworld')
                            if homeworld_url:
                                planet_response = requests.get(homeworld_url)
                                if planet_response.status_code == 200:
                                    homeworld_name = planet_response.json()["result"]["properties"]["name"]
                                else:
                                    homeworld_name = "Desconocido"
                            else:
                                homeworld_name = "N/A"

                            # Mostrar detalles del personaje
                            print(f"\nDetalles para {character_details.get('name', 'N/A')}:")
                            print(f"Altura: {character_details.get('height', 'N/A')} cm")
                            print(f"Peso: {character_details.get('mass', 'N/A')} kg")
                            print(f"Color de cabello: {character_details.get('hair_color', 'N/A')}")
                            print(f"Color de piel: {character_details.get('skin_color', 'N/A')}")
                            print(f"Color de ojos: {character_details.get('eye_color', 'N/A')}")
                            print(f"Año de nacimiento: {character_details.get('birth_year', 'N/A')}")
                            print(f"Género: {character_details.get('gender', 'N/A')}")
                            print(f"Mundo natal: {homeworld_name}")

                            # Obtener y mostrar detalles de las naves, vehículos y episodios desde la API secundaria
                            secondary_api_response = requests.get("https://swapi.py4e.com/api/people/")
                            if secondary_api_response.status_code == 200:
                                secondary_characters_data = secondary_api_response.json()["results"]
                                for sec_character in secondary_characters_data:
                                    if sec_character["name"].lower() == character_details["name"].lower():
                                        starships = sec_character.get('starships', [])
                                        vehicles = sec_character.get('vehicles', [])
                                        films = sec_character.get('films', [])
                                        
                                        if starships or vehicles or films:
                                            if starships:
                                                print("\nNaves:")
                                                for starship_url in starships:
                                                    starship_response = requests.get(starship_url)
                                                    if starship_response.status_code == 200:
                                                        starship_name = starship_response.json()["name"]
                                                        print(f" - {starship_name}")
                                                    else:
                                                        print(" - Error al obtener detalles de la nave.")
                                            if vehicles:
                                                print("\nVehículos:")
                                                for vehicle_url in vehicles:
                                                    vehicle_response = requests.get(vehicle_url)
                                                    if vehicle_response.status_code == 200:
                                                        vehicle_name = vehicle_response.json()["name"]
                                                        print(f" - {vehicle_name}")
                                                    else:
                                                        print(" - Error al obtener detalles del vehículo.")

                                            if films:
                                                print("\nEpisodios:")
                                                for film_url in films:
                                                    film_response = requests.get(film_url)
                                                    if film_response.status_code == 200:
                                                        film_title = film_response.json()["title"]
                                                        print(f" - {film_title}")
                                                    else:
                                                        print(" - Error al obtener detalles del episodio.")
                                            print()  # Agregar una línea en blanco después de las naves, vehículos y episodios
                                        else:
                                            print("No se encontraron naves, vehículos o episodios asociados con este personaje.")
                                        break
                            else:
                                print("Error al obtener información adicional desde la API secundaria.")

                        else:
                            print(f"Error al obtener detalles para {matching_characters[choice]['name']}")
                    else:
                        print("Selección inválida. Inténtalo de nuevo.")
                except ValueError:
                    print("Entrada no válida. Por favor, introduce un número o 'q' para salir.")
        else:
            print("No se encontraron personajes que coincidan con tu búsqueda.")

                                

