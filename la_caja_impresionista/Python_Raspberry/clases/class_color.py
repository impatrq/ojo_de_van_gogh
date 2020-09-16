import os
import io
import pandas as pd
from google.cloud import vision

from google_vision_engine import GoogleVisionEngine
from texto_to_audio import texto_to_audio
from morse_colores import morse_colores


reproductor = texto_to_audio()
vibracion = morse_colores(22)


class Colors(GoogleVisionEngine):

    def __init__(self, image_path, client, dataframe_colores):

        # guardamos la tabla de colores patrones para el query
        super().__init__(image_path, client)
        self.dataframe_colores = dataframe_colores

    def llamar_api(self, ):

        # Leo la imagen
        with open(self.image_path, 'rb') as image:
            content = image.read()  # Leemos las cosas de la imagen y lo guardamos en contenido
            # Enviamos la peticion a la API de google con el formato JSON
            # especifico optimizar la velocidad de respuesta
            response = self.client.annotate_image({'image': {'content': content}, 'features': [
                {'type': vision.enums.Feature.Type.IMAGE_PROPERTIES}], }).image_properties_annotation
            dominant_colors = response.dominant_colors.colors  # Respuesta de colores

            return(dominant_colors)

    def obtener_color(self, dominant_colors):

        # guardamos los valores de la api
        dominant_colors = dominant_colors

        # Ciclo for para analizar cada color que nos dio la respuesta
        for color in dominant_colors:
            df_pixel_fraction = df_pixel_fraction.append(
                dict(
                    r=int(color.color.red),
                    g=int(color.color.green),
                    b=int(color.color.blue),
                    score=color.score,
                    pixel_fraction=color.pixel_fraction
                ),
                ignore_index=True)

        self.obtener_predominantes(df_pixel_fraction)

    def obtener_predominantes(self, df_pixel_fraction):

        # leo el dataframe con todos los valores
        df_pixel_fraction = df_pixel_fraction

        df_pixel_fraction = df_pixel_fraction.sort_values(
            ['pixel_fraction'], ascending=False).head(2)  # Agarramos los dos valores con mas predominancia en la pantalla
        df_pixel_fraction = df_pixel_fraction.sort_values(
            ['score'], ascending=False).head(2)  # Agarramos valores de confiabilidad altos

        # Nos fijamos si el primer color y el segundo son ambos confiables
        dif = df_pixel_fraction['score'][0] - df_pixel_fraction['score'][1]

        # Si los dos colores son confaibles usamos los dos
        if (dif < 0.10):
            cont = 0
            for cont in [0, 1]:
                r = (df_pixel_fraction['r'][cont])
                g = (df_pixel_fraction['g'][cont])
                b = (df_pixel_fraction['b'][cont])

                # Llamamos a la funcion que hace el query para el nombre de color
                self.obtener_nombre_color(r, g, b)

        # Si solo hay uno confiable usamos ese y ya esta
        else:
            r = (df_pixel_fraction['r'][0])
            g = (df_pixel_fraction['g'][0])
            b = (df_pixel_fraction['b'][0])

            # Llamamos a la funcion que hace el query para el nombre de color
            self.obtener_nombre_color(r, g, b)

        def obtener_nombre_color(R, G, B):

            # Guardamos la tabla de colores con nombres
            dataframe_colores = self.dataframe_colores

            # Guardamos los valores de R,G,B
            R = R
            G = G
            B = B

            # Se busca el color en la tabla con menos distancia del color que nos da la API
            minimo = 1000
            for i in range(len(dataframe_colores)):
                # Se calcula la distancia minima con valores absolutos
                distancia_color = abs(R - int(dataframe_colores.loc[i, "R"])) + abs(
                    G - int(dataframe_colores.loc[i, "G"])) + abs(B - int(dataframe_colores.loc[i, "B"]))
                # Si la distancia del color es menor o igual se guarda como minimo
                if(distancia_color <= minimo):
                    minimo = distancia_color
                    # Se guarda el nombre del color con menor distancia al buscado
                    nombre_color = dataframe_colores.loc[i, "Principal_color"]

            # Se reproduce el color por audio
            reproductor.audio(nombre_color)
            # Vibra de acuerdo al color
            vibracion.color_to_sonido(nombre_color)
