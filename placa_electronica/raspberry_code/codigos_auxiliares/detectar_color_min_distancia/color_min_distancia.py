import pandas as pd
import numpy as np
import array
import time

# Se toma el tiempo de arranque
start = time.time()

# Se lee la tabla de colores
dataframe = pd.read_csv('colores.csv')

# Se indica el color que se busca
color_prueba = [100, 100, 100]

# Se busca el color en la tabla con menos distancia del color buscado
minimo = 1000
for i in range(len(dataframe)):
    # Se calcula la distancia minima con valores absolutos
    distancia_color = abs(color_prueba[0] - int(dataframe.loc[i, "R"])) + abs(color_prueba[1] -
                                                                              int(dataframe.loc[i, "G"])) + abs(color_prueba[2] - int(dataframe.loc[i, "B"]))
    # Si la distancia del color es menor o igual se guarda como minimo
    if(distancia_color <= minimo):
        minimo = distancia_color
        # Se guarda el nombre del color con menor distancia al buscado
        nombre_color = dataframe.loc[i, "Principal_color"]

# Se muestra el color
print(nombre_color)

# Se muestra cuanto tiempo tardo el programa en dar respuesta
print(time.time()-start)
