import pandas as pd
from textblob import TextBlob
from google.cloud import vision

from clases.google_vision_engine import GoogleVisionEngine


class ObjectManager(GoogleVisionEngine):

    def get_response_api(self, ):

        # Se lee la imagen
        with open(self.image_path, 'rb') as image:
            # Leemos las cosas de la imagen y lo guardamos en contenido
            content = image.read()
            # Enviamos la peticion a la API de google con el formato JSON
            # especifico optimizar la velocidad de respuesta
            response = self.client.annotate_image({'image': {'content': content}, 'features': [
                {'type': vision.enums.Feature.Type.OBJECT_LOCALIZATION}], })
            # Guardamos la respuesta de la API
            respuesta_objeto_api = response.localized_object_annotations
            return (respuesta_objeto_api)

    def get_object(self, respuesta_objeto_api):

        # guardamos los valores obtenidos de la api
        respuesta_objeto_api = respuesta_objeto_api

        # Creamos un dataframe con la respuesta de la API
        df_reconocer_objeto = pd.DataFrame(
            columns=['name', 'score', 'vertices'])

        # Hacemos un for que analiza cada objeto de todos los que habia en la respuesta de la API
        for obj in respuesta_objeto_api:
            df_reconocer_objeto = df_reconocer_objeto.append(
                dict(
                    name=obj.name,  # Nombre del objeto
                    score=obj.score,  # Confiabilidad de que el objeto sea correcto
                    # Sirve para saber los vertices del objeto y poder ubicarlo
                    vertices=obj.bounding_poly.normalized_vertices
                ),
                ignore_index=True)

        # Descartamos los objetos de poca probabilidad de que sean correctos
        df_reconocer_objeto = df_reconocer_objeto.query('score >= 0.65')

        # Llamamos a la funcion que localize el lugar del objeto
        return(self.locate_object(df_reconocer_objeto))

    def locate_object(self, df_reconocer_objeto):

        # leo el dataframe con todos los objetos
        df_reconocer_objeto = df_reconocer_objeto

        # Leo el tamaño del dataframe
        largo_dataframe = len(df_reconocer_objeto)

        # Hacemos un for para analizar cada objeto
        for contador in range(largo_dataframe):

            # Se crea una variable para las puntas de los objetos
            vertices_objetos = df_reconocer_objeto.loc[contador, "vertices"]

            # se calcula el valor promedio de la lozalizacion del objeto en x
            promedio_x = (
                vertices_objetos[0].x + vertices_objetos[1].x)/2

            # se calcula el valor promedio de la lozalizacion del objeto en y
            promedio_y = (
                vertices_objetos[0].y + vertices_objetos[2].y)/2

            # Se crean las variables para saber la ubicacion de x e y
            ubicacion_x = ""
            ubicacion_y = ""

            # Se define la ubicacion del objeto en el eje y
            if promedio_y < 0.33:
                ubicacion_y = " la zona superior"
            elif promedio_y < 0.66:
                ubicacion_y = " el centro"
            else:
                ubicacion_y = " la zona inferior"

            # Se define la ubicacion del objeto en el eje x
            if promedio_x < 0.33:
                ubicacion_x = " izquierda"
            elif promedio_x < 0.66:
                ubicacion_x = " centro"
            else:
                ubicacion_x = " derecha"

            # Se guarda el valor recibido como objeto y se lo pasa a textblob
            nombre_objeto = TextBlob(df_reconocer_objeto.loc[contador, 'name'])

            # Se devuelve la localizacion del centro del objeto
            yield(nombre_objeto.translate(to='es') +
                  " está en" + ubicacion_y + ubicacion_x)
