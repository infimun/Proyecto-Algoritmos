import pandas as pd
import csv
import os 

"""
Estadisticas sobre naves, promedios y moda
"""
def Estadisticas_sobre_Naves():


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
