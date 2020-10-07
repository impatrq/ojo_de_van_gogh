import array
import serial
import time

#    Program       : Mindwave with Arduino                
#    Interfacing   : HC-05 Bluetooth Module               
#    Output        : Eye Blink Control LED                
					
					#define   LED        5

Theshold_EyeBlink = int(110)
EEG_AVG = int(70)
payloadDataS = array.array('l', range(5))
payloadDataB = array.array('l', range(32))
checksum= int(0)
generatedchecksum= int(0)
Raw_data = int(0)
Poorquality = int(0)
Plength = int(0)
Eye_Enable= int(0)
On_Flag= int(0)
Off_Flag= int(1)
j = int(0)
n= int(0)
Temp = 0
Avg_Raw = 0
Temp_Avg = 0

ser = serial.Serial('COM3', 57600) # lo de las comillas simples tenes que poner el com que uses
time.sleep(2)
def Read_One_Byte():           # One Byte Read Function
   ByteRead = int(0)
   while ser.available() == 0:
       ByteRead = 0
   ByteRead = ser.read()
   return ByteRead

def Eye_Blink ():
 
   if (Eye_Enable):         
   
     if (On_Flag == 1 and Off_Flag == 0):
     
       if ((Avg_Raw>Theshold_Eyeblink) and (Avg_Raw<350)):
       
         ser.write ('b', 1)
         ser.close ()
         
       
       else:
       
         if (Avg_Raw>350):
         
           On_Flag == 0
           Off_Flag == 1
         
         ser.write ('b', 0)
         ser.close ()
         
     else:
   
       ser.write ('b', 0)
       ser.close ()
            
   else:

     ser.write ('b', 0)
     ser.close ()

def Onesec_Rawval_Fun ():
   Avg_Raw = Temp/512
   if (On_Flag == 0 and Off_Flag == 1):
   
     if (n<3):
     
       Temp_Avg += Avg_Raw
       n= n+1
     
     else:
     
       Temp_Avg = Temp_Avg/3
       if (Temp_Avg<EEG_AVG):
       
         On_Flag = 1
         Off_Flag = 0
       
       n=0
       Temp_Avg=0
      
                
   Eye_Blink ()
   j=0
   Temp=0

def Small_Packet ():
   generatedchecksum = (0)
   i = int(0)
   for i in range(i<Plength):
   
     payloadDataS[i] = ReadOneByte()           #Read payload into memory
     generatedchecksum += payloadDataS[i] 
   
   generatedchecksum = 255 - generatedchecksum
   checksum  = ReadOneByte()
   if (checksum == generatedchecksum):          # Varify Checksum
    
     if (j<512):
     
       Raw_data  = ((payloadDataS[2] << 8)| payloadDataS[3])
       if (Raw_data&0xF000):
       
         Raw_data = (((~Raw_data)&0xFFF)+1)
       
       else:
       
         Raw_data = (Raw_data&0xFFF)
       
       Temp += Raw_data
       j = j+1
     
     else:
     
       Onesec_Rawval_Fun () 

def Big_Packet():
 
   generatedchecksum = 0
   for i in range (i<Plength):
   
     payloadDataB[i] = ReadOneByte()           # Read payload into memory
     generatedchecksum += payloadDataB[i] 
   
   generatedchecksum = 255 - generatedchecksum
   checksum = ReadOneByte()
   if (checksum == generatedchecksum):         # Varify Checksum
   
     Poorquality = payloadDataB[1]
     
     if (Poorquality==0 ):
     
       Eye_Enable = 1
     
     else:
     
       Eye_Enable = 0
    
                    # Main Function

   if(ReadOneByte() == 170):        # AA 1 st Sync data
   
     if(ReadOneByte() == 170):      # AA 2 st Sync data
     
       Plength = ReadOneByte()
       if(Plength == 4):   				 # Small Packet
       
         Small_Packet ()
         
       
       elif(Plength == 32):   			 # Big Packet
       
         Big_Packet ()