# Sistema de vibraciones de acuerdo al color

Los primeros programas fueron para empezar a entender el funcionamiento de Json y poder realizar los programas con los que se simula el proyecto.

## Crear Objeto  Json

Este programa usa las librerías ArduinoJson para crear un objeto Json y  deserializar un archivo Json, es decir, se obtiene el valor del documento. 
[Programa para crear Objeto JSON](https://github.com/matias1379/Ojo-de-van-gogh/tree/master/Sistema-de-vibracion/objetoJson)

## Crear Array Json
Este programa usa las librerías ArduinoJson para crea un array  Json, y lo deserializa, es decir, se obtiene cada parte del array 
[Programa para crear Array JSON](https://github.com/matias1379/Ojo-de-van-gogh/tree/master/Sistema-de-vibracion/arrayJson)

## Crear objeto color Json
Este programa usa las librerías ArduinoJson para poder crear un objeto Json, y también poder deserializar ese mismo que se creo obteniendo el valor del documento.
Esto se hace pidiendo un String en el DeserializarJson , que en este caso es el archivo que se serializo que devuelve el String json que creo el objeto. Luego se realiza la deserializacion y se devuelve el String color, obteniendo el valor del documento, que en este caso es : rojo.
[Programa para obtener color JSON](https://github.com/matias1379/Ojo-de-van-gogh/tree/master/Sistema-de-vibracion/color-deserializado)

# Programas finales: 

## Bluetooth master con Json
Este programa simula que se detecta el pestañeo a traves del  sensor cerebral , realiza la foto y convierte el documento Json en un char Array para ser mandado del Bluetooth master al Bluetooth slave.
[Programa para mandar el Json en un char Array por Bluetooth](https://github.com/matias1379/Ojo-de-van-gogh/tree/master/Sistema-de-vibracion/bt-master-json)

## Bluetooth slave con Json
Este programa recibe la informacion como char Array y lo convierte en un string a traves de la funcion concat. Luego de eso realiza el proceso de deserializar y obtener el valor del documento colour, dando como resultado rojo. Dependiendo del color que llegue se hara una determinada vibracion.
[Programa que detecta el color y realiza una vibración](https://github.com/matias1379/Ojo-de-van-gogh/tree/master/Sistema-de-vibracion/bt-slave-json)