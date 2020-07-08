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
      self.dataframe_colores = dataframe_colores
      with open(self.image_path, 'rb') as image:
         content = image.read()
         response = client.annotate_image({'image': {'content': content}, 'features': [{'type': vision.enums.Feature.Type.IMAGE_PROPERTIES}],}).image_properties_annotation
         dominant_colors = response.dominant_colors.colors


  

   
