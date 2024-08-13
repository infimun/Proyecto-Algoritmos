from center import listar_peliculas
from center import seleccionar_especie
from center import listar_planetas
from center import buscar_personaje

def main():
    while True:
        print("""
   ______________________________________________________________________
  |:..                                                      ``:::%%%%%%HH|
  |%%%:::::..                 M    e    n    u                 `:::::%%%%|
  |HH%%%%%:::::....._______________________________________________::::::|
""")
        print("\nSelecciona uan opcion:")
        print("1. Listar Peliculas")
        print("2. Seleccionar y Ver Detalles de Especies")
        print("3. Listar Planetas")
        print("4. Buscar Personaje")
        print("5. Salir")
        choice = input("\nIntroduce tu eleccion: ")

        if choice == '1':
            listar_peliculas()
        elif choice == '2':
            seleccionar_especie()
        elif choice == '3':
            listar_planetas()
        elif choice == '4':
            buscar_personaje()
        elif choice== '5':
            break
        else:
            print("Eleccion invalida. Por favor vuelva a intentar.")


if __name__ == "__main__":
    main()
