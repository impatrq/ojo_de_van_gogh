# Sistema detector de color

## Programa para determinar color

Este programa consiste en convertir de acuerdo a los valores obtenidos del rgb, pasarlos a hsv ya que es un sistema de color que permite tener margenes en los colores, esto quiere decir, que varios valores pueden ser el mismo color. 
Hemos visto que con la variacion de H se pueden obtener ciertos colores, y le hemos agregrado funciones para poder detectar los colores blanco, gris, marron y negro, tomando parametros de estos para poder dar una lectura mas precisa. 

```python
def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    s = (df/mx)*100
    v = mx*100
    

    if ((mx == r) and (s>=50) and (v>=30) and (v<=60)): #es el valor de marron
      return 370
      
    if ((v>25) and (v<=60) and (s<=10)):  #es el valor de gris
      return 380
      
    if (mx==mn) and (v>15) and (v<60):
      return 380
      
    if ((mx >= (226/255)) and (mn >= (226/255))): #es el valor de blanco
      return 390
    
    if mx <= (25/255):  #es el valor de negro
      return 400
      
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    
    return h, s, v, df

print(rgb_to_hsv(255, 255, 255))
print(rgb_to_hsv(52,52,52))

name = rgb_to_hsv(r, g, b)

def print_color_name (name):
  if name < 15:
    return("color:rojo")
    
  elif name < 45:
    return("color:naranja")
    
  elif name < 90:
    return("color:amarillo")
    
  elif name < 150:
    return("color:verde")
    
  elif name < 210:
    return("color:cyan")
    
  elif name < 270:
    return("color:azul")
    
  elif name < 300:
    return("color:violeta")
    
  elif name < 345:
    return("color:rosa")
    
  elif name < 360:
    return("color:rojo")
    
  elif name == 370:
    return("color:marron")
    
  elif name == 380:
    return("color:gris")
    
  elif name == 390:
    return("color:blanco")

  else:
    return("color:negro")
```

##  Ejemplo de JSON en Python:

### 1. Creo un archivo  json

Este programa consiste en crear un json y poder tomar datos adentro del creador del archivo json. Luego a traves de la funcion json.dumps (datos) se devuelve el archivo Json creado.

```python
import json
hsv = 'rojo'
datos = {
    'color' : f'{hsv}'

}

json_str = json.dumps(datos)

print('Datos en formato JSON:', json_str)
```

### 2. Guardo y leo un Json

Este programa crea una funcion, a partir del dato que se le escribe en esta, escribe un archivo json y lo guarda en datos json . Luego con la funcion de ...('datos.json', 'r')... se lee el archivo y se muestra el dato Json

```python
import json
hsv = ""

def escJson (hsv):
	 datos = {
    'color' : f'{hsv}'
  }

  with open('datos.json', 'w') as file:
    json.dump(datos, file)
    
  with open('datos.json', 'r') as file:
    data = json.load(file)
    print(data)
    
escJson("verde")
```
### 3.  Se crea un archivo json y depende de lo que se le ponga en escJson(), es el json obtenido 

```python
import json
hsv = ""

def escJson (hsv):
  datos = {
    'color' : f'{hsv}'
  }

  json_str = json.dumps(datos)

  print(json_str)
    
escJson("violeta")
```

### 4. En este modelo se prueba el json con un color ingresandolo abajo

```python
hsv = ""

def escJson (hsv):
  import json
  datos = {
    'color' : f'{hsv}'
  }

  json_str = json.dumps(datos)

  print(json_str)
    
name = 0


def print_color_name (name):
  if name < 15:
    escJson("rojo")
    
  elif name < 45:
    escJson("naranja")
    
  elif name < 90:
    escJson("amarillo")
    
  elif name < 150:
    escJson("verde")
    
  elif name < 210:
   escJson("cyan")
    
  elif name < 270:
    escJson("azul")
    
  elif name < 300:
    escJson("violeta")
    
  elif name < 345:
    escJson("rosa")
    
  elif name < 360:
    escJson("rojo")
    
  elif name == 370:
    escJson("marron")
    
  elif name == 380:
    escJson("gris")
    
  elif name == 390:
    escJson("blanco")

  else:
    escJson("negro")
    
print_color_name (140)    
```
### 5. Pasar de RGB a HSV y de HSV a color

En este programa se combinaron las pruebas de las anteriores y con este codigo ingrando valores de r,g,b se obtiene un color con formato json
```python
def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    s = (df/mx)*100
    v = mx*100
    hue = 0
    

    if ((mx == r) and (s >= 50) and (v >= 30) and (v <= 60)): #es el valor de marron
      return 370
      
    if ((v > 25) and (v <= 60) and (s <= 10)):  #es el valor de gris
      return 380
      
    if (mx==mn) and (v>15) and (v<60):
      return 380
      
    if ((mx >= (226/255)) and (mn >= (226/255))): #es el valor de blanco
      return 390
    
    if mx <= (25/255):  #es el valor de negro (NO DEBE SER TAN NEGRO!)
      return 400
      
    elif mx == r:
        hue = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        hue = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        hue = (60 * ((r-g)/df) + 240) % 360
    
    return hue

name = rgb_to_hsv(r, g, b)

hsv = str(0)

def escJson (hsv):
  import json
  datos = {
    'color' : f'{hsv}'
  }

  json_str = json.dumps(datos)

  print(json_str)
    

def print_color_name (name):
  if name < 15:
    escJson("rojo")
    
  elif name < 45:
    escJson("naranja")
    
  elif name < 90:
    escJson("amarillo")
    
  elif name < 150:
    escJson("verde")
    
  elif name < 210:
   escJson("cyan")
    
  elif name < 270:
    escJson("azul")
    
  elif name < 300:
    escJson("violeta")
    
  elif name < 345:
    escJson("rosa")
    
  elif name < 360:
    escJson("rojo")
    
  elif name == 370:
    escJson("marron")
    
  elif name == 380:
    escJson("gris")
    
  elif name < 390:
    escJson("blanco")

  else:
    escJson("negro")
```


