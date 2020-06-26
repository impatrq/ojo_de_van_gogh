import pandas as pd
import numpy as np
import array

dataframe = pd.read_csv('Tabla_colores.csv')




color_prueba=[239, 127, 26]

if color_prueba[0] == 0:
    color_prueba[0] += 0.1
if color_prueba[1] == 0:
    color_prueba[1] += 0.1
if color_prueba[2] == 0:
    color_prueba[2] += 0.1

mx = max(color_prueba[0]  , color_prueba[1]  , color_prueba[2])
mn = min(color_prueba[0]  , color_prueba[1]  , color_prueba[2])

diferencia_min_max= mx - mn


if mx <= 50 and diferencia_min_max <= 5 :
    print("color: black")

elif mn >= 230 : 
    print("color: blanco")

else:
    pass





dataframe=dataframe[['Principal_color', 'CSS_name', 'R', 'G', 'B']]



df=dataframe.query(
    'R/@color_prueba[0] <=1.34 and R/@color_prueba[0] >=0.73 ')
df=dataframe.query(
    'G/@color_prueba[1] <=1.34 and G/@color_prueba[1] >=0.73 ')
df=dataframe.query(
    'B/@color_prueba[2] <=1.34 and B/@color_prueba[2] >=0.73 ')


if(df.empty()):
    print("no se encontro una opcion en la base de datos")
    



print(dataframe)
