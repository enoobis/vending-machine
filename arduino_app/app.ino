int LED_PIN = 13;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("Arduino is ready!");
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    if (command == "turn_on_led") 
    {
      digitalWrite(LED_PIN, HIGH); 
      delay(5000);
      digitalWrite(LED_PIN, LOW); 
    }
    else if (command == "turn_off_led") 
    {
      digitalWrite(LED_PIN, LOW); 
    }
  }
}
