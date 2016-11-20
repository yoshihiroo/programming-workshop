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
    myFade(20);
  }
  delay(100);
}

void myBlink(int t) {
  digitalWrite(9, HIGH);
  delay(t);
  digitalWrite(9, LOW);
  delay(t);
}

void myFade(int t) {
  for (int i = 0; i <= 255; i=i+5) {
    analogWrite(9, i);
    delay(t);
  }
  for (int i = 255; i >= 0; i=i-5) {
    analogWrite(9, i);
    delay(t);
  }  
}
