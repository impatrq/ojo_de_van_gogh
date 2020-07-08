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
   def get_base64_encoded_image(self):
      with open(self.image_path, "rb") as img_file:
         return base64.b64encode(img_file.read()).decode('utf-8')

   
