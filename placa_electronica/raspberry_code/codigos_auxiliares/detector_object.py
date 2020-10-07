import os, io, time
from gtts import gTTS
from textblob import TextBlob
import pandas as pd


class detector_object:

    def __init__ (self):
        pass

    def object_recognition(self, localized_object_annotations, df):
        self.localized_object_annotations = localized_object_annotations
        self.df = df
        
        def tr_audio(data):
    
            traduction = TextBlob(data)
            traducido = str(traduction.translate(to = 'es'))

            with open('object.txt', 'w') as f:
                    f.write(traducido + location)

            with open('object.txt') as f:
                    lines = f.read()

                    output = gTTS(text = lines, lang = 'es', slow = False)

                    output.save('object.mp3')

                    os.system('mpg321 object.mp3 &')

        cont = 0
        for obj in localized_object_annotations:
    
            df = df.append(
                dict(
                    name=obj.name,
                    score=obj.score,
                    bounding=obj.bounding_poly
                ),
                ignore_index=True)
            df = df.query('score >= 0.65')

            
    
            if (obj.score >= 0.65):
                promedio_x = (obj.bounding_poly.normalized_vertices[0].x + obj.bounding_poly.normalized_vertices[1].x)/2
                promedio_y = (obj.bounding_poly.normalized_vertices[0].y + obj.bounding_poly.normalized_vertices[2].y)/2

                objeto = (df['name'][cont])
                if promedio_x < 0.33 and promedio_y < 0.33:
                    print(objeto + " está en la parte superior izquierda")
                    location = str(" está en la parte superior izquierda")

                elif promedio_x < 0.66 and promedio_y < 0.33:
                    print(objeto + " está en la parte superior centro")
                    location = str(" está en la parte superior centro")

                elif promedio_x <=1 and promedio_y < 0.33:
                    print(objeto + " está en la parte superior derecha")
                    location = str(" está en la parte superior derecha")

                elif promedio_x < 0.33 and promedio_y < 0.66:
                    print(objeto + " está en la centro izquierda")
                    location = str(" está en la centro izquierda")

                elif promedio_x < 0.66 and promedio_y < 0.66:
                    print(objeto + " está en el centro")
                    location = str(" está en el centro")

                elif promedio_x <= 1 and promedio_y < 0.66:
                    print(objeto + " está en el centro derecha")
                    location = str(" está en el centro derecha")

                elif promedio_x < 0.33 and promedio_y <= 1:
                    print(objeto + " está en la parte inferior izquierda")
                    location = str(" está en la parte inferior izquierda")

                elif promedio_x < 0.66 and promedio_y < 0.66:
                    print(objeto + " está en la parte inferior centro")
                    location = str(" está en la parte inferior centro")

                elif promedio_x <= 1 and promedio_y < 0.66:
                    print(objeto + " está en la parte inferior derecha")
                    location = str(" está en la parte inferior derecha")
                cont = cont + 1
                timing = str(objeto + location)
                print(len(timing))
                tr_audio(objeto)

                if len(timing) >= 50 :
                    time.sleep(4.045)
                
                else :
                    time.sleep(1.5)

                
    
