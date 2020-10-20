import pandas as pd
from google.cloud import vision

from clases.google_vision_engine import GoogleVisionEngine


class ColorsManager(GoogleVisionEngine):

    def __init__(self, image_path, client, dataframe_colores):

        # guardamos la tabla de colores patrones para el query
        super().__init__(image_path, client)
        self.dataframe_colores = dataframe_colores

    def get_response_api(self, ):

        # Leo la imagen
        with open(self.image_path, 'rb') as image:
            content = image.read()  # Leemos las cosas de la imagen y lo guardamos en contenido
            # Enviamos la peticion a la API de google con el formato JSON
            # especifico optimizar la velocidad de respuesta
            response = self.client.annotate_image({'image': {'content': content}, 'features': [
                {'type': vision.enums.Feature.Type.IMAGE_PROPERTIES}], }).image_properties_annotation
            respuesta_rgb_api = response.dominant_colors.colors  # Respuesta de colores

            return(respuesta_rgb_api)

    def get_color(self, respuesta_rgb_api):

        # guardamos los valores de la api
        respuesta_rgb_api = respuesta_rgb_api

        # Creo dataframe para guardar los valores de la api
        df_pixel_fraction = pd.DataFrame(
            columns=['r', 'g', 'b', 'score', 'pixel_fraction'])

        # Ciclo for para analizar cada color que nos dio la respuesta
        for color in respuesta_rgb_api:
            df_pixel_fraction = df_pixel_fraction.append(
                dict(
                    r=int(color.color.red),
                    g=int(color.color.green),
                    b=int(color.color.blue),
                    score=color.score,
                    pixel_fraction=color.pixel_fraction
                ),
                ignore_index=True)

        return(self.get_predominant_colors(df_pixel_fraction))

    def get_predominant_colors(self, df_pixel_fraction):

        # leo el dataframe con todos los valores
        df_pixel_fraction = df_pixel_fraction

        df_pixel_fraction = df_pixel_fraction.sort_values(
            ['pixel_fraction'], ascending=False).head(2)  # Agarramos los dos valores con mas predominancia en la pantalla
        df_pixel_fraction = df_pixel_fraction.sort_values(
            ['score'], ascending=False).head(2)  # Agarramos valores de confiabilidad altos

        # Reiniciamos el indice del dataframe
        df_pixel_fraction = df_pixel_fraction.reset_index(drop=True)

        # Nos fijamos si el primer color y el segundo son ambos confiables
        dif = df_pixel_fraction['score'][0] - df_pixel_fraction['score'][1]

        # Si los dos colores son confaibles usamos los dos
        if (dif < 0.10):
            for cont in [0, 1]:
                self.r = (df_pixel_fraction['r'][cont])
                self.g = (df_pixel_fraction['g'][cont])
                self.b = (df_pixel_fraction['b'][cont])

                # Llamamos a la funcion que hace el query para el nombre de color
                yield(self.get_color_name(self.r, self.g, self.b))

        # Si solo hay uno confiable usamos ese y ya esta
        else:
            self.r = (df_pixel_fraction['r'][0])
            self.g = (df_pixel_fraction['g'][0])
            self.b = (df_pixel_fraction['b'][0])

            # Llamamos a la funcion que hace el query para el nombre de color
            yield(self.get_color_name(self.r, self.g, self.b))

    def get_color_name(self, R, G, B):

        # Guardamos la tabla de colores con nombres
        dataframe_colores = self.dataframe_colores

        # Guardamos los valores de R,G,B
        self.r = R
        self.g = G
        self.b = B

        # Se busca el color en la tabla con menos distancia del color que nos da la API
        minimo = 1000
        for i in range(len(dataframe_colores)):
            # Se calcula la distancia minima con valores absolutos
            distancia_color = abs(self.r - int(dataframe_colores.loc[i, "R"])) + abs(
                self.g - int(dataframe_colores.loc[i, "G"])) + abs(self.b - int(dataframe_colores.loc[i, "B"]))
            # Si la distancia del color es menor o igual se guarda como minimo
            if(distancia_color <= minimo):
                minimo = distancia_color
                # Se guarda el nombre del color con menor distancia al buscado
                nombre_color = dataframe_colores.loc[i, "Principal_color"]

        # Se devuelve el nombre del color
        return (nombre_color)
