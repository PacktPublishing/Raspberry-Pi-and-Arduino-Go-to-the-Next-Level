#define LED_PIN 13

unsigned long lastTimeTemperatureSent = millis();
unsigned long temperatureSendDelay = 1000;

void setup() {
  Serial.begin(115200);
  while (!Serial) {}
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  unsigned long timeNow = millis();
  if (timeNow - lastTimeTemperatureSent >= temperatureSendDelay) {
    lastTimeTemperatureSent = timeNow;
    int temperature = random(5, 25);
    Serial.println(temperature);
  }

  if (Serial.available() > 0) {
    String cmd = Serial.readStringUntil('\n');
    if (cmd == "on") {
      digitalWrite(LED_PIN, HIGH);
    }
    else if (cmd == "off") {
      digitalWrite(LED_PIN, LOW);
    }
    else {
      
    }
  }
}
