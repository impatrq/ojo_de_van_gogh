#ifndef Mindwave_h
#define Mindwave_h

#include "Arduino.h"

class Mindwave
{
    public:
        Mindwave(char LED, char Thesold_Eyeblink, char EEG_AVG);
        byte ReadOneByte();
        void Small_Packet();
        void Big_Packet();
        void Onesec_Rawval_Fun();
        void Eye_Blink();
        long Calibrar_Sensor();
        void Esperar_al_mindwave();

    private:
        char LED;
        char Thesold_Eyeblink;
        char EEG_AVG;
        long payloadDataS[5];
        long payloadDataB[32];
        byte checksum;
        byte generatedchecksum;
        unsigned int Raw_data, 
        unsigned int Poorquality, 
        unsigned int Plength, 
        unsigned int Eye_Enable = 0,
        unsigned int On_Flag = 0, 
        unsigned int Off_Flag = 1;
        unsigned int j, n;
        long Temp, Avg_Raw, Temp_Avg;
        long Calibracion_raw;
        long Umbral_de_parpadeo;
        int intento;
}