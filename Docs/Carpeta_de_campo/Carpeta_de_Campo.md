

# Carpeta de Campo 

## Semana 15/03 - 22/03


Escribimos una declaración jurada sobre la compra del NeuroSky Mindwave debido a que Matías Pierri tuvo la oportunidad de que un conocido se lo compre en USA Y abaratar costos


[Declaracion Jurada](https://github.com/matias1379/Ojo-de-van-gogh/blob/master/Presupuesto-y-documentaciones/DeclaracionSensor.pdf)


Investigamos sobre vibradores y llegamos a la conclusión de que lo mas viable es reciclar vibradores de teléfonos viejos como los Nokia. Un motor vibrador es un motor común en el cual se le pone un peso en la punta del émbolo lo que lo hace vibrar, además se coloca dentro de un contenedor que aumenta la vibración.


Establecimos el entorno de trabajo BT con Arduino usando los HC-05. En base a las conclusiones confeccionamos una guía de como usar dicho entorno 


[Establecer conexion entre BT](https://github.com/matias1379/Ojo-de-van-gogh/blob/master/Presupuesto-y-documentaciones/Entorno%20de%20trabajo%20de%20Arduino%20con%20Bluetooth.md)


Usando Arduino logramos hacer vibrar los vibradores extraídos del Nokia usando la función Tone() and noTone() que te permite poner la frecuencia de vibración la cual va a variar según lo que se necesite


[Sistema de vibracion](https://github.com/matias1379/Ojo-de-van-gogh/blob/master/Presupuesto-y-documentaciones/Sistema%20de%20Vibraci%C3%B3n.md)


Como la Raspberry se maneja con JSON estuvimos aprendiendo a como procesar un string JSON en Arduino y poder hacer el intercambio de datos entre Raspberry y Arduino por BT. Nos dimos cuenta que para que se lean bien los datos hay que usar Serial.readString() ya que Serial.read() solo detecta que entra un char 


> **JSON** (acrónimo de  JavaScript Object Notation, «notación de objeto de JavaScript») es un  formato de texto sencillo para el intercambio de datos.


Empezamos a trabajar con el sensor cerebral conectado a un teléfono y logramos que cuando parpadee el usuario, el teléfono lo detecte pero esto es una app y no nos permite tocarla mucho para usarla en nuestro Arduino pero era a modo de primeros pasos. Usando un modulo bluetooth y comandándolo por AT tratamos de configurarlo insertando los siguientes datos


> Baudrate = "576000"
>
> BIND ADDR= "0081,f9,29eb31"
>
> PSSW = "1234"


Con esta configuración no funciono ya que la password estaba mal puesta. Viendo la documentación nos dimos cuenta que la pass es 0000


> PSSW CORRECTA ="0000"


Ya de esta forma pudimos conectar el Arduino con el HC-05 pero con el example que nos da el fabricante solo podemos medir nivel de atención y relajación. Tenemos que investigar como medir nivel de pestañeo. Sin embargo hicimos una prueba donde se prenden leds de acuerdo a que tan concentrado esta el usuario


Establecimos el entorno de trabajo en Google Visión IA que es usar la Nube de Google para, a través de un sistema de redes neuronales, obtener un análisis de lo que se ve en una foto. Para esto tuvimos que crear un proyecto en Google Cloud Services y habilitar la api de Google Vision AI. Una vez habilitado esto nos dan un archivo JSON que tiene nuestra API Key y la insertamos en la Raspberry usando 


```Raspbian Terminal
export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/filename.json
```


Una vez seteada la Raspberry se usan los siguientes comandos para instalar las dependencias necesarias


```Linux Terminal
   python3 -m pip install --user pip
   python3 -m pip install --user google-cloud-vision
   python3 -m pip install --user Pillow
   python3 -m pip install --user picamera
```


Usamos este comando para sacar una foto 


```RAspbian
   raspistill -o cam.jpg
```


Y este ejemplo para poder probar el análisis de la foto 


```Raspbian terminal
python3 camera_vision_face.py
```


Nos devuelve este análisis donde la Raspberry se encargo de detectar las personas que aparecen en la foto en este caso Theo. Lo borroso de la foto se debe a que Theo tiene el celu que no enfoca, la definición en si de la Pi Camera es bastante buena


<img src="/home/matias/Downloads/WhatsApp Image 2020-03-18 at 22.57.52.jpeg" alt="Un tipo que maneja inteligencia artificial" style="zoom: 33%;" />


Ahora tenemos que ver como usar la Raspberry para conectarla al BT y además que todos estos programas que describimos antes estén funcionando en Loop y de forma automática cuando se prende la Raspberry.


## Semana 22/03 - 29/03


Estuvimos viendo documentaciones y aparentemente para poder leer el valor de Blink Strength tenemos que escribir en el registro **0x16** 


![Registros tabla](/home/matias/Downloads/RegistrosNeurosky.jpeg)


Se hicieron ejemplos con Arduino para empezar a leer los datos Json que se recibirán de la Raspberry. Se han hecho pruebas de como formar un Json y como obtener el valor de Json.
Luego se probo mandar archivos String por BT, pero nos dimos cuenta que la función no permite mandar Strings por BT:


```
BTMaster.write()
```
Se ha visto varios videos o formas de intentar mandar el String por BT de otra forma, pero no se ha conseguido, entonces se empezó a investigar para pasar un String a un char Array. Se ha encontrado un ejemplo en el que muestra que la función: 
```
str.toCharArray(charArray,buf)
```
Siendo str el String ingresado, charArray, la variable donde se guarda el charArray y buf la cantidad máxima a convertir de String en char Array.


Se ha tenido problemas con esta función ya que dependiendo del orden en el que se declaraba el String, funcionaba o no. Pero se ha logrado descubrir el error, creando 2 programas: 
-	Uno que simula el parpadeo, sacar foto y mandar el String Json por BT a través de un charArray
-	El otro que recibe el char Array y lo convierte en un String, y obtiene el valor del Json de color y de acuerdo al color realiza una vibración
[Sistema de vibraciones con Json y BT](https://github.com/matias1379/Ojo-de-van-gogh/blob/master/Presupuesto-y-documentaciones/Sistema%20de%20vibraciones%20de%20acuerdo%20al%20color.md)

## Semana 29/03 al 05/04
Se crearon las piezas en 3D del cargador de pilas. Las piezas están diseñadas teniendo en cuenta las plaquetas que van a ir colocadas y están los agujeros para los respectivos cables.

[Planos Cargador PDF ](https://github.com/matias1379/Cargador-de-pilas/tree/master/Alimentacion/cargador%203D/Dibujos%20en%20PDF)

Analizamos el problema que creamos en el repositorio de Ojo de van gogh ya que nos mezclamos con el manejo de branches y mil problemas entonces decidimos crear repositorios por cada área de trabajo del proyecto y los archivos de documentación y publicidad manejarnos por drive. 
Los repos quedan de la siguiente manera:
- [Mindwave]( )
- [ArduinoVibrador   ](https://github.com/matias1379/ArduinoVibrador)
- [Raspberry](https://github.com/matias1379/Raspberry)
- [Cargador de pilas]([https://github.com/matias1379/Cargador-de-pilas](https://github.com/matias1379/Cargador-de-pilas))

Ahora nos manejamos con ramas donde la versión final y estable del repo va a Máster y luego cada feature se desarrolla en una rama paralela. Luego de hacerle el testing a la misma y ver que no hayan conflicto se hace un merge (se fusiona la rama con el máster y se cierra la rama)

Con respecto al mindwave decidimos poner en pausa el código del micro porque nos estábamos perdiendo con el tema del payload. Encontramos varios repos en github con los códigos en python donde al ejecutarlos te otorgan los datos. El plan es conectar por BT el mindwave a la compu y correr el script. Una vez que el mismo este listo 

Nos estamos contactando con varias empresas preguntando sobre plaquetas flexibles para el sistema de vibración aunque también se esta evaluando la opción de utilizar los brazaletes porta celulares para correr. Se ha realizado el PCB del sistema ya que una empresa nos contacto y nos lo pidió para saber el tamaño y complejidad.
[PCB-Vibrador](https://github.com/matias1379/ArduinoVibrador/blob/PCB/CodigosEjemplos/vibrador/PCB-Vibrador.pdf)

## Semana 05/04 al 12/04

Hemos recibido las respuestas de las empresas por plaquetas flexibles y nos ha parecido muy elevados los costos por lo cual optamos por usar un brazalete para celulares de un tamaño de 18cm x 10 cm y se ha realizado el esquemático del circuito donde estará la Raspberry con la cámara, el Arduino Nano, el Bluetooth, dos pilas, un regulador y los vibradores.

Hemos calculado el consumo total del circuito para saber que tenemos que usar dos pilas de 3.7V ya que con una nos duraría poco tiempo, y por esto se ha investigado sobre Step down, ya que tiene mejor rendimiento que un regulador.

También se ha realizado una librería para los colores en Arduino, y hemos encontrado el problema que si haces un archivo con la extensión:  ".c " salta un error y se soluciono esto cambiando la extensión del archivo a ".cpp"

Se ha investigado sobre el mindwave y el funcionamiento de un programa y se ha conseguido que se detecte el parpadeo pero también se detecta el parpadeo no forzado y para eso estamos viendo como solucionarlo.

Se ha conseguido que la Raspberry nos entregue el color en RGB con Json

Se ha comprado un dominio y estamos haciendo la pagina web a traves de un localHost (Xampp) y usando WordPress. Se ha elegido el tema de la pagina que es BlackootLite.
## Semana  12/04 al 19/04

Se ha terminado el PCB de la placa

Montamos el host en 000webhost que nos ofrece 300 Mb de espacio y le instalamos wordpress. Tuvimos problemas con el dominio así que contactamos a soporte técnico de hostinger y nos solucionaron el problema.

> Click  [aqui](ojodevangogh.tech) para entrar a nuestra pagina

Encontramos un modulo de python que pasa de RGB a nombre de color y funciona pero tienen sus limitaciones. El tema es que no da resultado a todos los RGB sino a los que son fáciles tales como  0,0,0 que da black pero si le metemos algo como 65,23,19 ya se pierde.

Encontramos una alternativa basandonos en las cosas que nos otorga el dios Luis llamas 

> [Luis llamas el dios de los colores](https://www.luisllamas.es/arduino-sensor-color-rgb-tcs34725/)

Donde podemos pasar de rgb a hsv que nos permite saber las distintas tonalidades de un color ya que distingue de rojo oscuro y rojo claro y nos permite tomas los dos como rojo. Gracias a esto ya poseemos 12 colores identificables

La pagina web se nos fue a la mierda. Nos suspendieron la pagina porque aparentemente superamos el limite de visitas al entrar a verla y nos dicen que si no pagamos en 7 días nos la borran.

Nos comunicamos con webhost a ver si hay alguna alternativa pero no nos contestan así que no nos queda otra que pagar y mudarnos a hostinger

## Semana 19/04 al 25/04

Pagamos la migración de nuestro pag a hostinger que nos salió 10 dolares. Tenemos que esperar 48 hs a que nos digan si salió todo bien y no perdimos la pagina.

Recuperamos la pagina y esta todo en orden aunque se nos desconfiguró el dominio y tenemos que cambiarlo así responde a ojodevangogh.tech . Eso si no podemos entrar al panel de wordpress por alguna razón.

Nos comunicamos con hostinger y después de unos largos idas y vueltas de email mudamos completamente la pagina ya no tenemos nada en webhost esta todo en hostinger y funca todo. Habilitamos la certificación ssl así que nuestro pagina es segura y ya tenemos acceso al panel de wordpress. 

Tenemos un problema en el responsive desing que hace que desaparezcan los botones de la pag cuando usamos una version mobile y no sabemos que hacer



## Semana 25/04 al 3/5

Vimos que no había manera de solucionar el responsive design mas que pagar el upgrade del theme de wordpress a premium que son 40 dolares así que pincho. 

Empezamos la búsqueda y encontramos uno llamos astrid que esta muy piola visualmente y tiene mucha opción de personalizacion. Lastimosamente no podiamos cambiarle el fondo blanco asi que para que no queme tanto le colocamos letra Arial que es mas gruesa y llama la atención.

Le instalamos un plugin a la pagina para que aparezcan botones que vinculen la pag con ig linkedin llamado UltimateShare.

Creamos una pagina de Instagram para empezar a subir cosas y ya grabamos unos videos pro de como la Raspberry reconoce colores y como a través de un color seleccionado funcionan los vibradores

Para un mejor orden creamos un repositorio nuevo donde metimos todas las cosas de los pequeños repos a través de git flow que permite ordenar todo en feature y que no se vaya todo a la mierda

Para armar cosas facheras para redes sociales hicimos que la plaqueta tenga todos los micros y cosas con modelos 3D asi verlos con el visor 3D de KiCAD

## Semana 03/05 al 11/05

Se hizo una intro para el video en After Fx, se le puso musica de fondo y se subio a Ig y a la pagina web el primer video mostrando como se reconoce el color con la cámara de la Raspberry

Tambien se definio el modelo para hacer la tapa del cargador de pila y se empezó a hacerla. 

Se agregó un pluggin para que la pagina cargue mas rapido y se corrigio el logo para que no sea de fondo blanco y pueda verse. 

## Semana 11/05 al 18/05

Se empezo a intentar conectar la raspberry con el sensor cerebral y se configuro esta para que trabaje por Remote

Agregamos con gtts para que se pueda escuchar el color y lo probamos con un parlante y anduvo. Para traducir el texto color a voz se creo una nueva funcion que envia archivo txt que los recibe el gtts y los reproduce en un parlante

Para la PRIMER ENTREVISTA DE RADIO, se realizo una tarjeta publicitaria que se subio a Ig y como se escucho bajo, se edito el  audio grabado y se preparó para subirlo a IGTV y quedamos en que cuando la situacion del pais lo permita, nos volveremos a juntar para contar los nuevos avances.

Se daño el disco de la computadora y perdimos lo que teníamos hecho de la tapa y no se habia subido a git.

## Semana 18/05 al 25/05

La raspberry no lee el payload del Mindway y estamos con ese problema que no sabemos como resolverlo

Se hizo un Backup de la pagina web porque se nos vencía el mes de Hostinger pero debido a un error que tuvieron nos regalaron un mes y ya elegimos que para el mes proximo vamos a cambiar al host de Sitio Hispano que nos saldría $860 el año ya que no se puede pagar por mes

Estuvimos pensando y se nos ocurrio que nuestra pagina tiene que tener para que los ciegos la puedan leer, entonces agregamos el Plugin Responsive Voice que permite a traves de un boton reproducir el contenido de cada pagina.

Se edito y subio el IGTV de la nota de radio y tambien subimos el link de la pagina que hizo la radio FM106.5 sobre esta nota. Tambien subimos una historia de "Quienes somos" y la dejamos como destacada

Se terminó la tapa y se empezó a realizar el encastre en la caja.

Se empezó a investigar sobre como agregar para que se pueda leer un texto a traves de la camara, usando OCR que nos da Google Vision.