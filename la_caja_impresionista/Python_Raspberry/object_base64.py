import io, os
from google.cloud import vision
import pandas as pd
import base64
import json

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:/Users/pc1/Documents/Python/OjoDeVangogh-04b247a7603b.json"

IMAGE_NAME = f'C:/Users/pc1/Documents/Python/fotos/objetos.png'

base64_string3 = get_base64_encoded_image(IMAGE_NAME)

raw_data = {
  "requests":[
    {
      "image":{
        "content": base64_string3
      },
      "features": [
        {
          "type":"OBJECT_LOCALIZATION",
          "maxResults":1
        }
      ]
    }
  ]
}


json_data = json.dumps(raw_data, indent=2)

content = json.loads(json_data)

client = vision.ImageAnnotatorClient()
image_path = f'C:/Users/pc1/Documents/Python/fotos/objetos.png'

with open(image_path, 'rb') as image:
    content = image.read()
    response = client.annotate_image({'image': {'content': content}, 'features': [{'type': vision.enums.Feature.Type.OBJECT_LOCALIZATION}],})
    localized_object_annotations = response.localized_object_annotations

df = pd.DataFrame(columns=['name', 'score', 'bounding'])

for obj in localized_object_annotations:
    df = df.append(
        dict(
            name=obj.name,
            score=obj.score,
            bounding=obj.bounding_poly
        ),
        ignore_index=True)
    df = df.query('score >= 0.65')

    if (obj.score >= 0.65):

        promedio_x = (obj.bounding_poly.normalized_vertices[0].x + obj.bounding_poly.normalized_vertices[1].x)/2
        promedio_y = (obj.bounding_poly.normalized_vertices[0].y + obj.bounding_poly.normalized_vertices[2].y)/2

        if promedio_x < 0.33 and promedio_y < 0.33:
            print("El objeto está en la parte superior izquierda")

        elif promedio_x < 0.66 and promedio_y < 0.33:
            print("El objeto está en la parte superior centro")

        elif promedio_x <=1 and promedio_y < 0.33:
            print("El objeto está en la parte superior derecha")

        elif promedio_x < 0.33 and promedio_y < 0.66:
            print("El objeto está en la centro izquierda")

        elif promedio_x < 0.66 and promedio_y < 0.66:
            print("El objeto está en el centro")

        elif promedio_x <= 1 and promedio_y < 0.66:
            print("El objeto está en el centro derecha")

        elif promedio_x < 0.33 and promedio_y <= 1:
            print("El objeto está en la parte inferior izquierda")

        elif promedio_x < 0.66 and promedio_y < 0.66:
            print("El objeto está en la parte inferior centro")

        elif promedio_x <= 1 and promedio_y < 0.66:
            print("El objeto está en la parte inferior derecha")
        
print(df)