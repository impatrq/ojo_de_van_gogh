import os
import io
from google.cloud import vision
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:/Users/pc1/Documents/Python/OjoDeVangogh-04b247a7603b.json'
client = vision.ImageAnnotatorClient()

file_name = 'control_remoto.png'
image_path = f'C:/Users/pc1/Documents/Python/{file_name}'

