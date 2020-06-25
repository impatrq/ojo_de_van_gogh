import os
import io
from google.cloud import vision
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:/Users/pc1/Documents/Python/OjoDeVangogh-04b247a7603b.json'
client = vision.ImageAnnotatorClient()

file_name = 'control_remoto.png'
image_path = f'C:/Users/pc1/Documents/Python/{file_name}'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)
response = client.image_properties(image=image).image_properties_annotation
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
        print (r,g,b)
    
else: 
    print (df['r'][0])
    print (df['g'][0])
    print (df['b'][0])