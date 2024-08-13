import requests
from swapi_client import SWAPIClient
from models.movie import Movie
from models.species import Species
from models.planet import Planet
import os

def construir_mision():
    misiones = cargar_misiones_existentes()

    if len(misiones) >= 5:
        print("Ya hay 5 misiones, debes eliminar una de las ya existentes para construir una nueva.")
        return

    print("\nConstrucción de nueva misión:")

    # Solicitar nombre de la misión
    while True:
        nombre_mision = input("Introduce el nombre de la misión: ").strip().lower().replace(" ", "")
        if any(mision['nombre'].lower().replace(" ", "") == nombre_mision for mision in misiones):
            print("Ya existe una misión con ese nombre. Por favor, elige otro nombre.")
        else:
            break

    # Solicitar planeta destino
    planeta_destino = seleccionar_planeta()

    if planeta_destino:
        print(f"\nHas seleccionado el planeta {planeta_destino} como destino.")
    else:
        print("\nNo se seleccionó ningún planeta.")

    # Solicitar nave a utilizar con paginación
    nave_utilizada = seleccionar_nave()

    # Solicitar armas a utilizar (máximo 7)
    armas = obtener_lista_armas()
    print("\nArmas disponibles:")
    for i, arma in enumerate(armas):
        print(f"{i+1}. {arma}")

    armas_utilizadas = seleccionar_multiples_opciones("\nSelecciona los números de las armas a utilizar (máximo 7, separadas por comas): ", armas, 7)

    # Solicitar integrantes de la misión (máximo 7) con selección múltiple y paginación
    integrantes = []
    while len(integrantes) < 7:
        personajes_disponibles = obtener_lista_personajes()
        pagina_actual = 1
        max_paginas = (len(personajes_disponibles) + 9) // 10  # Total de páginas

        while True:
            inicio = (pagina_actual - 1) * 10
            fin = inicio + 10
            personajes_pagina = personajes_disponibles[inicio:fin]

            print("\nPersonajes disponibles:")
            for i, personaje in enumerate(personajes_pagina, start=inicio + 1):
                print(f"{i}. {personaje}")

            seleccion = input(f"\nSelecciona el/los número(s) del personaje (restantes: {7 - len(integrantes)}, separados por comas), escribe 'next' para la siguiente página, 'prev' para la anterior, o 'next part' para finalizar la selección: ")

            if seleccion.lower() == 'next' and pagina_actual < max_paginas:
                pagina_actual += 1
            elif seleccion.lower() == 'prev' and pagina_actual > 1:
                pagina_actual -= 1
            elif seleccion.lower() == 'next part':
                break
            else:
                try:
                    seleccion_indices = [int(s) - 1 for s in seleccion.split(',')]
                    if all(inicio <= s < fin for s in seleccion_indices):
                        for s in seleccion_indices:
                            if len(integrantes) < 7:
                                integrantes.append(personajes_disponibles[s])
                            else:
                                break
                        if len(integrantes) == 7:
                            break
                    else:
                        print("Selección inválida. Inténtalo de nuevo.")
                except ValueError:
                    print("Entrada no válida. Por favor, introduce números separados por comas o 'next part' para finalizar.")

        if len(integrantes) == 7 or seleccion.lower() == 'next part':
            break

    # Crear la misión
    mision = {
        "nombre": nombre_mision,
        "planeta_destino": planeta_destino,
        "nave_utilizada": nave_utilizada,
        "armas_utilizadas": armas_utilizadas,
        "integrantes": integrantes
    }

    misiones.append(mision)
    guardar_misiones(misiones)
    print(f"\nMisión '{nombre_mision}' creada y guardada exitosamente.\n")

def visualizar_misiones():
    misiones = cargar_misiones_existentes()

    if not misiones:
        print("No hay misiones guardadas.")
        return

    print("\nMisiones guardadas:")
    for i, mision in enumerate(misiones):
        print(f"Misión {i+1}:")
        print(f"  Nombre: {mision['nombre']}")

    while True:
        seleccion = input("\nSelecciona una misión por número para ver detalles (o escribe 'back' para regresar): ")

        if seleccion.lower() == 'back':
            break
        try:
            seleccion = int(seleccion) - 1
            if 0 <= seleccion < len(misiones):
                mision = misiones[seleccion]
                print(f"\nDetalles de la Misión {seleccion + 1}:")
                print(f"  Nombre: {mision['nombre']}")
                print(f"  Planeta destino: {mision['planeta_destino']}")
                print(f"  Nave utilizada: {mision['nave_utilizada']}")
                print(f"  Armas utilizadas: {', '.join(mision['armas_utilizadas'])}")
                print(f"  Integrantes: {', '.join(mision['integrantes'])}")
                
                opcion = input("\nEscribe 'mod' para modificar, 'del' para eliminar, o 'back' para regresar: ").strip().lower()

                if opcion == 'mod':
                    modificar_mision(misiones, seleccion)
                    guardar_misiones(misiones)
                    print(f"Misión {seleccion + 1} modificada exitosamente.")
                    break
                elif opcion == 'del':
                    eliminar_mision(misiones, seleccion)
                    guardar_misiones(misiones)
                    print(f"Misión {seleccion + 1} eliminada exitosamente.")
                    break
                elif opcion == 'back':
                    break
                else:
                    print("Opción inválida.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número válido o 'back' para regresar.")

    visualizar_misiones()

def modificar_mision(misiones, index):
    mision = misiones[index]

    print("\nModificar misión:")

    # Modificar armas
    armas = obtener_lista_armas()
    print("\nArmas disponibles:")
    for i, arma in enumerate(armas):
        print(f"{i+1}. {arma}")

    armas_utilizadas = seleccionar_multiples_opciones("\nSelecciona los números de las armas a utilizar (máximo 7, separadas por comas): ", armas, 7)
    mision["armas_utilizadas"] = armas_utilizadas

    # Modificar integrantes
    integrantes = []
    while len(integrantes) < 7:
        personajes_disponibles = obtener_lista_personajes()
        pagina_actual = 1
        max_paginas = (len(personajes_disponibles) + 9) // 10  # Total de páginas

        while True:
            inicio = (pagina_actual - 1) * 10
            fin = inicio + 10
            personajes_pagina = personajes_disponibles[inicio:fin]

            print("\nPersonajes disponibles:")
            for i, personaje in enumerate(personajes_pagina, start=inicio + 1):
                print(f"{i}. {personaje}")

            seleccion = input(f"\nSelecciona el/los número(s) del personaje (restantes: {7 - len(integrantes)}, separados por comas), escribe 'next' para la siguiente página, 'prev' para la anterior, o 'next part' para finalizar la selección: ")

            if seleccion.lower() == 'next' and pagina_actual < max_paginas:
                pagina_actual += 1
            elif seleccion.lower() == 'prev' and pagina_actual > 1:
                pagina_actual -= 1
            elif seleccion.lower() == 'next part':
                break
            else:
                try:
                    seleccion_indices = [int(s) - 1 for s in seleccion.split(',')]
                    if all(inicio <= s < fin for s in seleccion_indices):
                        for s in seleccion_indices:
                            if len(integrantes) < 7:
                                integrantes.append(personajes_disponibles[s])
                            else:
                                break
                        if len(integrantes) == 7:
                            break
                    else:
                        print("Selección inválida. Inténtalo de nuevo.")
                except ValueError:
                    print("Entrada no válida. Por favor, introduce números separados por comas o 'next part' para finalizar.")

        if len(integrantes) == 7 or seleccion.lower() == 'next part':
            break

    mision["integrantes"] = integrantes

def eliminar_mision(misiones, index):
    misiones.pop(index)
    for i, mision in enumerate(misiones):
        mision["numero"] = i + 1

def cargar_misiones():
    misiones = cargar_misiones_existentes()

    if not misiones:
        print("No hay misiones para cargar.")
        return

    print("\nMisiones cargadas:")
    for i, mision in enumerate(misiones):
        print(f"\nMisión {i+1}:")
        print(f"  Nombre: {mision['nombre']}")
        print(f"  Planeta destino: {mision['planeta_destino']}")
        print(f"  Nave utilizada: {mision['nave_utilizada']}")
        print(f"  Armas utilizadas: {', '.join(mision['armas_utilizadas'])}")
        print(f"  Integrantes: {', '.join(mision['integrantes'])}")
    print()  # Espacio al final para separar la salida de las misiones cargadas


def cargar_misiones_existentes():
    if os.path.exists("misiones.txt"):
        with open("misiones.txt", "r") as file:
            misiones = eval(file.read())  # Usar eval para convertir el string en una lista de diccionarios
    else:
        misiones = []

    return misiones

def guardar_misiones(misiones):
    with open("misiones.txt", "w") as file:
        file.write(str(misiones))

def obtener_lista_planetas():
    all_planets = []
    page = 1

    # Obtener todos los planetas desde la API
    while True:
        response = requests.get(f"https://www.swapi.tech/api/planets?page={page}&limit=10")
        if response.status_code == 200:
            response_data = response.json()
            planets_data = response_data["results"]
            all_planets.extend([planet["name"] for planet in planets_data])
            
            # Verificar si hay más páginas
            if response_data["next"] is None:
                break
            page += 1
        else:
            print("Error al obtener planetas.")
            return []

    return all_planets

def seleccionar_planeta():
    planetas = obtener_lista_planetas()
    if not planetas:
        print("No se pudo obtener la lista de planetas.")
        return None

    planetas_por_pagina = 10
    total_planetas = len(planetas)
    pagina_actual = 1

    while True:
        inicio = (pagina_actual - 1) * planetas_por_pagina
        fin = inicio + planetas_por_pagina

        print("\nPlanetas disponibles:")
        for index, planeta in enumerate(planetas[inicio:fin], start=inicio + 1):
            print(f"{index}. {planeta}")

        opciones = "\nSelecciona un planeta por número"
        if pagina_actual > 1:
            opciones += " o escribe 'prev' para ver opciones anteriores"
        if fin < total_planetas:
            opciones += " o 'next' para ver más opciones"
        opciones += " (o 'q' para cancelar): "

        eleccion = input(opciones)

        if eleccion.lower() == 'q':
            return None
        elif eleccion.lower() == 'next' and fin < total_planetas:
            pagina_actual += 1
        elif eleccion.lower() == 'prev' and pagina_actual > 1:
            pagina_actual -= 1
        else:
            try:
                eleccion = int(eleccion) - 1
                if inicio <= eleccion < fin:
                    return planetas[eleccion]
                else:
                    print("Selección inválida. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número o 'q' para cancelar.")

def obtener_lista_naves():
    all_starships = []
    page = 1

    # Obtener todas las naves desde la API
    while True:
        response = requests.get(f"https://www.swapi.tech/api/starships?page={page}&limit=10")
        if response.status_code == 200:
            response_data = response.json()
            starships_data = response_data["results"]
            all_starships.extend([starship["name"] for starship in starships_data])
            
            # Verificar si hay más páginas
            if response_data["next"] is None:
                break
            page += 1
        else:
            print("Error al obtener naves.")
            return []

    return all_starships

def seleccionar_nave():
    naves_disponibles = obtener_lista_naves()
    pagina_actual = 1
    max_paginas = (len(naves_disponibles) + 9) // 10  # Total de páginas

    while True:
        inicio = (pagina_actual - 1) * 10
        fin = inicio + 10
        naves_pagina = naves_disponibles[inicio:fin]

        print("\nNaves disponibles:")
        for i, nave in enumerate(naves_pagina, start=inicio + 1):
            print(f"{i}. {nave}")

        seleccion = input("\nSelecciona el número de la nave, escribe 'next' para la siguiente página, 'prev' para la anterior, o 'q' para cancelar: ")

        if seleccion.lower() == 'next' and pagina_actual < max_paginas:
            pagina_actual += 1
        elif seleccion.lower() == 'prev' and pagina_actual > 1:
            pagina_actual -= 1
        elif seleccion.lower() == 'q':
            return None
        else:
            try:
                seleccion = int(seleccion) - 1
                if inicio <= seleccion < fin:
                    return naves_disponibles[seleccion]
                else:
                    print("Selección inválida. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número o 'q' para cancelar.")

def obtener_lista_armas():
    # Simulación de obtención de armas
    return [
        "Blaster", 
        "Sable de luz", 
        "Rifle de francotirador", 
        "Granada térmica",
        "Lanzallamas", 
        "Arco láser",
        "Electrostaff", 
        "Rayo destructor", 
        "Pistola de iones", 
        "Blaster pesado"
    ]

def obtener_lista_personajes():
    all_characters = []
    page = 1

    # Obtener todos los personajes desde la API
    while True:
        response = requests.get(f"https://www.swapi.tech/api/people?page={page}&limit=10")
        if response.status_code == 200:
            response_data = response.json()
            characters_data = response_data["results"]
            all_characters.extend([character["name"] for character in characters_data])
            
            # Verificar si hay más páginas
            if response_data["next"] is None:
                break
            page += 1
        else:
            print("Error al obtener personajes.")
            return []

    return all_characters

def seleccionar_personaje():
    personajes = obtener_lista_personajes()
    if not personajes:
        print("No se pudo obtener la lista de personajes.")
        return None

    personajes_por_pagina = 10
    total_personajes = len(personajes)
    pagina_actual = 1

    while True:
        inicio = (pagina_actual - 1) * personajes_por_pagina
        fin = inicio + personajes_por_pagina

        print("\nPersonajes disponibles:")
        for index, personaje in enumerate(personajes[inicio:fin], start=inicio + 1):
            print(f"{index}. {personaje}")

        opciones = "\nSelecciona un personaje por número"
        if pagina_actual > 1:
            opciones += " o escribe 'prev' para ver opciones anteriores"
        if fin < total_personajes:
            opciones += " o 'next' para ver más opciones"
        opciones += " (o 'q' para cancelar): "

        eleccion = input(opciones)

        if eleccion.lower() == 'q':
            return None
        elif eleccion.lower() == 'next' and fin < total_personajes:
            pagina_actual += 1
        elif eleccion.lower() == 'prev' and pagina_actual > 1:
            pagina_actual -= 1
        else:
            try:
                eleccion = int(eleccion) - 1
                if inicio <= eleccion < fin:
                    return personajes[eleccion]
                else:
                    print("Selección inválida. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número o 'q' para cancelar.")

def seleccionar_opcion(mensaje, opciones):
    while True:
        try:
            seleccion = int(input(mensaje)) - 1
            if 0 <= seleccion < len(opciones):
                return opciones[seleccion]
            else:
                print("Selección inválida. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

def seleccionar_multiples_opciones(mensaje, opciones, max_opciones=None):
    while True:
        seleccion = input(mensaje).split(',')
        seleccion = [opcion.strip() for opcion in seleccion]
        try:
            if max_opciones and len(seleccion) > max_opciones:
                print(f"Puedes seleccionar un máximo de {max_opciones} opciones. Inténtalo de nuevo.")
                continue
            seleccion_indices = [int(opcion) - 1 for opcion in seleccion]
            if all(0 <= indice < len(opciones) for indice in seleccion_indices):
                return [opciones[indice] for indice in seleccion_indices]
            else:
                print("Selección inválida. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce números separados por comas.")