import RPi.GPIO as GPIO
import time


class morse_colores:
    pin_buzzer = int
    frecuencia = int

    # Se crea el metodo que pide el pin en el que saldra la vibracion
    def __init__(self, pin_buzzer):
        # se agrega el valor de pin
        self.pin_buzzer = pin_buzzer
        pass

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
