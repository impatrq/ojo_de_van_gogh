from texto_to_audio import texto_to_audio
from gtts import gTTS

dato = texto_to_audio()

text = "Con gTTS, te explicaremos como convertir texto a voz desde la ventana de símbolo de sistema utilizando la API de Google Translate. Con este programa de línea de comandos, podrás tomar textos cortos o largos, para guardarlo en un archivo de audio en formato MP3. Pero lo más importante de la plataforma es la posibilidad de personalizar la conversión o determinar reglas para el idioma."

dato.audio(text)
