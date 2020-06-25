import io, os
from google.cloud import vision
from gtts import gTTS
from textblob import TextBlob
import pandas as pd
from detector_object import detector_object

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"OjoDeVangogh-04b247a7603b.json"
client = vision.ImageAnnotatorClient()

file_name = 'label_sample2.jpg'
image_path = f'/home/pi/label_detection/{file_name}'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)
response = client.object_localization(image=image)
localized_object_annotations = response.localized_object_annotations

df = pd.DataFrame(columns=['name', 'score'])

detector_de_objeto = detector_object()

detector_de_objeto.object_recognition(localized_object_annotations, df)