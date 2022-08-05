#define BUTTON_PIN 7

unsigned long lastTimeButtonChanged = millis();
unsigned long debounceDelay = 50;
byte previousButtonState;

void setup() {
  pinMode(BUTTON_PIN, INPUT);
  previousButtonState = digitalRead(BUTTON_PIN);

  Serial.begin(115200);
  while (!Serial) {}
}

void loop() {
  unsigned long timeNow = millis();
  if (timeNow - lastTimeButtonChanged >= debounceDelay) {
    byte buttonState = digitalRead(BUTTON_PIN);
    if (buttonState != previousButtonState) {
      lastTimeButtonChanged = timeNow;
      previousButtonState = buttonState;
      if (buttonState == HIGH) { // button is pressed
        Serial.println("button_pressed");
      }
    }
  }
}
