void setup() {
  pinMode(9, OUTPUT);
}

void loop() {
  myBlink();
  myFade();
}

void myBlink() {
  digitalWrite(9, HIGH);
  delay(500);
  digitalWrite(9, LOW);
  delay(500);
}

void myFade() {
  int i = 0;
  while (i < 256) {
    analogWrite(9, i);
    i = i + 5;
    delay(10);
  }
  i = 255;
  while (i > 0) {
    analogWrite(9, i);
    i = i - 5;
    delay(10);
  }
}
