#include <ArduinoJson.hpp>        //incluyo librerias de Json
#include <ArduinoJson.h>
#include <SoftwareSerial.h>       //incluyo libreria para cambiar pines de serial
SoftwareSerial BTMaster (8, 9);  //pin RX=8, pin TX=9
String color;
// Funcion de serializar Json
String SerializarJson()
{
    String json;  
    StaticJsonDocument<300> doc;  // se crea un objeto llamado doc con 300 bytes de memoria
    doc["colour"] = ""+String(color);       //el documento colour tiende valor a rojo
    
    serializeJson(doc, json);     //se serializa el doc y guarda en json
    return json;
}

int str_len =SerializarJson().length()+1;
char charArray[100];

void setup() {

 Serial.begin(9600);        //Inicializa puerto serie 
 BTMaster.begin(9600);    //Inicializa puerto serie de BT
 //Serial.println("Elija un color");
}

void loop() {
  
  if(Serial.available()>0){ //Si en el serial hay un dato
     color = Serial.readString(); 
       SerializarJson().toCharArray(charArray, 100);    //hago el string json en un char array
       Serial.println("Color detectado:"+String(color));
       Serial.println("El color sensado es:"+String(color));
       Serial.println("***************");
       BTMaster.write(charArray); //escribo en el bt el char array
        
  }
     
}
