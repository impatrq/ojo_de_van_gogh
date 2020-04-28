# Entorno de trabajo de Arduino con Bluetooth

Los dispositivos Bluetooth(BT) pueden ser configurados para que trabajen como Esclavo (slave) o maestro (master). 

## Modulo BT HC-05 como esclavo :
En este modo el dispositivo espera que un BT master se conecte a el.
## Modulo BT HC-05 como maestro:
En este modo, el HC-05 es el que inicia la conexión. Se utiliza este modo para comunicarse entre módulos BT.

## <u>Modos de trabajo:</u>
Tiene 4 estados :

1. Estado desconectado:
   - Entra en este estado cuando se alimenta al modulo y no ha realizado una conexión Bt. 
   - El Led del BT parpadea rápidamente.
   - El HC-05 no pude interpretar comandos AT

2. Estado conectado o de comunicación:
	- Entra cuando hay una comunicación con otro dispositivo BT.
	- El Led hace doble parpadeo
	- Los datos ingresados por el pin Rx se transmiten por BT al dispositivo conectado y los datos recibidos se devuelven por el pin Tx 

3. Modo AT 1
	- Para entrar a este estado después de conectar y  alimentar el modulo es necesario apretar el botón del modulo.
	- Se  pueden enviar comandos AT, pero a la misma velocidad que esta configurado
	- Parpadea rápido igual que en el estado desconectado.

4. Modo AT 2
	- E modulo debe encender con el botón presionado, después de haber encendido se puede soltar y permanecerá en este estado.

- En este estado, para enviar comandos AT es necesario hacerlo a la velocidad de 38400 baudios.

- EL LED del módulo en este estado parpadea lento.
## <u>Conexión para configuración del modulo Bluetooth:</u>

La conexión entre la PC y el modulo de forma directa es usando un conversor USB-Serial:

 ![Conexion HC-05 y conversor USB a TTL](http://www.naylampmechatronics.com/img/cms/Blog/HC-05%20comandos%20AT/HC05%20Conversor%20TTL.JPG) 

## Configurando el modulo HC-05
Lo haremos en el modo AT 2 , manteniendo presionado el botón hasta alimentar el modulo. Se abre el Monitor Serial del IDE de Arduino y se elige "Ambos NL y CR" y la velocidad "38400 baud".

Primero se debe hacer el test de comunicación mandando AT y el monitor serial debe responder "Ok". 

##  Configurando nuestro módulo HC-05 como esclavo:
- Entrar en modo AT 1 o Modo AT 2
- Verificar si estamos en modo AT
Enviar: AT
Recibe: OK

- Establecer el Role como Esclavo
Enviar:  AT+ROLE=0
Respuesta: OK

- Configurar el Nombre del modulo
Enviar: AT+NAME= BTSlave
Respuesta: OK

- Establecer el Pin de vinculación
Enviar: AT+PSWD="1379"
Respuesta: OK

- Configura la Velocidad de configuración
Enviar: AT+UART=9600,0,0
Respuesta: OK

- Obtener la dirección de nuestro modulo bluetooth
Enviar: AT+ADDR?
Respuesta: +ADDR:<dirección>

Para verificar los datos cambiados se le agrega un "?":
Enviar: 
AT+ROLE?
AT+PSWD?
AT+UART?
AT+ADDR? 
Respuesta:
+ROLE:0
OK
+PSWD:1379
OK
+UART:9600,0,0
OK
+ADDR: 0019:09:037236
- Resetear el modulo para que salga del modo AT
Enviar: AT+RESET
Respuesta: OK

## Configurando nuestro modulo como maestro 
- Entrar en modo AT 1 o Modo AT 2
- Verificar si estamos en modo AT
Enviar: AT
Recibe: OK

- Establecer el Role como Maestro
Enviar:  AT+ROLE=1
Respuesta: OK

- Configurar el Nombre del modulo
Enviar: AT+NAME=BTMaster
Respuesta: OK

- Establecer el Pin de vinculación
Enviar: AT+PSWD="1379"
Respuesta: OK

- Configura la Velocidad
Enviar: AT+UART=9600,0,0
Respuesta: OK

- Configurar el modo de conexión para un dispositivo especifico
Enviar: AT+CMODE=0
Respuesta: OK

- Especificar la dirección del dispositivo a conectarse
Enviar: AT+BIND=0019:09:037236
Respuesta: OK

- Verificar los parámetros cambiados
Enviar: 
AT+ROLE?
AT+PSWD?
AT+UART?
AT+CMODE?
AT+BIND?

Respuesta:
+ROLE:1
OK
+PSWD:1379
OK
+UART:9600,0,0
OK
+CMOD:0
OK
+BIND:0019:09:037236
OK

- Resetear el modulo:
Enviar: AT+RESET
Respuesta: OK

## Primeras pruebas del modulo Bluetooth Slave controlado con el celular:

Con el siguiente programa a través de la aplicación del celular "Android bluetooth controller", se recibe en el serial de Arduino lo que se escribió en el celular.
Para eso debemos entrar a la aplicación, prender el bluetooth y seleccionar el dispositivo bluetooth a conectarse (BTSlave) y seleccionar el modo "Terminal mode" y las palabras que se escriban allí aparecerán en el Serial de Arduino.
[Primer programa con Bluetooth](https://github.com/matias1379/Ojo-de-van-gogh/tree/Sistema-de-vibracion/bt1)

El segundo programa que probaremos hay que entrar en la aplicación y seleccionar nuestro dispositivo bluetooth y seleccionar el modo Switch Mode y configurar que el verde es el estado "1" y el rojo el estado "0". Con este programa lo que hacemos es prender y apagar el led interno del Arduino que está en el pin 13.
[Prueba de encendido de un led con Bluetooth](https://github.com/matias1379/Ojo-de-van-gogh/tree/Sistema-de-vibracion/bt2)

