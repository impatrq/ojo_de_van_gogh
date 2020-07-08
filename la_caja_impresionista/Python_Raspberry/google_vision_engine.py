import os
import io
from google.cloud import vision
import pandas as pd
import base64
import json


class GoogleVisionEngine:

   def __init__(self,image_path ,type ):
      self.image_path = image_path
      self.type = type
      



   def pedir_color(self, dataframe_colores):
      
      client = vision.ImageAnnotatorClient()
      self.df = dataframe_colores
      with open(self.image_path, 'rb') as image:
         content = image.read()
         response = client.annotate_image({'image': {'content': content}, 'features': [{'type': vision.enums.Feature.Type.IMAGE_PROPERTIES}],}).image_properties_annotation
         dominant_colors = response.dominant_colors.colors
   
      for color in dominant_colors:
         df = df.append(
            dict(
                  r = int(color.color.red),
                  g = int(color.color.green),
                  b = int(color.color.blue),
                  score=color.score,
                  pixel_fraction=color.pixel_fraction
            ),
            ignore_index=True)

         df = df.sort_values(['pixel_fraction'],ascending=False).head(2)
         df = df.sort_values(['score'],ascending=False).head(2)
      dif = df['score'][0] - df['score'][1]

      if (dif < 0.10):
         cont = 0
         for cont in [0,1]:
            r = (df['r'][cont])
            g = (df['g'][cont])
            b = (df['b'][cont])
            print (df)
         
      else: 
         print (df['r'][0])
         print (df['g'][0])
         print (df['b'][0])
   
   def rgb_to_name_query(self,R,G,B):
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
         pass


      dataframe = dataframe[['Principal_color', 'CSS_name', 'R', 'G', 'B']]

      Resultado_busqueda_binaria = busqueda_binaria(dataframe,0 , len(dataframe[['R']]),color_prueba[0]) 

      dataframe.query('R == @Resultado_busqueda_binaria',inplace=True)
      dataframe.query(
         'G/@color_prueba[1] <=1.5 and G/@color_prueba[1] >=0.65 ',inplace= True)
      dataframe.query(
         'B/@color_prueba[2] <=1.5 and B/@color_prueba[2] >=0.65 ', inplace= True)


      if(dataframe.empty == True):
         print("no se encontro una opcion en la base de datos")
         df = pd.DataFrame(columns=['Principal_color', 'CSS_name', 'R', 'G', 'B'])
         df= df.append(
            dict(
                  Principal_color="Clasificar",
                  CSS_name="Clasificar",
                  R=int(color_prueba[0]),
                  G=int(color_prueba[1]),
                  B=int(color_prueba[2]),
            ), ignore_index=True
         )
         dataframe_actualizado=dataframe_actualizado.append(df, ignore_index=True)
         dataframe_actualizado.to_csv('Tabla_colores.csv',index=False)
         print (dataframe_actualizado)
         


      print(dataframe)

   def rgb_to_name_hsv(self,R,G,B):
      pass
   

   def busqueda_binaria(self,dataframe, comienzo, final, objetivo):

      
      print("entre")




      if comienzo > final:
         return "hola"
      medio = (comienzo + final) // 2

      if dataframe['R'][medio] <= objetivo * 1.5 and dataframe['R'][medio] >= objetivo * 0.65:
         print("objetivo")
         return objetivo
      elif dataframe['R'][medio] < objetivo:
         return self.busqueda_binaria(dataframe, medio + 1, final, objetivo)
      else:
         return self.busqueda_binaria(dataframe, comienzo, medio - 1, objetivo)   
         
   



  

   
