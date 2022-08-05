#define BUTTON_PIN 7
#define RGB_RED_PIN 11
#define RGB_GREEN_PIN 10
#define RGB_BLUE_PIN 9

unsigned long lastTimeButtonChanged = millis();
unsigned long debounceDelay = 50;
byte previousButtonState;

void setup() {
  pinMode(BUTTON_PIN, INPUT);
  pinMode(RGB_RED_PIN, OUTPUT);
  pinMode(RGB_GREEN_PIN, OUTPUT);
  pinMode(RGB_BLUE_PIN, OUTPUT);

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

  if (Serial.available() > 0) {
    String cmd = Serial.readStringUntil('\n');
    if (cmd.startsWith("red:")) {
      cmd.remove(0, 4);
      int red = cmd.toInt();
      analogWrite(RGB_RED_PIN, red);
    }
    else if (cmd.startsWith("green:")) {
      cmd.remove(0, 6);
      int green = cmd.toInt();
      analogWrite(RGB_GREEN_PIN, green);
    }
    else if (cmd.startsWith("blue:")) {
      cmd.remove(0, 5);
      int blue = cmd.toInt();
      analogWrite(RGB_BLUE_PIN, blue);
    }
    else {
      // nothing
    }
  }  
}
