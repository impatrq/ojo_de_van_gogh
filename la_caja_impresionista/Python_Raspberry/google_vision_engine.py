import os
import io
import pandas as pd
from google.cloud import vision
from gtts import gTTS
from textblob import TextBlob


#########################################
#agregar que si el query no anda use hsv#
#TO DO Agregar audio a reconocer objetos#
#########################################


class GoogleVisionEngine:

    #Se crea el metodo constructor que pide la imagen para trabajar
    #con los metodos
    def __init__(self, image_path):
        self.image_path = image_path #Al objeto se le agrega el valor de path que le mandamos
        

    #Metodo para reconocer un objeto
    def reconocer_objeto(self, ):
        client = vision.ImageAnnotatorClient() #creamos el cliente de google vision

        with open(self.image_path, 'rb') as image:
            content = image.read() # Leemos las cosas de la imagen y lo guardamos en contenido
            # Enviamos la peticion a la API de google con el formato JSON
            # especifico optimizar la velocidad de respuesta
            response = client.annotate_image({'image': {'content': content}, 'features': [
                                             {'type': vision.enums.Feature.Type.OBJECT_LOCALIZATION}], }) 
            localized_object_annotations = response.localized_object_annotations #Guardamos la respuesta de la API

        df_reconocer_objeto = pd.DataFrame(
            columns=['name', 'score', 'bounding']) #Creamos un dataframe con la respuesta de la API

        #Hacemos un for que analiza cada objeto de todos los que habia en la respuesta de la API
        for obj in localized_object_annotations:
            df_reconocer_objeto = df_reconocer_objeto.append(
                dict(
                    name=obj.name, # Nombre del objeto 
                    score=obj.score,# Confiabilidad de que el objeto sea correcto
                    bounding=obj.bounding_poly #Sirve para saber los vertices del objeto y poder ubicarlo
                ),
                ignore_index=True)

            #Descartamos los objetos de poca probabilidad de que sean correctos
            df_reconocer_objeto = df_reconocer_objeto.query('score >= 0.65') 

            #Si el valor es confiable
            if (obj.score >= 0.65):
                
                #Posicion en X
                promedio_x = (
                    obj.bounding_poly.normalized_vertices[0].x + obj.bounding_poly.normalized_vertices[1].x)/2
                #Posicion en Y
                promedio_y = (
                    obj.bounding_poly.normalized_vertices[0].y + obj.bounding_poly.normalized_vertices[2].y)/2

                if promedio_x < 0.33 and promedio_y < 0.33:
                    print("El objeto está en la parte superior izquierda")

                elif promedio_x < 0.66 and promedio_y < 0.33:
                    print("El objeto está en la parte superior centro")

                elif promedio_x <= 1 and promedio_y < 0.33:
                    print("El objeto está en la parte superior derecha")

                elif promedio_x < 0.33 and promedio_y < 0.66:
                    print("El objeto está en la centro izquierda")

                elif promedio_x < 0.66 and promedio_y < 0.66:
                    print("El objeto está en el centro")

                elif promedio_x <= 1 and promedio_y < 0.66:
                    print("El objeto está en el centro derecha")

                elif promedio_x < 0.33 and promedio_y <= 1:
                    print("El objeto está en la parte inferior izquierda")

                elif promedio_x < 0.66 and promedio_y < 0.66:
                    print("El objeto está en la parte inferior centro")

                elif promedio_x <= 1 and promedio_y < 0.66:
                    print("El objeto está en la parte inferior derecha")

    def pedir_color(self, dataframe_colores):

        client = vision.ImageAnnotatorClient() #creamos el cliente de google vision
        dataframe_colores = dataframe_colores #guardamos la tabla de colores patrones para el query

        with open(self.image_path, 'rb') as image:
            content = image.read()# Leemos las cosas de la imagen y lo guardamos en contenido
            # Enviamos la peticion a la API de google con el formato JSON
            # especifico optimizar la velocidad de respuesta
            response = client.annotate_image({'image': {'content': content}, 'features': [
                                             {'type': vision.enums.Feature.Type.IMAGE_PROPERTIES}], }).image_properties_annotation
            dominant_colors = response.dominant_colors.colors# Respuesta de colores


        #Ciclo for para analizar cada color que nos dio la respuesta
        for color in dominant_colors:
            df_pixel_fraction = df_pixel_fraction.append(
                dict(
                    r=int(color.color.red),
                    g=int(color.color.green),
                    b=int(color.color.blue),
                    score=color.score,
                    pixel_fraction=color.pixel_fraction
                ),
                ignore_index=True)

            df_pixel_fraction = df_pixel_fraction.sort_values(
                ['pixel_fraction'], ascending=False).head(2) # Agarramos los dos valores con mas predominancia en la pantalla
            df_pixel_fraction = df_pixel_fraction.sort_values(
                ['score'], ascending=False).head(2) # Agarramos valores de confiabilidad altos
        dif = df_pixel_fraction['score'][0] - df_pixel_fraction['score'][1] # Nos fiajmos si el primer color y el segundo son ambos confiables 

        #Si los dos colores son confaibles usamos los dos
        if (dif < 0.10):
            cont = 0
            for cont in [0, 1]:
                r = (df_pixel_fraction['r'][cont])
                g = (df_pixel_fraction['g'][cont])
                b = (df_pixel_fraction['b'][cont])

                self.rgb_to_name_query(dataframe_colores, r, g, b)# Llamamos a la funcion que hace el query para el nombre de color
        #Si solo hay uno confiable usamos ese y ya esta
        else:
            r = (df_pixel_fraction['r'][0])
            g = (df_pixel_fraction['g'][0])
            b = (df_pixel_fraction['b'][0])

            self.rgb_to_name_query(dataframe_colores, r, g, b)# Llamamos a la funcion que hace el query para el nombre de color

    def rgb_to_name_query(self, dataframe_colores, R, G, B):

        dataframe_colores = dataframe_colores #Guardamos la tabla de colores con nombres

        #Guardamos los valores de R,G,B
        R = R 
        G = G
        B = B

        #Como no se puede dividir por 0 le agregamos 0.1 si es 
        #0 el valor que entra

        if R == 0:
            R += 0.1
        if G == 0:
            G += 0.1
        if B == 0:
            B += 0.1

        #Nos fijamos los valores que entran su minimo y maximo
        mx = max(R, G, B)
        mn = min(R, G, B)

        diferencia_min_max = mx - mn
        # Si los tres valores son muy parecidos y son menores a 50
        # Siempre da negro la combinacion
        if mx <= 50 and diferencia_min_max <= 5:
            print("color: black")
        
        # Si los tres valores son muy parecidos y son mayores a 230
        # Siempre da blanco la combinacion
        elif mn >= 230:
            print("color: blanco")

        #Si no procedemos a el query
        else:
            dataframe_colores = dataframe_colores[[
                'Principal_color', 'CSS_name', 'R', 'G', 'B']] #Sacamos el valor de Hexagesimal 

            #Llamamos al metodo de busqueda binaria para buscar si un color en 
            #la tabla de R asi pedir ese valor
            Resultado_busqueda_binaria = self.busqueda_binaria(
                dataframe_colores, 0, len(dataframe_colores[['R']]), R)
            

            dataframe_colores.query(
                'R == @Resultado_busqueda_binaria', inplace=True) # Query para ver Los colores con R parecido
            dataframe_colores.query(
                'G/@G <=1.5 and G/@G >=0.65 ', inplace=True)# Query para ver Los colores con G parecido
            dataframe_colores.query(
                'B/@B <=1.5 and B/@B >=0.65 ', inplace=True)# Query para ver Los colores con B parecido

            #Si los query dan vacio porque no se encontro el color
            if(dataframe_colores.empty == True):
                print("no se encontro una opcion en la base de datos")

                #Creamos una fila para el nuevo color que no sabemos el nombre
                df_new_color = pd.DataFrame(
                    columns=['Principal_color', 'CSS_name', 'R', 'G', 'B'])
                
                #A la nueva fila le guardamos los valores del color nuevo
                # Dejamos un mensaje que hay que clasificar el nombre
                df_new_color = df_new_color.append(
                    dict(
                        Principal_color="Clasificar",
                        CSS_name="Clasificar",
                        R=int(R),
                        G=int(G),
                        B=int(B),
                    ), ignore_index=True
                )

                #Al nuevo dataframe le agregamos el nuevo color
                dataframe_actualizado = dataframe_actualizado.append(
                    df_new_color, ignore_index=True)
                #Ordenamos el nuevo color segun su valor en R porque 
                #lo requiere la busqeuda binaria
                dataframe_actualizado = dataframe_actualizado.sort_values(
                    ['R'], ascending=True)
                #Exportamos la nueva tabla para qe reeemplace la vieja
                dataframe_actualizado.to_csv('Tabla_colores.csv', index=False)

    def leer_texto(self,):
        client = vision.ImageAnnotatorClient()
        with open(self.image_path, 'rb') as image:
            content = image.read()
            # construct an image instance
            # annotate Image Response
            response = client.annotate_image({'image': {'content': content}, 'features': [
                                             {'type': vision.enums.Feature.Type.TEXT_DETECTION}], })
            # returns TextAnnotation
            texts = response.text_annotations

        df_leer_texto = pd.DataFrame(columns=['locale', 'description'])

        for text in texts:
            df_leer_texto = df_leer_texto.append(
                dict(
                    locale=text.locale,
                    description=text.description
                ),
                ignore_index=True
            )

        texto = (df_leer_texto['description'][0])
        traduction = TextBlob(texto)
        idioma = str(traduction.detect_language())
        if idioma != 'es':
            traducido = str(traduction.translate(to='es'))

        with open('bread.txt', 'w') as f:
            f.write(traducido)

        with open('bread.txt') as f:
            lines = f.read()

            output = gTTS(text=lines, lang='es', slow=False)

            output.save('texto.mp3')

        os.system('mpg321 texto.mp3 &')

    def rgb_to_name_hsv(self, R, G, B):
        pass

    def busqueda_binaria(self, dataframe, comienzo, final, objetivo):

        if comienzo > final:
            return False
        medio = (comienzo + final) // 2

        if dataframe['R'][medio] <= objetivo * 1.5 and dataframe['R'][medio] >= objetivo * 0.65:
            print("objetivo")
            return objetivo

        elif dataframe['R'][medio] < objetivo:
            return self.busqueda_binaria(dataframe, medio + 1, final, objetivo)
        else:
            return self.busqueda_binaria(dataframe, comienzo, medio - 1, objetivo)
