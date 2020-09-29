import RPi.GPIO as GPIO
import time


class morse_colores:

    # Se crea el metodo que pide el pin en el que saldra la vibracion
    def __init__(self, pin_buzzer):
        # se agrega el valor de pin
        self.pin_buzzer = pin_buzzer
        self.INTERVALO = 0.25
        self.PUNTO = 0.25
        self.LINEA = 1
        # desactivamos mensajes de error
        GPIO.setwarnings(False)

        # indicamos el uso de  la identificacion BCM para los GPIO
        GPIO.setmode(GPIO.BCM)

        # indicamos que el GPIO18 es de salida
        GPIO.setup(self.pin_buzzer, GPIO.OUT)

    # Se crea la funcion para hacer un punto

    def vibrate_morse(self, duracion_vibracion):
        """
        this function recive an array of time 
        and make vibrations
        """
        INTERVALO = self.INTERVALO
        for i in duracion_vibracion:
            # Se activa la salida por 250mS
            GPIO.output(self.pin_buzzer, True)
            time.sleep(duracion_vibracion[i])
            if duracion_vibracion[i] == 1:
                print("----------------------------")
            else:
                print(".....")
            # Se apaga la salida por 250mS
            GPIO.output(self.pin_buzzer, False)
            time.sleep(INTERVALO)

    def color_to_vibrate(self, color):
        PUNTO = self.PUNTO
        LINEA = self.LINEA
        vibrate_morse = self.vibrate_morse

        if (color == "blanco"):
            vibrate_morse([PUNTO, PUNTO, PUNTO, PUNTO])
            print("Color blanco")

        elif (color == "rojo"):
            vibrate_morse([PUNTO, PUNTO, PUNTO, LINEA])
            print("Color rojo")

        elif (color == "marron"):
            vibrate_morse([PUNTO, PUNTO, LINEA, PUNTO])
            print("Color marron")

        elif (color == "naranja"):
            vibrate_morse([PUNTO, PUNTO, LINEA, LINEA])
            print("Color naranja")

        elif (color == "amarillo"):
            vibrate_morse([PUNTO, LINEA, PUNTO, PUNTO])
            print("Color amarillo")

        elif (color == "verde"):
            vibrate_morse([PUNTO, LINEA, PUNTO, LINEA])
            print("Color verde")

        elif (color == "cyan"):
            vibrate_morse([PUNTO, LINEA, LINEA, PUNTO])
            print("Color cyan")

        elif (color == "azul"):
            vibrate_morse([PUNTO, LINEA, LINEA, LINEA])
            print("Color azul")

        elif (color == "violeta"):
            vibrate_morse([LINEA, PUNTO, PUNTO, PUNTO])
            print("Color violeta")

        elif (color == "rosa"):
            vibrate_morse([LINEA, PUNTO, PUNTO, LINEA])
            print("Color rosa")

        elif (color == "gris"):
            vibrate_morse([LINEA, PUNTO, LINEA, PUNTO])
            print("Color gris")

        elif (color == "negro"):
            vibrate_morse([LINEA, LINEA, LINEA, LINEA])
            print("Color negro")
