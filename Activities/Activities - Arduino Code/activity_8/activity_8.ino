#include <LiquidCrystal.h>

#define RGB_RED_PIN 11
#define RGB_GREEN_PIN 10
#define RGB_BLUE_PIN 9
#define LCD_RS_PIN A4
#define LCD_E_PIN A5
#define LCD_D4_PIN 2
#define LCD_D5_PIN 3
#define LCD_D6_PIN 4
#define LCD_D7_PIN 5

LiquidCrystal lcd(LCD_RS_PIN, LCD_E_PIN, LCD_D4_PIN,
                            LCD_D5_PIN, LCD_D6_PIN, LCD_D7_PIN);

void setup() {
  Serial.begin(115200);
  while (!Serial) {}

  lcd.begin(16, 2);
  pinMode(RGB_RED_PIN, OUTPUT);
  pinMode(RGB_GREEN_PIN, OUTPUT);
  pinMode(RGB_BLUE_PIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String cmd = Serial.readStringUntil('\n');
    if (cmd.startsWith("print_text:")) {
      cmd.remove(0,11);
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print(cmd);
    }
    else if (cmd.startsWith("set_led:")) {
      cmd.remove(0,8);
      int red = cmd.substring(0,3).toInt();
      int green = cmd.substring(4,7).toInt();
      int blue = cmd.substring(8).toInt();
      analogWrite(RGB_RED_PIN, red);
      analogWrite(RGB_GREEN_PIN, green);
      analogWrite(RGB_BLUE_PIN, blue);
    }
    else {
      // nothing
    }
  }
}
