#include "WiFi.h"
#include "SPI.h"
// #include "WiFiUdp.h"
// #include "NTPClient.h"
 
const char* ssid = "RICHARazer"; //choose wireless ssid
const char* password =  "1234567890"; //put wireless password here.
const char* host = "192.168.137.181";
const int port = 8000;
volatile boolean people1;
volatile boolean people2;
// WiFiUDP ntpUDP;
// NTPClient timeClient(ntpUDP, "europe.pool.ntp.org", 3600, 60000);



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
  //timeClient.begin();
  Serial.println("Connected to the WiFi network");
  // Print local IP address and start web server
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  people1 = 0;
  people2 = 0;
  
}

boolean temp1 = 0;
  boolean temp2 = 0;

void loop() {
  //timeClient.update();
  //Client.println(timeClient.getFormattedTime());
  //delay(500);
  Serial.println(host);
    /* Use WiFiClient class to create TCP connections */
  Serial.begin(9600);
  WiFiClient client;
  if (!client.connect(host, port)) {
      Serial.println("connection failed");
      return;
  }
  // put your main code here, to run repeatedly:
  people1 = digitalRead(2);
  people2 = digitalRead(14);
  String msg1 = "Door_1:" + String(people1);
  String msg2 = "Door_2:" + String(people2);
  Serial.println(msg1);
  Serial.println(msg2);
  Serial.println("----------------------------");
  
  if(people1 == 1 && temp1 == 0) {
    temp1 = 1;
    client.println(msg1);
    //client.println(timeClient.getFormattedTime());
  } 
  else if (people1 == 0 && temp1 == 1) {
    temp1 = 0;
    client.println("Door_1:" + String(0));
    //client.println(timeClient.getFormattedTime());
  }
  if(people2 == 1 && temp2 == 0) {
    temp2 = 1;
    client.println(msg2);
    //client.println(timeClient.getFormattedTime());
  }
  else if (people2 == 0 && temp2 == 1) {
    temp2 = 0;
    client.println("Door_2:" + String(0));
    //client.println(timeClient.getFormattedTime());
  }

Serial.println("temp = " + String(temp1));
  
  //delay(500);
}
