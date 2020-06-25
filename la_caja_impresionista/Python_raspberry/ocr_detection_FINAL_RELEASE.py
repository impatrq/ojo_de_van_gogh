import os, io, picamera
from google.cloud import vision
import pandas as pd
from gtts import gTTS
from textblob import TextBlob

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"OjoDeVangogh-04b247a7603b.json"
client = vision.ImageAnnotatorClient()

def takephoto():
    camera = picamera.PiCamera()
    camera.capture('read.jpg')
takephoto()

file_name = 'read2.jpg'
image_path = f'/home/pi/txtdetect/{file_name}'

