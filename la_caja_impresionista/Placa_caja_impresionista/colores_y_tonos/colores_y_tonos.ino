const int buzzer=9;
int tono;
void setup() {
  Serial.begin(9600);
  Serial.println("Escribe el color: verde, rojo, azul");
}

void loop() {
if(Serial.available()){ //si llega informacion por Serial
   tono=Serial.read();    //leo y guardo en tono

   //Si es 1 hago tal ruido
     if(tono=='1'){
      //le agregue este for para que se repita 4 veces
      for(c = 0, c <= 4, c++) {
        tone(buzzer,440);
        delay(1000);
        noTone(buzzer);
        delay(100);
     
        Serial.println("Está sonando el color: verde");
      }
      c = 0;  
    }
    //Si es 2 hago tal ruido
    if(tono=='2'){
    
      for(c = 0, c <= 4, c++){
        tone(buzzer,880);
        delay(1000);
        noTone(buzzer);
        delay(1000);
        Serial.println("Está sonando el color: rojo");
      }
     c = 0;
     }
  //Si es 3 hago tal ruido
     if(tono=='3'){
      for(c = 0, c <= 4, c++){
        tone(buzzer,2000);
        delay(1000);
        noTone(buzzer);
        delay(2000);
        Serial.println("Está sonando el color: azul");
      }
      c = 0;
     }   
     
     Serial.println("Escribe el color: verde, rojo, azul");
  }
}
