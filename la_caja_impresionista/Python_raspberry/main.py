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
from enum import Enum


class Opciones_usuario(Enum):
    detectar_color = 1
    detectar_color_y_matices = 2
    leer_texto = 3
    detectar_objetos = 4


arduino = serial.Serial('/dev/ttyACM0', 9600)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)  # creo el pin del led

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    time.sleep(2)  # Tiempo de espera para disparar la foto
    camera.capture('photo.jpg')


while True:
    orden = arduino.read()

    if(orden == b'@Opciones_usuario.detectar_color'):

        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'OjoDeVangogh-04b247a7603b.json'
        client = vision.ImageAnnotatorClient()

        file_name = 'photo.jpg'
        image_path = f'/home/pi/banana.jpg'

        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)
        response = client.image_properties(
            image=image).image_properties_annotation
        dominant_colors = response.dominant_colors.colors
        df = pd.DataFrame(columns=['r', 'g', 'b', 'pixel_fraction', 'score'])

        for color in dominant_colors:
            df = df.append(
                dict(
                    r=int(color.color.red),
                    g=int(color.color.green),
                    b=int(color.color.blue),
                    score=color.score,
                    pixel_fraction=color.pixel_fraction
                ),
                ignore_index=True)  # se crea un diccionario con los valores de los colores
            # se toma los dos valores que ocupen mas espacio en la pantalla
            df = df.sort_values(['pixel_fraction'], ascending=False).head(2)
            # se toma los dos valores que hay confianza que la IA detecto el color
            df = df.sort_values(['score'], ascending=False).head(2)

        # Se calcula si la confianza entre el primero y el segundo son parecidas
        dif = df['score'][0] - df['score'][1]

        # Si los niveles de confianza son proximos se dice los dos colores
        if (dif < 0.10):
            cont = 0
            for cont in [0, 1]:
                r = (df['r'][cont])
                g = (df['g'][cont])
                b = (df['b'][cont])
                print(r, g, b)
        # Si los niveles de confianza son distantes se dice solo el mas confianble
        else:
            print(df['r'][0])
            print(df['g'][0])
            print(df['b'][0])

    elif(orden == b'@Opciones_usuario.detectar_color_y_matices'):

        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'OjoDeVangogh-04b247a7603b.json'
        client = vision.ImageAnnotatorClient()

        file_name = 'photo.jpg'
        image_path = f'/home/pi/banana.jpg'

        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)
        response = client.image_properties(
            image=image).image_properties_annotation
        dominant_colors = response.dominant_colors.colors
        df = pd.DataFrame(columns=['r', 'g', 'b', 'pixel_fraction', 'score'])

        for color in dominant_colors:
            df = df.append(
                dict(
                    r=int(color.color.red),
                    g=int(color.color.green),
                    b=int(color.color.blue),
                    score=color.score,
                    pixel_fraction=color.pixel_fraction
                ),
                ignore_index=True)  # se crea un diccionario con los valores de los colores

            # se toma los dos valores que ocupen mas espacio en la pantalla
            df = df.sort_values(['pixel_fraction'], ascending=False).head(2)

            # se toma los dos valores que hay confianza que la IA detecto el color
            df = df.sort_values(['score'], ascending=False).head(2)

        # Se calcula si la confianza entre el primero y el segundo son parecidas
        dif = df['score'][0] - df['score'][1]

        # Si los niveles de confianza son proximos se dice los dos colores
        if (dif < 0.10):
            cont = 0
            for cont in [0, 1]:
                r = (df['r'][cont])
                g = (df['g'][cont])
                b = (df['b'][cont])
                print(r, g, b)

        # Si los niveles de confianza son distantes se dice solo el mas confianble
        else:
            print(df['r'][0])
            print(df['g'][0])
            print(df['b'][0])

    elif(orden == b'@Opciones_usuario.leer_texto'):

    elif(orden == b'@Opciones_usuario.detectar_objetos'):
        pass
