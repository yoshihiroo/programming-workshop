void setup() {
  pinMode(7, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(7) == LOW) { // is Obstacle
    Serial.println("OBSTACLE!!, OBSTACLE!!");
  }
  else { // no Obstacle
    Serial.println("clear");
  }  
  delay(200);
}
