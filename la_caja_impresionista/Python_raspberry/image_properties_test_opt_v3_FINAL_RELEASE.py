import os
import io
import webcolors
import time
import picamera
import serial
import json
import base64
from detector_colores import detector_colores
from escribirJson import escribir_Json
from google.cloud import vision                                                                                                                          

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

#start = time.time()                                                             
#with picamera.PiCamera(resolution=(640, 480), framerate=100) as camera:                                
    #camera.shutter_speed = 18000                                                                                  
    #camera.start_preview()                                                                                          
    #time.sleep(0)                                                               
    #start = time.time()                                                    
    #camera.capture('banana2.jpg', 'jpeg', use_video_port=True)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'OjoDeVangogh-04b247a7603b.json'
client = vision.ImageAnnotatorClient()


IMAGE_NAME = '/home/pi/color_audio/banana2.jpg'

base64_string3 = get_base64_encoded_image(IMAGE_NAME)

raw_data = {
  "requests":[
    {
      "image":{
        "content": base64_string3
      },
      "features": [
        {
          "type":"IMAGE_PROPERTIES",
          "maxResults":1
        }
      ]
    }
  ]
}


json_data = json.dumps(raw_data, indent=2)

content = json.loads(json_data)

client = vision.ImageAnnotatorClient()
image_path ='/home/pi/color_audio/banana2.jpg'

with open(image_path, 'rb') as image:
    content = image.read()
    response = client.annotate_image({'image': {'content': content}, 'features': [{'type': vision.enums.Feature.Type.IMAGE_PROPERTIES}],}).image_properties_annotation
    dominant_colors = response.dominant_colors


for color in dominant_colors.colors:
  print('')

r = int(color.color.red)
g = int(color.color.green)
b = int(color.color.blue)


Detector_de_colores = detector_colores() # creo el objeto detector de color

hsv = Detector_de_colores.rgb_to_hsv(r,g,b) # al detector le paso el r,g,b y me devuelve el dato en HSV

color_nombre = Detector_de_colores.print_color_name(hsv) # al detector le paso el hsv y me devuelve el nombre del color

escribir_Json(color_nombre) # llamo al metodo escribir_json y le paso el color y me devuelve el json con el color cargado

Detector_de_colores.print_to_audio(hsv) # llamo al metodo que reproduce audio
