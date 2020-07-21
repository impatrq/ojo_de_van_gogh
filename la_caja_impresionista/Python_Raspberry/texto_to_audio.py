import os
import io
from gtts import gTTS

# Se crea el metodo y se declara la variable


class texto_to_audio:
    texto = str

    def __init__(self):
        pass

    # Se crea la funcion que pasa de texto a audio
    def audio(self, texto):
        self.texto = texto

        # Se crea un archivo txt que tiene la variable texto
        with open('texto_a_traducir.txt', 'w') as f:
            f.write(self.texto)

        # Se lee el archivo creado
        with open('texto_a_traducir.txt') as f:
            lines = f.read()

            # se convierte ese archivo a audio
            output = gTTS(text=lines, lang='es', slow=False)

            # Se guarda el audio como mp3
            output.save('texto.mp3')

        # Se reproduce el audio
        os.system('texto.mp3 &')
