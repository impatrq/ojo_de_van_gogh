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











