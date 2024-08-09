'''
Programa de Sergio De La Corriea
(Lista de Películas de la saga)
'''

import csv

a_peliculas= open('C:/Python/csv/films.csv', 'r')


fila=1
lector_p = csv.reader(a_peliculas)
for fila in lector_p:
    if fila[0]!="id":
        print(f"id: {fila[0]}")
        print(f"titulo: {fila[1]}")
        print(f"fecha_estreno: {fila[2]}")
        print(f"director: {fila[3]}")
        print(f"produtor: {fila[4]}")
        print(f"opening: {fila[5]}")
        print(" ")
