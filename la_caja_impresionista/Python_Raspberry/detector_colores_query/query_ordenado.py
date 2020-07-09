import pandas as pd
import numpy as np
import array

# Con esta vamos filtrando la tabla
dataframe = pd.read_csv('Tabla_colores.csv')
# Esta variable va a ir guardando los nuevos valores
dataframe_actualizado = pd.read_csv('Tabla_colores.csv')

color_prueba = [2, 2, 2]


def busqueda_binaria(dataframe, comienzo, final, objetivo):

    print("entre")

    if comienzo > final:
        return "hola"
    medio = (comienzo + final) // 2

    if dataframe['R'][medio] <= objetivo * 1.5 and dataframe['R'][medio] >= objetivo * 0.65:
        print("objetivo")
        return objetivo
    elif dataframe['R'][medio] < objetivo:
        return busqueda_binaria(dataframe, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(dataframe, comienzo, medio - 1, objetivo)


if color_prueba[0] == 0:
    color_prueba[0] += 0.1
if color_prueba[1] == 0:
    color_prueba[1] += 0.1
if color_prueba[2] == 0:
    color_prueba[2] += 0.1

mx = max(color_prueba[0], color_prueba[1], color_prueba[2])
mn = min(color_prueba[0], color_prueba[1], color_prueba[2])

diferencia_min_max = mx - mn


if mx <= 50 and diferencia_min_max <= 5:
    print("color: black")

elif mn >= 230:
    print("color: blanco")

else:
    pass


dataframe = dataframe[['Principal_color', 'CSS_name', 'R', 'G', 'B']]


Resultado_busqueda_binaria = busqueda_binaria(
    dataframe, 0, len(dataframe[['R']]), color_prueba[0])

dataframe.query('R == @Resultado_busqueda_binaria', inplace=True)
dataframe.query(
    'G/@color_prueba[1] <=1.5 and G/@color_prueba[1] >=0.65 ', inplace=True)
dataframe.query(
    'B/@color_prueba[2] <=1.5 and B/@color_prueba[2] >=0.65 ', inplace=True)


if(dataframe.empty == True):
    print("no se encontro una opcion en la base de datos")
    df = pd.DataFrame(columns=['Principal_color', 'CSS_name', 'R', 'G', 'B'])
    df = df.append(
        dict(
            Principal_color="Clasificar",
            CSS_name="Clasificar",
            R=int(color_prueba[0]),
            G=int(color_prueba[1]),
            B=int(color_prueba[2]),
        ), ignore_index=True
    )
    dataframe_actualizado = dataframe_actualizado.append(df, ignore_index=True)
    dataframe_actualizado = dataframe_actualizado.sort_values(
        ['R'], ascending=True)
    dataframe_actualizado.to_csv('Tabla_colores.csv', index=False)
    print(dataframe_actualizado)


print(dataframe)
