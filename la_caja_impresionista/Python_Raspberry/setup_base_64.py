import os
import io
from google.cloud import vision
import pandas as pd
import base64
import json


class SetupGoogleVision:

   def __init__(self,image_path,type):
      self.image_path = image_path
      self.type = type
      self.hola = ""
      raw_data = {
      "requests":[
         {
            "image":{
            "content": self.get_base64_encoded_image()
            },
            "features": [
            {
               "type": f"{self.image_path}",
               "maxResults":1
            }
            ]
         }
      ]
      }
   def get_base64_encoded_image(self,):
      with open(self.image_path, "rb") as img_file:
         return base64.b64encode(img_file.read()).decode('utf-8')

   def pedir_color(self, ):
      client = vision.ImageAnnotatorClient()
      with open(self.image_path, 'rb') as image:
         content = image.read()
         response = client.annotate_image({'image': {'content': content}, 'features': [{'type': vision.enums.Feature.Type.IMAGE_PROPERTIES}],}).image_properties_annotation
         dominant_colors = response.dominant_colors.colors
  

   
