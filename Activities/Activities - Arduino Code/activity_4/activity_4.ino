#include <LiquidCrystal.h>

#define LCD_RS_PIN A4
#define LCD_E_PIN A5
#define LCD_D4_PIN 2
#define LCD_D5_PIN 3
#define LCD_D6_PIN 4
#define LCD_D7_PIN 5

LiquidCrystal lcd(LCD_RS_PIN, LCD_E_PIN, LCD_D4_PIN,
                             LCD_D5_PIN, LCD_D6_PIN, LCD_D7_PIN);

int counter = 0;

unsigned long lastTimeCounterSent = millis();
unsigned long sendCounterDelay = 500;

void setup() {
  lcd.begin(16, 2);
  Serial.begin(115200);
  while (!Serial) {}
}

void loop() {
  unsigned long timeNow = millis();
  if (timeNow - lastTimeCounterSent >= sendCounterDelay) {
    lastTimeCounterSent = timeNow;
    Serial.println(counter);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Sent counter: ");
    lcd.setCursor(0, 1);
    lcd.print(counter);
    counter++;
  }

  if (Serial.available() > 0) {
    String cmd = Serial.readStringUntil('\n');
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print(cmd);
    if (cmd == "reset_counter") {
      counter = 0;
    }
    else {
      
    }
  }
}
