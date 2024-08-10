import os
def limpiar_pantalla():
    if os.name == 'nt':  # Verifica si estamos en Windows
        os.system('cls')  # Limpia la pantalla
    else:
        os.system('clear') # Limpia la pantalla