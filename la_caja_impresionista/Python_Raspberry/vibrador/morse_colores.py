import RPi.GPIO as GPIO
import time


class morse_colores:
    pin_buzzer = int

    # Se crea el metodo que pide el pin en el que saldra la vibracion
    def __init__(self, pin_buzzer):
        # se agrega el valor de pin
        self.pin_buzzer = pin_buzzer

        # desactivamos mensajes de error
        GPIO.setwarnings(False)

        # indicamos el uso de  la identificacion BCM para los GPIO
        GPIO.setmode(GPIO.BCM)

        # indicamos que el GPIO18 es de salida
        GPIO.setup(self.pin_buzzer, GPIO.OUT)

    # Se crea la funcion para hacer un punto

    def punto(self):
        # Se activa la salida por 250mS
        GPIO.output(self.pin_buzzer, True)
        time.sleep(0.25)
        # Se apaga la salida por 250mS
        GPIO.output(self.pin_buzzer, True)
        time.sleep(0.25)

    def linea(self):
        # Se activa la salida por 1seg
        GPIO.output(self.pin_buzzer, True)
        time.sleep(1)
        # Se apaga la salida por 250mS
        GPIO.output(self.pin_buzzer, True)
        time.sleep(0.25)

    # Se definen las vibraciones de los distintos colores,
    # segun tabla de referencia
    def blanco(self):
        self.punto()
        self.punto()
        self.punto()
        self.punto()

    def rojo(self):
        self.punto()
        self.punto()
        self.punto()
        self.linea()

    def marron(self):
        self.punto()
        self.punto()
        self.linea()
        self.punto()

    def naranja(self):
        self.punto()
        self.punto()
        self.linea()
        self.linea()

    def amarillo(self):
        self.punto()
        self.linea()
        self.punto()
        self.punto()

    def verde(self):
        self.punto()
        self.linea()
        self.punto()
        self.linea()

    def cyan(self):
        self.punto()
        self.linea()
        self.linea()
        self.punto()

    def azul(self):
        self.punto()
        self.linea()
        self.linea()
        self.linea()

    def violeta(self):
        self.linea()
        self.punto()
        self.punto()
        self.punto()

    def rosa(self):
        self.linea()
        self.punto()
        self.punto()
        self.linea()

    def gris(self):
        self.linea()
        self.punto()
        self.linea()
        self.punto()

    def negro(self):
        self.linea()
        self.linea()
        self.linea()
        self.linea()

    def color_to_sonido(self, color):
        if (color == "blanco"):
            self.blanco()
            print("Color blanco")

        elif (color == "rojo"):
            self.rojo()
            print("Color rojo")

        elif (color == "marron"):
            self.marron()
            print("Color marron")

        elif (color == "naranja"):
            self.naranja()
            print("Color naranja")

        elif (color == "amarillo"):
            self.amarillo()
            print("Color amarillo")

        elif (color == "verde"):
            self.verde()
            print("Color verde")

        elif (color == "cyan"):
            self.cyan()
            print("Color cyan")

        elif (color == "azul"):
            self.azul()
            print("Color azul")

        elif (color == "violeta"):
            self.violeta()
            print("Color violeta")

        elif (color == "rosa"):
            self.rosa()
            print("Color rosa")

        elif (color == "gris"):
            self.gris()
            print("Color gris")

        elif (color == "negro"):
            self.negro()
            print("Color negro")
