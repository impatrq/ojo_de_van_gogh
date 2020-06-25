import os, io
import pandas as pd
from gtts import gTTS
from textblob import TextBlob

class detector_ocr:

    def __init__ (self):
        pass

    def text_recognition(self, texts, df):
        self.texts = texts
        self.df = df
        for text in texts:
            df = df.append(
                dict(
                    locale=text.locale,
                    description=text.description
                ),
                ignore_index=True
            )
        print(df['description'][0])
        texto = (df['description'][0])

        traduction = TextBlob(texto)
        idioma = str(traduction.detect_language())
        if idioma != 'es':
            traducido = str(traduction.translate(to = 'es'))
            
        with open('bread.txt', 'w') as f:
            f.write(traducido)

        with open('bread.txt') as f:
            lines = f.read()

            output = gTTS(text = lines, lang = 'es', slow = False)

            output.save('texto.mp3')

        os.system('mpg321 texto.mp3 &')
