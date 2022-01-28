#include <SPI.h>
#include <LoRa.h>

#define LED 6

int code;
int valPWM = 150;
int ack;
bool state       = false;
bool controlFlag = false;

void ledHandler();
void pwmHandler();

void setup() {

  Serial.begin(9600);
  while (!Serial);

  Serial.println("LoRa Receiver");

  if (!LoRa.begin(433E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }

  pinMode(LED, OUTPUT);
}

void loop() {
  // try to parse packet
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    // received a packet
    Serial.print("Received packet '");

    // read packet
    while (LoRa.available()) {
      code = (LoRa.read());
      Serial.print(code);
    }

    if(code == 55){
      ledHandler();
    } else if (code == 56 || code == 57){
      pwmHandler();
    }

    // print RSSI of packet
    Serial.print("' with RSSI ");
    Serial.println(LoRa.packetRssi());
  }
}

void ledHandler(){
  if (controlFlag){
    valPWM = 0;
    analogWrite(LED, valPWM);
    controlFlag = false;
  } else {
    valPWM = 170;
    analogWrite(LED, valPWM);
    controlFlag = true;
  }
}

void pwmHandler(){
  controlFlag = true;
  if (code == 56){
    if (valPWM <= 225){
      valPWM += 30;   
    } else {
      //send error
    }
  } else if (code == 57){
    if (valPWM >= 30){
      valPWM -=30;
    }else{
      //send error
    }
  }
  analogWrite(LED, valPWM);
}
