import os
import io
import webcolors
import time
#import picamera
import serial
import json
import detector_colores
from google.cloud import vision
from escribirJson import escJson

#with picamera.PiCamera() as camera:
    #camera.resolution = (1024, 768)
    #camera.start_preview()
    #time.sleep(2) #Tiempo de espera para disparar la foto
    #camera.capture('banana.jpg')

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'Ojo-de-van-gogh-1d875cc39f9a'
client = vision.ImageAnnotatorClient()

file_name = 'banana.jpg'
image_path = f'/home/pi/ojo_de_van_gogh/la_caja_impresionista/banana.jpg'

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

#creo el objeto detectar colores
detector_de_colores = detector_colores.detector_colores()
#Le digo al objeto detectar colores que active su funcion de pasar rgb a hsv
hsv = detector_de_colores.rgb_to_hsv(r,g,b)

#le digo al objeto detectar colores que active su funcion pasar de hsv a nombre de color
nombre_color = detector_de_colores.print_color_name(hsv)

#invoco a la funcion escJson y le paso el nombre del color que va a tener el json
escJson(nombre_color)








""" datos = (wJson (hsv))
data = {}
data['color:'] = (datos)
path = '/home/pi'
file_name = "ej.json" """

""" with open(os.path.join(path, file_name), 'w') as file:
    json.dump(data, file) """


