#!/usr/bin/env python3
import serial
import time
from telegram import Bot

while True:
    try:
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
        print("Successfully connected to Serial. Wait 3 seconds...")
        break
    except serial.SerialException:
        print("Could not connect to Serial, retrying in 1 second...")
        time.sleep(1)

with open('/home/pi/.local/share/.telegram_bot_token', 'r') as f:
    telegram_token = f.read().rstrip()
bot = Bot(token=telegram_token)
chat_id = "-623214910"

time.sleep(3)
ser.reset_input_buffer()
print("Serial OK.")
bot.send_message(chat_id=chat_id,
                 text="Connected to Arduino with Serial")

try:
    while True:
        time.sleep(0.01)
except KeyboardInterrupt:
    print("Closing Serial.")
    ser.close()
    bot.send_message(chat_id=chat_id,
                     text="Disconnected from Arduino")
