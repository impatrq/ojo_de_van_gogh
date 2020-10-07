/*
  Morse.c -  
*/
 
#include "Arduino.h"
#include "Morse.h"
 
void punto(){
  tone(9, 440);
  delay(250);
  noTone(9);
  delay(250);  
}
 
void raya(){
  tone(9, 440);
  delay(1000);
  noTone(9);
  delay(250); 
}

void blanco(){
  punto(); punto(); punto(); punto();
}

void rojo(){
  punto(); punto(); punto();raya();
}

void marron(){
  punto(); punto(); raya(); punto();
}

void naranja(){
  punto(); punto(); raya();raya();
}
void amarillo(){
  punto(); raya(); punto(); punto();
}

void verde(){
  punto(); raya(); punto();raya();
}

void cyan(){
  punto(); raya(); raya(); punto();
}

void azul(){
  punto(); raya(); raya();raya();
}

void violeta(){
  raya(); punto(); punto(); punto();
}

void rosa(){
  raya(); punto(); punto();raya();
}

void gris(){
  raya(); punto(); raya(); punto();
}

void negro(){
  raya(); raya(); raya();raya();
}
