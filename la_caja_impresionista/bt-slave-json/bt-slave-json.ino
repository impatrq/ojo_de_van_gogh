#include <ArduinoJson.hpp>        //incluyo librerias de Json
#include <ArduinoJson.h>
#include <SoftwareSerial.h>       //incluyo libreria para cambiar pines de serial
#include "Morse.h"                //incluyo libreria para la vibracion 
SoftwareSerial BTSlave (10, 11);  //pin RX=10, pin TX=11

String str = "";                  //variable que hace el string del json

// Funcion de deserializar Json
String DeserializarJson(String json)  //Devuelve un string y pide el string json
{
    StaticJsonDocument<300> doc;// se crea un objeto llamado doc con 300 bytes de memoria
    DeserializationError error = deserializeJson(doc, json);  //se deserializa el documento y la variable json
    if (error) { return; }                                    // si hay error devolver nada
 
    String color = doc["colour"]; //busco el documento "colour" y guardo lo que contiene 
                //se imprime el contenido de colour, osea rojo
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
      Serial.println(str);
      str = "";
   
       //Se ejecuta la funcion de acuerdo al color
        if(color=="blanco"){
        blanco();
        Serial.println("Está sonando el color: blanco");
        }
                 
        else if(color=="rojo"){
        rojo();
        Serial.println("Está sonando el color: rojo");
        }

        else if(color=="marron"){
        marron();
        Serial.println("Está sonando el color: marron");
        }
                 
        else if(color=="naranja"){
        naranja();
        Serial.println("Está sonando el color: naranja");
        }

        else if(color=="amarillo"){
        amarillo();
        Serial.println("Está sonando el color: amarillo");
        }
                 
        else if(color=="verde"){
        verde();
        Serial.println("Está sonando el color: verde");
        }

        else if(color=="cyan"){
        cyan();
        Serial.println("Está sonando el color: cyan");
        }

        else if(color=="azul"){
        azul();
        Serial.println("Está sonando el color: azul");
        }
        
        else if(color=="violeta"){
        violeta();
        Serial.println("Está sonando el color: violeta");
        }
      
        else if(color=="rosa"){
        rosa();
        Serial.println("Está sonando el color: rosa");
        }
                 
        else if(color=="gris"){
        gris();
        Serial.println("Está sonando el color: gris");
        }
                 
       else if(color=="negro"){
        negro();
        Serial.println("Está sonando el color: negro");
        }
       Serial.println("***************");
     }
  }  
}
