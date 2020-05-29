import os
import io
import webcolors
import time
import picamera
import serial
import json
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


def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    s = (df/mx)*100
    v = mx*100
    hue = 0
    
    if ((mx == r) and (s >= 50) and (v >= 30) and (v <= 60)): #es el valor de marron
      return 370
      
    if ((v > 25) and (v <= 60) and (s <= 10)):  #es el valor de gris
      return 380
      
    if (mx==mn) and (v>15) and (v<60):
      return 380
      
    if ((mx >= (226/255)) and (mn >= (226/255))): #es el valor de blanco
      return 390
    
    if mx <= (25/255):  #es el valor de negro (NO DEBE SER TAN NEGRO!)
      return 400
  
    elif mx == r:
        hue = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        hue = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        hue = (60 * ((r-g)/df) + 240) % 360

    return hue

name = rgb_to_hsv(r, g, b)

hsv = str(0)

def escJson (hsv):
  datos = {
    'color' : f'{hsv}'
  }

  json_str = json.dumps(datos)

  print(json_str)
    

def print_color_name (name):
  if name < 15:
    escJson("rojo")
    
  elif name < 45:
    escJson("naranja")
    
  elif name < 90:
    escJson("amarillo")
    
  elif name < 150:
    escJson("verde")
    
  elif name < 210:
    escJson("cyan")
    
  elif name < 270:
    escJson("azul")
    
  elif name < 300:
    escJson("violeta")
    
  elif name < 345:
    escJson("rosa")
    
  elif name < 360:
    escJson("rojo")
    
  elif name == 370:
    escJson("marron")
    
  elif name == 380:
    escJson("gris")
    
  elif name < 390:
    escJson("blanco")

  else:
    escJson("negro")
    
def print_color_to_aud (name):
  if name < 15:
    os.system('mpg321 rojo.mp3 &')
    
  elif name < 45:
    os.system('mpg321 naranja.mp3 &')
    
  elif name < 90:
    os.system('mpg321 amarillo.mp3 &')
    
  elif name < 150:
    os.system('mpg321 verde.mp3 &')
    
  elif name < 210:
    os.system('mpg321 cyan.mp3 &')
    
  elif name < 270:
    os.system('mpg321 azul.mp3 &')
    
  elif name < 300:
    os.system('mpg321 violeta.mp3 &')
    
  elif name < 345:
    os.system('mpg321 rosa.mp3 &')
    
  elif name < 360:
    os.system('mpg321 rojo.mp3 &')
    
  elif name == 370:
    os.system('mpg321 marron.mp3 &')
    
  elif name == 380:
    os.system('mpg321 gris.mp3 &')
    
  elif name < 390:
    os.system('mpg321 blanco.mp3 &')

  else:
    os.system('mpg321 negro.mp3 &')

        
color = str(rgb_to_hsv(r, g, b))

print("hue:", color)

color2 = str(print_color_name (name))

print(color2)

color3 = str(print_color_to_aud (name))

print("-R:" , r, "-G:", g, "-B:", b)

hsv = str(0)

def wJson (hsv):
  data = {
    'color' : f'{hsv}'
  }

datos = (wJson (hsv))
data = {}
data['color:'] = (datos)
path = '/home/pi'
file_name = "ej.json"

with open(os.path.join(path, file_name), 'w') as file:
    json.dump(data, file)

#escJson("a")
