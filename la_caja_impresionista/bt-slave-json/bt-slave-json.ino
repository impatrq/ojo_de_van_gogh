#include <ArduinoJson.hpp>        //incluyo librerias de Json
#include <ArduinoJson.h>
#include <SoftwareSerial.h>       //incluyo libreria para cambiar pines de serial
SoftwareSerial BTSlave (10, 11);  //pin RX=10, pin TX=11

String str = "";                  //variable que hace el string del json
const int buzzer=8;               //pin del vibrador o buzzer

// Funcion de deserializar Json
String DeserializarJson(String json)  //Devuelve un string y pide el string json
{
    StaticJsonDocument<300> doc;// se crea un objeto llamado doc con 300 bytes de memoria
    DeserializationError error = deserializeJson(doc, json);  //se deserializa el documento y la variable json
    if (error) { return; }                                    // si hay error devolver nada
 
    String color = doc["colour"]; //busco el documento "colour" y guardo lo que contiene 
    Serial.println(color);        //se imprime el contenido de colour, osea rojo
    return color;
}

void setup() {

 Serial.begin(9600);        //Inicializa puerto serie 
 BTSlave.begin(9600);    //Inicializa puerto serie de BT
 
}

void loop() {
  
  while(BTSlave.available()>0){ //mientra llega informacion por BT 
   char caracter=BTSlave.read();    //leo y guardo en caracer
     if (caracter != '}'){    //si caracter es distinto a la llave
      str.concat(caracter); //guardo en str cada caracter y formo string
     }
     else{
      str.concat('}');//agrego la llave 
      String color = DeserializarJson(str); //deserializo str y guardo en color
                 
      //Si es rojo hago tal ruido
       if(color=="rojo"){
        tone(buzzer,440);
        delay(1000);
        noTone(buzzer);
        delay(100);
        Serial.println("Está sonando el color: rojo");
       
      }
      //Si es verde hago tal ruido
      if(color=="verde"){
        tone(buzzer,880);
        delay(1000);
        noTone(buzzer);
        delay(1000);
        Serial.println("Está sonando el color: verde");
        
       }
      //Si es azul hago tal ruido
       if(color=="azul"){
        tone(buzzer,2000);
        delay(1000);
        noTone(buzzer);
        delay(2000);
        Serial.println("Está sonando el color: azul");
       }   
     }
  }
}
