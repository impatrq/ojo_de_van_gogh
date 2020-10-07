const int buzzer=9;
const int tonos[]={50,500,1000,2500,5000,10000,15000};

void setup() {
 
}

void loop() {
  for(int iTono=0; iTono<7; iTono++){
    tone(buzzer,tonos[iTono]);
    delay(1000);
  }
  noTone(buzzer);
  delay(1000);
}
