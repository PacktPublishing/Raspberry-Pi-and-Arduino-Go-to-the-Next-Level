#include <LiquidCrystal.h>
#include <Servo.h>

#define SERVO_PIN 12
#define RGB_RED_PIN 11
#define RGB_GREEN_PIN 10
#define RGB_BLUE_PIN 9
#define BUZZER_PIN 8
#define BUTTON_PIN 7
#define LCD_RS_PIN A4
#define LCD_E_PIN A5
#define LCD_D4_PIN 2
#define LCD_D5_PIN 3
#define LCD_D6_PIN 4
#define LCD_D7_PIN 5

#define SERVO_OPEN_DOOR_POSITION 50
#define SERVO_CLOSE_DOOR_POSITION 140

LiquidCrystal lcd(LCD_RS_PIN, LCD_E_PIN, LCD_D4_PIN,
                            LCD_D5_PIN, LCD_D6_PIN, LCD_D7_PIN);
Servo servo;

unsigned long lastTimeButtonChanged = millis();
unsigned long debounceDelay = 50;
byte previousButtonState;

void setup() {
  Serial.begin(115200);
  while (!Serial) {}
  while (Serial.available() > 0) {
    Serial.read();
  }
  
  servo.attach(SERVO_PIN);
  servo.write(SERVO_CLOSE_DOOR_POSITION);

  pinMode(BUTTON_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(RGB_RED_PIN, OUTPUT);
  pinMode(RGB_GREEN_PIN, OUTPUT);
  pinMode(RGB_BLUE_PIN, OUTPUT);

  previousButtonState = digitalRead(BUTTON_PIN);

  lcd.begin(16,2);
  lcd.print("Starting...");
  delay(1000);
  lcd.clear();
}

void loop() {
  unsigned long timeNow = millis();
  if (timeNow - lastTimeButtonChanged >= debounceDelay) {
    byte buttonState = digitalRead(BUTTON_PIN);
    if (buttonState != previousButtonState) {
      lastTimeButtonChanged = timeNow;
      previousButtonState = buttonState;
      if (buttonState == HIGH) {
        Serial.println("button_pressed");
      }
    }
  }
}
