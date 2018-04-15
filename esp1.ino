 
#include <ESP8266WiFi.h>
//int ledPin = 2; // GPIO2 of ESP8266
int ledPin = D4; // D4 of Wemos D1
 

void setup() {
    Serial.begin (9600);  //(115200);
    Serial.println ("8266 starting...");
    delay(10); 
    pinMode(ledPin, OUTPUT);
    for (int i=0; i<8; i++) {
      digitalWrite(ledPin, HIGH);
      delay(100); 
      digitalWrite(ledPin, LOW);
      delay(100); 
    }
}

void loop() {
    Serial.println ("8266 is alive.");
    delay (2000);
}

