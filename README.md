

# Ojo de van gogh

Este proyecto esta hecho con el fin de crear un **sistema de ayuda a la gente con discapacidad visual** para, a través de inteligencia artificial, **reconocer objectos que no pueden ver**. 

Se compone de un sistema electrónico que va colocado en el antebrazo y lleva una camera que se coloca en la mano. Cuando el ciego, por ejemplo, parpadea dos veces el sensor cerebral entiende su intencionalidad de querer sacar una foto y se lo comunica a la raspberry, esta actua sacando una foto y la procesa con **google vision API** para luego dar una respuesta del texto que se lee en la foto, el objeto que aparece o los colores predominantes

## Requisitos

Para ejecutar este proyecto se debe contar con estos requisitos:

- Hardware: elementos electronicos fisicos para crear el sistema.
  - Mindwave
  - Arduino Nano
  - Raspberry Pi Zero
  - Pi camera
  - Cargador portatil pequeño (ver PCB)
  - Dos buzzers
- Software: lenguajes requeridos para poder llevar a cabo esta idea
  - Python 3.7
  - Arduino IDE

## Instalación

#### Raspberry:

Para ejecutar la instalación debemos pararnos en la carpeta raiz del proyecto y ejecutar

```shell
pip install -r requirements.txt
```

Luego de ejecutar esto contamos con las dependencias para que la raspberry trabaje de manera correcta. 

#### Arduino:

Para ejecutar la instalacion procedemos a conectar el arduino a nuestro computador y seleccionamos el puerto correspondiente y enviamos el archivo "mindwave.ino" que se encuentra en la siguiente ruta *ojo_de_van_gogh\placa_electronica\arduino_code*

## Autores de este repositorio 

- **CARRO, Nahuel Agustín** - *PCB, Arduino y Raspberry* - [NahuelCarro](https://github.com/NahuelCarro)
- **PIERRI, Matias Gabriel** - *PCB, Arduino, Raspberry y Case3D* - [matias1379](https://github.com/matias1379)
- **VILARDO, Theo** - *Raspberry* - [TheoVilardo](https://github.com/theovilardo)
- **FONTE, Gonzalo Juan** - *Case3D* - [gonzafonte](https://github.com/gonzafonte)

## Colaboradores

- **MEDINA, Sergio** - *Supervisor desarrollo proyecto* - [sergiomedinaio](https://github.com/sergiomedinaio)

