import pandas as pd
import numpy as np
import array

dataframe = pd.read_csv('Tabla_colores.csv')

color_prueba = [230, 210, 40]

if color_prueba[0] == 0:
    color_prueba[0] += 0.1
if color_prueba[1] == 0:
    color_prueba[1] += 0.1
if color_prueba[2] == 0:
    color_prueba[2] += 0.1

dataframe = dataframe[['Principal_color', 'CSS_name', 'R', 'G', 'B']]

dataframe = dataframe.query(
    'R/@color_prueba[0] <=1.34 and R/@color_prueba[0] >=0.73 ')
dataframe = dataframe.query(
    'G/@color_prueba[1] <=1.34 and G/@color_prueba[1] >=0.73 ')
dataframe = dataframe.query(
    'B/@color_prueba[2] <=1.34 and B/@color_prueba[2] >=0.73 ')


print(dataframe)
