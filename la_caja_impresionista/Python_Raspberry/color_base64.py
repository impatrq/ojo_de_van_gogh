import os
import io
from google.cloud import vision
import pandas as pd
import base64
import json

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
      return base64.b64encode(img_file.read()).decode('utf-8')

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:/Users/pc1/Documents/Python/OjoDeVangogh-04b247a7603b.json'

IMAGE_NAME = f'C:/Users/pc1/Documents/Python/fotos/text.png'


client = vision.ImageAnnotatorClient()
image_path = f'C:/Users/pc1/Documents/Python/fotos/text.png'

with open(image_path, 'rb') as image:
  content = image.read()
  response = client.annotate_image({'image': {'content': content}, 'features': [{'type': vision.enums.Feature.Type.IMAGE_PROPERTIES}],}).image_properties_annotation
  dominant_colors = response.dominant_colors.colors

df = pd.DataFrame(columns=['r','g','b', 'pixel_fraction', 'score'])

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