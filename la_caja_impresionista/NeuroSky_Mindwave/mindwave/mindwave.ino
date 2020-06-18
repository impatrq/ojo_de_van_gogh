//                                                         //
//    Program       : Mindwave with Arduino                //
//    Interfacing   : HC-05 Bluetooth Module               //
//    Output        : Eye Blink Control LED                //

#define BAUDRATE 57600
#define LED 5
#define Theshold_Eyeblink 110
#define EEG_AVG 70

long payloadDataS[5] = {0};
long payloadDataB[32] = {0};
byte checksum = 0, generatedchecksum = 0;
unsigned int Raw_data, Poorquality, Plength, Eye_Enable = 0, On_Flag = 0, Off_Flag = 1;
unsigned int j, n = 0;
long Temp, Avg_Raw, Temp_Avg;
long Calibracion_raw;
long Umbral_de_parpadeo;
int intento = 0;

void setup()
{
  Serial.begin(BAUDRATE); // USB
  pinMode(LED, OUTPUT);
  for (int h = 0; h < 10; h++)
  {
    Serial.println("Empezo el void setup");
  }
  Esperar_al_mindwave();


  Serial.println("Empezo a calibrar");

  Umbral_de_parpadeo = Calibrar_sensor() ;
  Umbral_de_parpadeo = Umbral_de_parpadeo * 2;
  

}

void loop() // Main Function
{

  Serial.println("El umbral de pestañeo es:");
  Serial.println(Umbral_de_parpadeo);

  if (ReadOneByte() == 170) // AA 1 st Sync data
  {
    if (ReadOneByte() == 170) // AA 2 st Sync data
    {
      Plength = ReadOneByte();
      if (Plength == 4) // Small Packet
      {
        Small_Packet();
      }
      else if (Plength == 32) // Big Packet
      {
        Big_Packet();
        Serial.println("BigPacket");
      }
    }
  }
}

byte ReadOneByte() // One Byte Read Function
{
  int ByteRead;
  while (!Serial.available());
  ByteRead = Serial.read();
  return ByteRead;
}
void Small_Packet()
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

void Big_Packet()
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

void Onesec_Rawval_Fun()
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
  Eye_Blink();
  j = 0;
  Temp = 0;
}

void Eye_Blink()
{
  if (Eye_Enable)
  {
    if (On_Flag == 1 && Off_Flag == 0)
    {
      if ((Avg_Raw > Theshold_Eyeblink) && (Avg_Raw < 350))
      {
        digitalWrite(LED, HIGH);
        Serial.println("1");
      }
      else
      {
        if (Avg_Raw > 350)
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

long Calibrar_sensor()
{ 
  Serial.println("Calibrando");
  Serial.println("Calibrando");
  Serial.println("Calibrando");
  Serial.println("Calibrando");
  while (Calibracion_raw < 100 ){
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

              return Calibracion_raw;
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

void Esperar_al_mindwave()
{
  bool info_no_entro = true;
  while (info_no_entro == true)
  {
    Serial.println(Serial.available());
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
