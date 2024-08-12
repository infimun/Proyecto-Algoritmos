import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('ruta_al_archivo.csv')

# Contar la cantidad de personajes nacidos en cada planeta
conteo_planetas = df['homeworld'].value_counts()

# Crear el gráfico
plt.figure(figsize=(10, 6))
conteo_planetas.plot(kind='bar')
plt.title('Cantidad de personajes nacidos en cada planeta')
plt.xlabel('Planeta')
plt.ylabel('Cantidad de personajes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()