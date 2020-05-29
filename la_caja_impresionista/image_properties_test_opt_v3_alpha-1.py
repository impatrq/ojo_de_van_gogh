import os
import io
import webcolors
import time
import picamera
import serial
import json
from detector_colores import detector_colores
from escribirJson import escribir_Json
from google.cloud import vision                                                                                                                          

start = time.time()                                                             
with picamera.PiCamera(resolution=(640, 480), framerate=100) as camera:                                
    camera.shutter_speed = 18000                                                                                  
    camera.start_preview()                                                                                          
    time.sleep(0)                                                               
    start = time.time()                                                    
    camera.capture('banana2.jpg', 'jpeg', use_video_port=True)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'OjoDeVangogh-04b247a7603b.json'
client = vision.ImageAnnotatorClient()

#file_name = 'banana2.jpg'
#image_path = f'/home/pi/color_audio/banana2.jpg'

#with io.open(image_path, 'rb') as image_file:
    #content = image_file.read()

from base64 import b64encode
from json import dumps

ENCODING = 'utf-8'
IMAGE_NAME = 'banana2.jpg'
JSON_NAME = 'output.json'

# first: reading the binary stuff
# note the 'rb' flag
# result: bytes
with open(IMAGE_NAME, 'rb') as open_file:
    byte_content = open_file.read()

# second: base64 encode read data
# result: bytes (again)
base64_bytes = b64encode(byte_content)

# third: decode these bytes to text
# result: string (in utf-8)
base64_string = base64_bytes.decode(ENCODING)

# optional: doing stuff with the data
# result here: some dict
raw_data = {IMAGE_NAME: base64_string}

# now: encoding the data to json
# result: string
json_data = dumps(raw_data, indent=2)

# finally: writing the json string to disk
# note the 'w' flag, no 'b' needed as we deal with text here
with open(JSON_NAME, 'w') as another_open_file:
    another_open_file.write(json_data)

with open("output.json", "r") as f:
    content = json.loads(f)

image = vision.types.Image(content=content)
response = client.image_properties(image=image).image_properties_annotation
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









with open(os.path.join(path, file_name), 'w') as file:
    json.dump(data, file)

#escJson("a")
