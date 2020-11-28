# Python core
import time
import serial
import pandas as pd
import os

# Raspberry
import picamera
import RPi.GPIO as GPIO

# Google Vision
from google.cloud import vision

# Clases
from clases.text_manager import TextManager
from clases.morse_colores import MorseColores
from clases.texto_to_audio import TextoToAudio
from clases.colors_manager import ColorsManager
from clases.object_manager import ObjectManager
from clases.opciones_usuario import OpcionesUsuario

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'./OjoDeVangogh-04b247a7603b.json'
CLIENT = vision.ImageAnnotatorClient()

FILE_NAME = 'photo.jpg'
IMAGE_PATH = f'./{FILE_NAME}'

DATAFRAME_COLOR = pd.read_csv('./colores.csv', encoding='utf-8')
IDIOMA = 'es'

reproductor_audio = TextoToAudio()
morse_colores = MorseColores(22)  # Se indica el pin de los vibradores

arduino = serial.Serial('/dev/ttyACM0', 9600)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)  # creo el pin del led

while True:
    orden = arduino.read()
    if orden == b'sacar foto':
        with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        time.sleep(2)  # Tiempo de espera para disparar la foto
        camera.capture('photo.jpg')

        if(orden == b'OpcionesUsuario.detectar_color.value'):

            colors_manager = ColorsManager(IMAGE_PATH, CLIENT, DATAFRAME_COLOR)
            datos_rgb_api = colors_manager.get_response_api()
            print(datos_rgb_api)

            for value_color in colors_manager.get_color(datos_rgb_api):

                morse_colores.color_to_vibrate(value_color)
                traducido = reproductor_audio.translate(value_color, IDIOMA)
                reproductor_audio.speak_audio(str(traducido))
                time.sleep(2)

        elif(orden == b'OpcionesUsuario.leer_texto.value'):

            text_manager = TextManager(IMAGE_PATH, CLIENT)

            respuesta_texto_api = text_manager.get_response_api()

            texto = text_manager.get_text(respuesta_texto_api)

            traducido = reproductor_audio.translate(texto, IDIOMA)
            reproductor_audio.speak_audio(str(traducido))
            time.sleep(1)

        elif(orden == b'OpcionesUsuario.detectar_objetos.value'):

            object_manager = ObjectManager(IMAGE_PATH, CLIENT)

            respuestas_objetos = object_manager.get_response_api()

            for objetos in object_manager.get_object(respuestas_objetos):

                traducido = reproductor_audio.translate(objetos, IDIOMA)
                reproductor_audio.speak_audio(str(traducido))
                time.sleep(3)

        else:
            print("No llego ninguna orden")
