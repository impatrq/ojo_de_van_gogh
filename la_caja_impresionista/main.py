import os
import io
import webcolors
import time
import picamera
import serial
import json
import RPi.GPIO as GPIO
from detector_colores import detector_colores
from escribirJson import escribir_Json
from google.cloud import vision    

arduino = serial.Serial('/dev/ttyACM0',9600)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT) #creo el pin del led

while True: 
    orden = arduino.read()

    if(orden == b'1'):
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

        Detector_de_colores = detector_colores() # creo el objeto detector de color

        hsv = Detector_de_colores.rgb_to_hsv(r,g,b) # al detector le paso el r,g,b y me devuelve el dato en HSV

        color_nombre = Detector_de_colores.print_color_name(hsv) # al detector le paso el hsv y me devuelve el nombre del color

        escribir_Json(color_nombre) # llamo al metodo escribir_json y le paso el color y me devuelve el json con el color cargado

        Detector_de_colores.print_to_audio(hsv) # llamo al metodo que reproduce audio
    else:
        pass










""" datos = (wJson (hsv))
data = {}
data['color:'] = (datos)
path = '/home/pi'
file_name = "ej.json" """

""" with open(os.path.join(path, file_name), 'w') as file:
    json.dump(data, file) """


