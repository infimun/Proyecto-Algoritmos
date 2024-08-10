import subprocess
import limpiarp
import msvcrt
import os

def menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1. Lista de peliculas de la Saga")
        print("2. Opción 2")
        print("3. Opción 3")
        print("4. Opción 4")
        print("5. Opción 5")
        print("0. Salir")

        seleccion = input("Elige una opción (1-5, o 0 para salir): ")

        if seleccion == '1':
            limpiarp.limpiar_pantalla()
            print("Por favor esperar a que termine el proceso...")
            subprocess.run(["python", ruta+"/sergio SWAPI(A).py"])
            print("Presione cualquier tecla para continuar...")
            msvcrt.getch()
        elif seleccion == '2':
            limpiarp.limpiar_pantalla()
            print("Por favor esperar a que termine el proceso...")
            subprocess.run(["python", ruta+"/Sergio SWAPI(B).py"])
            print("Presione cualquier tecla para continuar...")
            msvcrt.getch()
        elif seleccion == '3':
            opcion_3()
        elif seleccion == '4':
            opcion_4()
        elif seleccion == '5':
            opcion_5()
        elif seleccion == '0':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

ruta=os.path.dirname(os.path.abspath(__file__))
if __name__ == "__main__":
    menu_principal()