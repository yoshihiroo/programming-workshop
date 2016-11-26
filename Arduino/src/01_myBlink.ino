void setup() {
  pinMode(9, OUTPUT);
}

void loop() {
  myBlink();
}

void myBlink() {
  digitalWrite(9, HIGH);
  delay(1000);           // 1,000 millisecond
  digitalWrite(9, LOW);
  delay(1000);
}
