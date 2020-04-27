import os
import io
import webcolors
import time
#import picamera
import serial
import json
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
  import json
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

        
color = str(rgb_to_hsv(r, g, b))

print("hue:", color)

color2 = str(print_color_name (name))

print(color2)

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

escJson("a")
