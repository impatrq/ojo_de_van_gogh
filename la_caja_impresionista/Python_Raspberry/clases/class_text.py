import pandas as pd
from google.cloud import vision

from google_vision_engine import GoogleVisionEngine


class TextManager(GoogleVisionEngine):

    def get_response_api(self, ):

        # Se lee la imagen
        with open(self.image_path, 'rb') as image:
            # Leemos las cosas de la imagen y lo guardamos en contenido
            content = image.read()
            # Enviamos la peticion a la API de google con el formato JSON
            # especifico optimizar la velocidad de respuesta
            response = self.client.annotate_image({'image': {'content': content}, 'features': [
                {'type': vision.enums.Feature.Type.TEXT_DETECTION}], })

            respuesta_texto_api = response.text_annotations
            return (respuesta_texto_api)

    def get_text(self, respuesta_texto_api):

        # Guardamos los valores de la api
        respuesta_texto_api = respuesta_texto_api

        # Creamos el dataframe con el texto y el idioma
        df_leer_texto = pd.DataFrame(columns=['description'])

        # Por cada texto detectado lo unimos al dataframe
        for text in respuesta_texto_api:
            df_leer_texto = df_leer_texto.append(
                dict(
                    description=text.description
                ),
                ignore_index=True)

        # a la variable texto le metemos el contenido del texto
        texto_completo = (df_leer_texto['description'][0])

        return(texto_completo)
