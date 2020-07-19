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
        punto()
        punto()
        punto()
        punto()

    def rojo(self):
        punto()
        punto()
        punto()
        linea()

    def marron(self):
        punto()
        punto()
        linea()
        punto()

    def naranja(self):
        punto()
        punto()
        linea()
        linea()

    def amarillo(self):
        punto()
        linea()
        punto()
        punto()

    def verde(self):
        punto()
        linea()
        punto()
        linea()

    def cyan(self):
        punto()
        linea()
        linea()
        punto()

    def azul(self):
        punto()
        linea()
        linea()
        linea()

    def violeta(self):
        linea()
        punto()
        punto()
        punto()

    def rosa(self):
        linea()
        punto()
        punto()
        linea()

    def gris(self):
        linea()
        punto()
        linea()
        punto()

    def negro(self):
        linea()
        linea()
        linea()
        linea()
