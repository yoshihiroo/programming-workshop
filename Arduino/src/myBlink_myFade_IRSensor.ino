void setup() {
  pinMode(9, OUTPUT);
  pinMode(7, INPUT);
}

void loop() {
  if (digitalRead(7) == LOW) // is Obstacle
  {
    myBlink(300);
  }
  else // no Obstacle
  {
    myUpFade(4);
    myDownFade(4);
  }
  delay(200);
}

void myBlink(int t) {
  digitalWrite(9, HIGH);
  delay(t);
  digitalWrite(9, LOW);
  delay(t);
}

void myUpFade(int s) {
  int i=0;
  while (i < 256) {
    analogWrite(9, i);
    i = i + s;
    delay(10);
  }
}

void myDownFade(int s) {
  int i=255;
  while (i > 0) {
    analogWrite(9, i);
    i = i - s;
    delay(10);
  }
}
