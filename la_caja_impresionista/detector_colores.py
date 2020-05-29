import os
import json

class detector_colores:
    
    r = int
    g = int
    b = int
    mx = int
    mn = int
    df = int
    v = int
    hue = int
    hsv = str


    def __init__ (self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def rgb_to_hsv(self):
        r = r/255.0
        g = g/255.0
        b = b/255.0
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

    


        

    
