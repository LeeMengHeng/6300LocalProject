//void setup() {
//  // put your setup code here, to run once:
//  Serial.begin(9600);
//}
#include "WiFi.h"
#include "SPI.h"
 
const char* ssid = "RICHALEGION"; //choose wireless ssid
const char* password =  "1234567890"; //put wireless password here.
const char* host = "192.168.137.46";
const int port = 8000;
 
void setup() {
  SPI.begin();
  Serial.begin(9600);
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
  // Print local IP address and start web server
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP()); //show ip address when connected on serial monitor.
  Serial.begin(9600);
}
 
void loop() {
  // put your main code here, to run repeatedly
  delay(1000);
  Serial.println(host);
    /* Use WiFiClient class to create TCP connections */
    WiFiClient client;
    if (!client.connect(host, port)) {
        Serial.println("connection failed");
        return;
    }
    String msg ="Pressure:"+String(analogRead(36));
    Serial.println(msg);
    client.println(msg);
//  String msg1 = "Sensor1:" + String(analogRead(36));
//  String msg2 = "Sensor2:" + String(analogRead(35));
//  Serial.println(WiFi.RSSI());
//  Serial.println(msg1);
//  Serial.println(msg2);
  delay(1000);
}
