#include <Servo.h>

#define BUTTON_PIN 7
#define SERVO_PIN 12

unsigned long lastTimeButtonChanged = millis();
unsigned long debounceDelay = 50;
byte previousButtonState;

Servo servo;

void setup() {
  pinMode(BUTTON_PIN, INPUT);
  previousButtonState = digitalRead(BUTTON_PIN);

  servo.attach(SERVO_PIN);

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

  if (Serial.available() > 0) {
    String cmd = Serial.readStringUntil('\n');
    if (cmd.startsWith("servo:")) {
      cmd.remove(0, 6);
      int angle = cmd.toInt();
      servo.write(angle);
    }
  }
}
