# Correr script cada vez que se prenda la Raspberry

Desde remote.it se entra a la raspberry y por ssh usando Putty se realizo todo esto:

Se crea un archivo :

```bash
nano script_automatico.sh # con esto se crea el archivo y entramos
```

Luego adentro del script se escribe:

#!/bin/bash  Esta línea define qué shell utilizaremos, que es el Bash de shell en nuestro caso.

python3 main.py lo que hace es ejecutar el main.py que es donde esta el codigo que da el color en Json

```bash
#!/bin/bash 

python3 main.py 
```

Tocamos control O para guardar el archivo, enter y luego control X para salir

Para que el archivo sea ejecutable y no muestre que no tiene permisos se usa:

```bash
chmod +x ./script_automatico.sh
```

Luego se ejecuta para probar que el programa ande, con:

```bash
./script_automatico.sh
```

## Usar Crontab

Se ejecuta en el terminal

crontab -e , en nuestro caso elegimos nano, osea 1, y ahi se escribe:

```bash
@reboot /home/pi/script_automatico.sh
```

Con este se indica que cada vez que se reinicie la Raspberry, se iniciara el script_automatico.sh que este ejecuta el main.py

Para reiniciar la Raspberry se usa el comando **<u>sudo reboot</u>**

