#define LED_PIN 13

void setup() {
  Serial.begin(115200);
  while (!Serial) {}
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String cmd = Serial.readStringUntil('\n');
    if (cmd == "on") {
      digitalWrite(LED_PIN, HIGH);
    }
    else if (cmd == "off") {
      digitalWrite(LED_PIN, LOW);
    }
    else {
      // nothing
    }
  }
}
