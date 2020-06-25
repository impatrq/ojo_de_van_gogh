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
        
    else:
        print("esperando la orden")
        pass








""" datos = (wJson (hsv))
data = {}
data['color:'] = (datos)
path = '/home/pi'
file_name = "ej.json" """

""" with open(os.path.join(path, file_name), 'w') as file:
    json.dump(data, file) """


