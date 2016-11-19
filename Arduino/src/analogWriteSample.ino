void setup() {
}

void loop() {
  analogWrite(9, 255);  //0~255
  delay(1000);

  analogWrite(9, 150);  //0~255
  delay(1000);

  analogWrite(9, 50);  //0~255
  delay(1000);

  analogWrite(9, 20);  //0~255
  delay(1000);

}
