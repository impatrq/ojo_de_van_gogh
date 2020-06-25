import os, io, picamera
from google.cloud import vision
import pandas as pd
from gtts import gTTS
from textblob import TextBlob

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"OjoDeVangogh-04b247a7603b.json"
client = vision.ImageAnnotatorClient()

def takephoto():
    camera = picamera.PiCamera()
    camera.capture('read.jpg')
takephoto()

file_name = 'read2.jpg'
image_path = f'/home/pi/txtdetect/{file_name}'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

# construct an iamge instance
image = vision.types.Image(content=content)

# annotate Image Response
response = client.text_detection(image=image)  # returns TextAnnotation
df = pd.DataFrame(columns=['locale', 'description'])

texts = response.text_annotations
for text in texts:
    df = df.append(
        dict(
            locale=text.locale,
            description=text.description
        ),
        ignore_index=True
    )

print(df['description'][0])

texto = (df['description'][0])

def traduccion(texto):
    traduction = TextBlob(texto)
    idioma = str(traduction.detect_language())
    if idioma != 'es':
        traducido = traduction.translate(to = 'es')
        return traducido

tr = str(traduccion(texto))

with open('bread.txt', 'w') as f:
        f.write(tr)

with open('bread.txt') as f:
        lines = f.read()

        output = gTTS(text = lines, lang = 'es', slow = False)

        output.save('texto.mp3')

os.system('mpg321 texto.mp3 &')