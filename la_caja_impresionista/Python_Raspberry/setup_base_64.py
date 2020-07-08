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


  

   
