void loop() {
  myBlink();
  myFade();
}

// ----- Functions -----

void myBlink() {
  digitalWrite(9, HIGH);
  delay(500);
  digitalWrite(9, LOW);
  delay(500);
}

void myFade() {
  for (int i = 0; i <= 255; i=i+5) {
    analogWrite(9, i);
    delay(10);
  }
  for (int i = 255; i >= 0; i=i-5) {
    analogWrite(9, i);
    delay(10);
  }  
}
