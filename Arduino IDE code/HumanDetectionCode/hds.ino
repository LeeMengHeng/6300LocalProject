volatile boolean people;
void setup() {
  // put your setup code here, to run once:
  people = 0;
  pinMode(2, INPUT);
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  people = digitalRead(2);
  if(people == 1) {
    digitalWrite(13, HIGH);
    delay(1000);
  } else {
    digitalWrite(13, LOW);
  }
  Serial.println(people);
}
