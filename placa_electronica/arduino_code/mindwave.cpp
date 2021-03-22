#include "Arduino.h"
#include "mindwave.h"



Mindwave::Mindwave(int _BAUDRATE,char _LED, char _Theshold_Eyeblink,char  _EEG_AVG)
{
   BAUDRATE = _BAUDRATE;
   LED = _LED;
   Thesold_Eyeblink = _Theshold_Eyeblink;
   EEG_AVG = _EEG_AVG;
}

byte Mindwave::ReadOneByte() // One Byte Read Function
{
   while (!Serial.available())
      ;
   ByteRead = Serial.read();
   return ByteRead;
}

void Mindwave::Eye_Blink()
{
   
   if (Eye_Enable)
   {
      if (On_Flag == 1 && Off_Flag == 0)
      {
         if ((Avg_Raw > Thesold_Eyeblink) && (Avg_Raw < 350))
         {
            digitalWrite(LED, HIGH);
            Serial.Write("1");
         }
         else
         {
            if (Avg_Raw > Umbral_de_parpadeo)
            {
               On_Flag == 0;
               Off_Flag == 1;
            }
            digitalWrite(LED, LOW);
            Serial.println("0");
         }
      }
      else
      {
         digitalWrite(LED, LOW);
      }
   }
   else
   {
      digitalWrite(LED, LOW);
   }
}

void Mindwave::Onesec_Rawval_Fun()
{

   Avg_Raw = Temp / 512;

   Serial.println(Avg_Raw);
   if (On_Flag == 0 && Off_Flag == 1)
   {
      if (n < 3)
      {
         Temp_Avg += Avg_Raw;
         n++;
      }
      else
      {
         Temp_Avg = Temp_Avg / 3;
         if (Temp_Avg < EEG_AVG)
         {
            On_Flag = 1;
            Off_Flag = 0;
         }
         n = 0;
         Temp_Avg = 0;
      }
   }
   j = 0;
   Temp = 0;
   Eye_Blink();
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

void Mindwave::Big_Packet()
{
   generatedchecksum = 0;
   for (int i = 0; i < Plength; i++)
   {
      payloadDataB[i] = ReadOneByte(); //Read payload into memory
      generatedchecksum += payloadDataB[i];
   }
   generatedchecksum = 255 - generatedchecksum;
   checksum = ReadOneByte();
   if (checksum == generatedchecksum) // Varify Checksum
   {
      Poorquality = payloadDataB[1];
      Serial.println("La calidad de señal es: " + Poorquality);
      if (Poorquality == 0)
      {
         Eye_Enable = 1;
      }
      else
      {
         Eye_Enable = 0;
      }
   }
}

void Mindwave::Calibrar_Sensor()
{ 
  Serial.println("Calibrando");
  Serial.println("Calibrando");
  Serial.println("Calibrando");
  Serial.println("Calibrando");
  while (Calibracion_raw <= 100 ){
    if (ReadOneByte() == 170) // AA 1 st Sync data
    {
      if (ReadOneByte() == 170) // AA 2 st Sync data
      {
        Plength = ReadOneByte();
        if (Plength == 4) // Small Packet
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
              Avg_Raw = Temp / 512;

              Calibracion_raw = Avg_Raw;
              Serial.println("La calibracion_rAW es: " + Calibracion_raw);

              Umbral_de_parpadeo = Calibracion_raw * 2;
            }
          }
        }
        else if (Plength == 32) // Big Packet
        {
          generatedchecksum = 0;
          for (int i = 0; i < Plength; i++)
          {
            payloadDataB[i] = ReadOneByte(); //Read payload into memory
            generatedchecksum += payloadDataB[i];
          }
          generatedchecksum = 255 - generatedchecksum;
          checksum = ReadOneByte();
          if (checksum == generatedchecksum) // Varify Checksum
          {
            Poorquality = payloadDataB[1];
            Serial.println("La calidad de señal es: " + Poorquality);
            if (Poorquality == 0)
            {
              Eye_Enable = 1;
            }
            else
            {
              Eye_Enable = 0;
            }
          }
        }
      }
    }
  }
  
}

void Mindwave::Esperar_al_mindwave()
{
  bool info_no_entro = true;
  while (info_no_entro == true)
  {
    Serial.println(Serial.available());
    // if (Serial.available() > 0)
    // {
    //   if (ReadOneByte() == 170) // AA 1 st Sync data
    //   {
    //     if (ReadOneByte() == 170) // AA 2 st Sync data
    //     {
    //       Plength = ReadOneByte();
    //       if (Plength == 4) // Small Packet
    //       {
    //         Serial.println("La informacion esta lista para usar");
    //         info_no_entro = false;
    //       }
    //       else if (Plength == 32) // Big Packet
    //       {
    //         Serial.println("Entro info pero no esta usable");
    //       }
    //     }
    //   }
    // }
    // else
    // {
      if (Serial.available() == 0){
      Serial.println("No esta entrando info");
      Serial.println("volver a intentar");
      delay(1000);
      }
      else
      {
        Serial.println("Empezo a entrar informacion");
        Serial.println("En breve empieza la calibracion");
        delay(2500); // este delay esta puesto para darle al mindwave un tiempo a estabilizarse
        info_no_entro = false;
      }
      
      // delay(500);
      // Serial.println("intento numero: " + intento);

      // intento++;
    
  }
}
