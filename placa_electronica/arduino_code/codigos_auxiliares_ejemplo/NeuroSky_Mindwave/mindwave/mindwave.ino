//                                                         //
//    Program       : Mindwave with Arduino                //
//    Interfacing   : HC-05 Bluetooth Module               //
//    Output        : Eye Blink Control LED                //
#include "mindwave.h"

#define BAUDRATE 57600
#define LED 5
#define Theshold_Eyeblink 110
#define EEG_AVG 70

int Plength;

Mindwave mindwave(
    BAUDRATE,
    LED,
    Theshold_Eyeblink,
    EEG_AVG);

void setup()
{
  Serial.begin(BAUDRATE); // USB
  pinMode(LED, OUTPUT);
  for (int h = 0; h < 10; h++)
  {
    Serial.println("Empezo el void setup");
  }

  mindwave.Esperar_al_mindwave();

  Serial.println("Empezo a calibrar");

  mindwave.Calibrar_Sensor();
}

void loop() // Main Function
{
  if (mindwave.ReadOneByte() == 170) // AA 1 st Sync data
  {
    if (mindwave.ReadOneByte() == 170) // AA 2 st Sync data
    {
      Plength = mindwave.ReadOneByte();
      if (Plength == 4) // Small Packet
      {
        mindwave.Small_Packet();
      }
      else if (Plength == 32) // Big Packet
      {
        mindwave.Big_Packet();
        Serial.println("BigPacket");
      }
    }
  }
}
