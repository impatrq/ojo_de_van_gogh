import os, io
from google.cloud import vision
import pandas as pd
import base64
import json

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:/Users/pc1/Documents/Python/OjoDeVangogh-04b247a7603b.json"

IMAGE_NAME = f'C:/Users/pc1/Documents/Python/fotos/text.png'

base64_string3 = get_base64_encoded_image(IMAGE_NAME)

raw_data = {
  "requests":[
    {
      "image":{
        "content": base64_string3
      },
      "features": [
        {
          "type":"TEXT_DETECTION",
          "maxResults":1
        }
      ]
    }
  ]
}


json_data = json.dumps(raw_data, indent=2)

content = json.loads(json_data)

client = vision.ImageAnnotatorClient()
image_path = f'C:/Users/pc1/Documents/Python/fotos/text.png'

with open(image_path, 'rb') as image:
    content = image.read()
    # construct an image instance
    # annotate Image Response
    response = client.annotate_image({'image': {'content': content}, 'features': [{'type': vision.enums.Feature.Type.TEXT_DETECTION}],})
    # returns TextAnnotation
    texts = response.text_annotations

df = pd.DataFrame(columns=['locale', 'description'])

for text in texts:
    df = df.append(
        dict(
            locale=text.locale,
            description=text.description
        ),
        ignore_index=True
    )

print(df['description'][0])