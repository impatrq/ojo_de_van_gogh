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
    hue = float
    hsv = str


    def __init__ (self):
        pass
        

    def rgb_to_hsv(self,r,g,b):
        self.r = r/255.0
        self.g = g/255.0
        self.b = b/255.0
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
    
    def print_to_audio(self, hsv):

      self.hsv = hsv

      if hsv < 15:
         os.system('mpg321 rojo.mp3 &')

      elif hsv < 45:
            os.system('mpg321 naranja.mp3 &')
            
      elif hsv < 90:
            os.system('mpg321 amarillo.mp3 &')
            
      elif hsv < 150:
            os.system('mpg321 verde.mp3 &')
            
      elif hsv < 210:
            os.system('mpg321 cyan.mp3 &')
            
      elif hsv < 270:
            os.system('mpg321 azul.mp3 &')
            
      elif hsv < 300:
            os.system('mpg321 violeta.mp3 &')
            
      elif hsv < 345:
            os.system('mpg321 rosa.mp3 &')
            
      elif hsv < 360:
            os.system('mpg321 rojo.mp3 &')
            
      elif hsv == 370:
            os.system('mpg321 marron.mp3 &')
            
      elif hsv == 380:
            os.system('mpg321 gris.mp3 &')
            
      elif hsv < 390:
            os.system('mpg321 blanco.mp3 &')

      else:
            os.system('mpg321 negro.mp3 &')    

    

        

    

       
    def print_color_name(self,hsv):
        
         self.hsv = hsv
         if hsv < 15:
            return "rojo"  

         elif hsv < 45:
            return "naranja"

         elif hsv < 90:
            return "amarillo"

         elif hsv < 150:
            return "verde"

         elif hsv < 210:
            return "cyan"

         elif hsv < 270:
            return "azul"

         elif hsv < 300:
            return "violeta"

         elif hsv < 345:
            return "rosa"

         elif hsv < 360:    
            return "rojo"

         elif hsv == 370:
            return "marron"

         elif hsv == 380:
            return "gris"

         elif hsv < 390:
            return "blanco"

         else:
            return "negro"

         