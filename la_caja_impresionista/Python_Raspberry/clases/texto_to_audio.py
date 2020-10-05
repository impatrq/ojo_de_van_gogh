import os
from gtts import gTTS
from textblob import TextBlob


class TextoToAudio:

    def __init__(self,):
        self.content = ""

    def translate(self, content, requested_language):

        # Se guarda el idioma pedido como global
        self.requested_language = requested_language

        self.content = TextBlob(content)

        # Se guarda el idioma del contenido
        content_language = str(self.content.detect_language())

        # Si son diferentes idiomas se traduce
        if content_language != self.requested_language:
            translated_content = str(self.content.translate(
                to=self.requested_language))

            # Se devuelve el contenido traducido
            return (translated_content)

        # Si no, se devuelve el contenido como se paso
        else:
            return (self.content)

    # Se crea la funcion que pasa de texto a audio
    def speak_audio(self, contenido_traducido):

        # Se guarda el contenido traducido
        contenido_traducido = contenido_traducido

        # Se crea un archivo txt que tiene la variable texto
        with open('contenido_a_reproducir.txt', 'w') as f:
            f.write(contenido_traducido)

        # Se lee el archivo creado
        with open('contenido_a_reproducir.txt') as f:
            lines = f.read()

            # se convierte ese archivo a audio
            output = gTTS(text=lines, lang=self.requested_language, slow=False)

            # Se guarda el audio como mp3
            output.save('texto.mp3')

        # Se reproduce el audio
        os.system('texto.mp3 &')
