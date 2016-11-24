void setup() {
}

void loop() {
  analogWrite(9, 255);  // 0~255
  delay(1000);          // 1,000 millisecond

  analogWrite(9, 150);
  delay(1000);

  analogWrite(9, 50);
  delay(1000);

  analogWrite(9, 20);
  delay(1000);
}
