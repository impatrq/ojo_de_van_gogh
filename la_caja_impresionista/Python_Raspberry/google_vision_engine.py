import os
import io
import pandas as pd
from google.cloud import vision
from gtts import gTTS
from textblob import TextBlob


class GoogleVisionEngine:

    def __init__(self, image_path):
        self.image_path = image_path

    def pedir_color(self, dataframe_colores):

        client = vision.ImageAnnotatorClient()
        dataframe_colores = dataframe_colores

        with open(self.image_path, 'rb') as image:
            content = image.read()
            response = client.annotate_image({'image': {'content': content}, 'features': [
                                             {'type': vision.enums.Feature.Type.IMAGE_PROPERTIES}], }).image_properties_annotation
            dominant_colors = response.dominant_colors.colors

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

            df_pixel_fraction = df_pixel_fraction.sort_values(
                ['pixel_fraction'], ascending=False).head(2)
            df_pixel_fraction = df_pixel_fraction.sort_values(
                ['score'], ascending=False).head(2)
        dif = df_pixel_fraction['score'][0] - df_pixel_fraction['score'][1]

        if (dif < 0.10):
            cont = 0
            for cont in [0, 1]:
                r = (df_pixel_fraction['r'][cont])
                g = (df_pixel_fraction['g'][cont])
                b = (df_pixel_fraction['b'][cont])

                self.rgb_to_name_query(dataframe_colores, r, g, b)

        else:
            r = (df_pixel_fraction['r'][0])
            g = (df_pixel_fraction['g'][0])
            b = (df_pixel_fraction['b'][0])
            self.rgb_to_name_query(dataframe_colores, r, g, b)

    def rgb_to_name_query(self, dataframe_colores, R, G, B):

        dataframe_colores = dataframe_colores
        R = R

        if R == 0:
            R += 0.1
        if G == 0:
            G += 0.1
        if B == 0:
            B += 0.1

        mx = max(R, G, B)
        mn = min(R, G, B)

        diferencia_min_max = mx - mn

        if mx <= 50 and diferencia_min_max <= 5:
            print("color: black")

        elif mn >= 230:
            print("color: blanco")

        else:
            dataframe_colores = dataframe_colores[[
                'Principal_color', 'CSS_name', 'R', 'G', 'B']]

            Resultado_busqueda_binaria = self.busqueda_binaria(
                dataframe_colores, 0, len(dataframe_colores[['R']]), R)

            dataframe_colores.query(
                'R == @Resultado_busqueda_binaria', inplace=True)
            dataframe_colores.query(
                'G/@G <=1.5 and G/@G >=0.65 ', inplace=True)
            dataframe_colores.query(
                'B/@B <=1.5 and B/@B >=0.65 ', inplace=True)

            if(dataframe_colores.empty == True):
                print("no se encontro una opcion en la base de datos")
                df_new_color = pd.DataFrame(
                    columns=['Principal_color', 'CSS_name', 'R', 'G', 'B'])
                df_new_color = df_new_color.append(
                    dict(
                        Principal_color="Clasificar",
                        CSS_name="Clasificar",
                        R=int(R),
                        G=int(G),
                        B=int(B),
                    ), ignore_index=True
                )
                dataframe_actualizado = dataframe_actualizado.append(
                    df_new_color, ignore_index=True)
                dataframe_actualizado.to_csv('Tabla_colores.csv', index=False)


    def leer_texto(self,):
      client = vision.ImageAnnotatorClient()
      with open(self.image_path, 'rb') as image:
         content = image.read()
         # construct an image instance
         # annotate Image Response
         response = client.annotate_image({'image': {'content': content}, 'features': [{'type': vision.enums.Feature.Type.TEXT_DETECTION}],})
         # returns TextAnnotation
         texts = response.text_annotations

      df_leer_texto = pd.DataFrame(columns=['locale', 'description'])

      for text in texts:
         df_leer_texto = df_leer_texto.append(
            dict(
                  locale=text.locale,
                  description=text.description
            ),
            ignore_index=True
         )

      texto = (df_leer_texto['description'][0])
      traduction = TextBlob(texto)
      idioma = str(traduction.detect_language())
      if idioma != 'es':
         traducido = str(traduction.translate(to = 'es'))
            
      with open('bread.txt', 'w') as f:
         f.write(traducido)

      with open('bread.txt') as f:
         lines = f.read()

         output = gTTS(text = lines, lang = 'es', slow = False)

         output.save('texto.mp3')

      os.system('mpg321 texto.mp3 &')
         


    def rgb_to_name_hsv(self, R, G, B):
        pass

    def busqueda_binaria(self, dataframe, comienzo, final, objetivo):

        if comienzo > final:
            return False
        medio = (comienzo + final) // 2

        if dataframe['R'][medio] <= objetivo * 1.5 and dataframe['R'][medio] >= objetivo * 0.65:
            print("objetivo")
            return objetivo

        elif dataframe['R'][medio] < objetivo:
            return self.busqueda_binaria(dataframe, medio + 1, final, objetivo)
        else:
            return self.busqueda_binaria(dataframe, comienzo, medio - 1, objetivo)

   
