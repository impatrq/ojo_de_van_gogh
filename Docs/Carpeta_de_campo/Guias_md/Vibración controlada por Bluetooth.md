# Vibración controlada por Bluetooth

En estos programas se han combinado los programas de bluetooth con el de sistema de vibración. Hay dos programas, el del BT Master y el del BT Slave. 

## BT Master
Este programa consiste en mandar la información del serial al Bt Slave para que este la procese y realice alguna acción. Antes de esto el BT ha sido configurado con su nombre, contraseña y para que se conecte al BT Slave .
[Programa del BT Master](https://github.com/matias1379/Ojo-de-van-gogh/tree/Sistema-de-vibracion/bt-master)

## BT Slave 
Este programa recibe la información del BT Master y dependiendo del numero recibido (color) hace una determinada frecuencia por un determinado tiempo, repitiendo esto 5 veces por el for.
[Programa del BT SLave](https://github.com/matias1379/Ojo-de-van-gogh/tree/Sistema-de-vibracion/bt-slave)