from texto_to_audio import texto_to_audio

dato = texto_to_audio()

text = "Con gTTS, te explicaremos como convertir texto a voz desde la ventana de símbolo de sistema utilizando la API de Google Translate. Con este programa de línea de comandos, podrás tomar textos cortos o largos, para guardarlo en un archivo de audio en formato MP3. Pero lo más importante de la plataforma es la posibilidad de personalizar la conversión o determinar reglas para el idioma."
dato.audio(text)

# Es el mismo texto pero en ingles y lo tradujo re bien
ingles = "With gTTS, we will explain how to convert text to speech from the command prompt window using the Google Translate API. With this command line program, you can take short or long texts, to save it in an audio file in MP3 format. But the most important thing about the platform is the possibility of customizing the conversion or determining rules for the language."
dato.audio(ingles)
