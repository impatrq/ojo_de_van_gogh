import os
import io
import webcolors
import time
#import picamera
import serial
import json
import detector_colores
from google.cloud import vision

#with picamera.PiCamera() as camera:
    #camera.resolution = (1024, 768)
    #camera.start_preview()
    #time.sleep(2) #Tiempo de espera para disparar la foto
    #camera.capture('banana.jpg')

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'OjoDeVangogh-04b247a7603b.json'
client = vision.ImageAnnotatorClient()

file_name = 'banana.jpg'
image_path = f'/home/pi/banana.jpg'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)
response = client.image_properties(image=image).image_properties_annotation
dominant_colors = response.dominant_colors

for color in dominant_colors.colors:

    print('')

r = int(color.color.red)
g = int(color.color.green)
b = int(color.color.blue)

detector_de_colores = detector_colores.detector_colores(r,g,b)

detector_de_colores.rgb_to_hsv()

name = rgb_to_hsv(r, g, b)

hsv = str(0)


        
color = str(rgb_to_hsv(r, g, b))

print("hue:", color)

color2 = str(print_color_name (name))

print(color2)

print("-R:" , r, "-G:", g, "-B:", b)

hsv = str(0)



datos = (wJson (hsv))
data = {}
data['color:'] = (datos)
path = '/home/pi'
file_name = "ej.json"

with open(os.path.join(path, file_name), 'w') as file:
    json.dump(data, file)


