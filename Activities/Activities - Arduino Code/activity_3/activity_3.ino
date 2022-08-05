// init counter, send it every 500ms, increment it
// when receive reset_counter cmd, reset counter

int counter = 0;

unsigned long lastTimeCounterSent = millis();
unsigned long sendCounterDelay = 500;

void setup() {
  Serial.begin(115200);
  while (!Serial) {}
}

void loop() {
  unsigned long timeNow = millis();
  if (timeNow - lastTimeCounterSent >= sendCounterDelay) {
    lastTimeCounterSent = timeNow;
    Serial.println(counter);
    counter++;
  }

  if (Serial.available() > 0) {
    String cmd = Serial.readStringUntil('\n');
    if (cmd == "reset_counter") {
      counter = 0;
    }
    else {
      
    }
  }
}
