| Codigo | Colores  |
| :----: | :------: |
|  0000  |  blanco  |
|  0001  |   rojo   |
|  0010  | marron |
|  0011  |   naranja   |
|  0100  | amarillo  |
|  0101  |  dorado   |
|  0110  | beige  |
|  0111  |  violeta   |
|  1000  |  rosa   |
|  1001   |  purpura  |
|  1010   | verde |
|  1011   |   azul   |
|  1100   | cyan  |
|  1101   |   plata  |
|  1110   | gris  |
|  1111   | negro  |



```
def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    s = (df/mx)*100
    v = mx*100
    if mx <= (25/255):
      print("negro")
    if ((mx >= (226/255)) and (mn >= (226/255))):
      print ("blanco")
    if ((v>25) and (v<=60) and (s<=10)):
      print ("gris")
    if ((mx == r) and (s>=50) and (v>=30) and (v<=60)):
      print ("marron")
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
       

    return h, s, v

print(rgb_to_hsv(226, 226, 226))
print(rgb_to_hsv(152, 137, 137))
print(rgb_to_hsv(79, 43, 27))
print(rgb_to_hsv(25, 25, 25))
```


