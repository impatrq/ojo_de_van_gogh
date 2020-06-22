#include "Arduino.h"
#include "mindwave.h"

#define BAUDRATE 57600
#define LED 5
#define Theshold_Eyeblink 110
#define EEG_AVG 70

Mindwave::Mindwave(BAUDRATE, LED, Theshold_Eyeblink, EEG_AVG)
{
   this.BAUDRATE = BAUDRATE;
   this.LED = LED;
   this.Theshold_Eyeblink = Theshold_Eyeblink;
   this.EEG_AVG = EEG_AVG;
}

byte Mindwave::ReadOneByte() // One Byte Read Function
{
   while (!Serial.available())
      ;
   ByteRead = Serial.read();
   return ByteRead;
}

void Mindwave::Small_Packet()
{
   generatedchecksum = 0;
   for (int i = 0; i < Plength; i++)
   {
      payloadDataS[i] = ReadOneByte(); //Read payload into memory
      generatedchecksum += payloadDataS[i];
   }
   generatedchecksum = 255 - generatedchecksum;
   checksum = ReadOneByte();
   if (checksum == generatedchecksum) // Varify Checksum
   {
      if (j < 512)
      {
         Raw_data = ((payloadDataS[2] << 8) | payloadDataS[3]);
         if (Raw_data & 0xF000)
         {
            Raw_data = (((~Raw_data) & 0xFFF) + 1);
         }
         else
         {
            Raw_data = (Raw_data & 0xFFF);
         }
         Temp += Raw_data;
         j++;
      }
      else
      {
         Onesec_Rawval_Fun();
      }
   }
}
