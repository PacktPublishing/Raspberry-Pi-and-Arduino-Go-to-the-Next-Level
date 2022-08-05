#!/usr/bin/env python3
from picamera import PiCamera
import os
import time
import serial
from telegram.ext import Updater, CommandHandler
from telegram import Bot

last_time_photo_taken = time.time()
photo_delay = 2.0

while True:
    try:
        ser = serial.Serial('/dev/ttyACM1', 115200, timeout=1.0)
        print("Successfully connected to Serial. Wait 3 seconds...")
        break
    except serial.SerialException:
        print("Could not connect to Serial, retrying in 1 second...")
        time.sleep(1)

camera = PiCamera()
camera.resolution = (640, 480)
camera.rotation = 180
image_folder_name = "/home/pi/camera"
if not os.path.exists(image_folder_name):
    os.mkdir(image_folder_name)
image_file_name = image_folder_name + "/photo.jpg"

time.sleep(3)
ser.reset_input_buffer()
print("Camera OK")
print("Serial OK.")

def start_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Welcome!")
    
def get_photo_handler(update, context):
    with open(image_file_name, 'rb') as photo:
        print("Sending photo to telegram")
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=photo)

with open('/home/pi/.local/share/.telegram_bot_token', 'r') as f:
    telegram_token = f.read().rstrip()
bot = Bot(token=telegram_token)
chat_id = "-623214910"
updater = Updater(token=telegram_token)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(CommandHandler('get_photo', get_photo_handler))
updater.start_polling()

try:
    while True:
        time.sleep(0.01)
        # take photo
        time_now = time.time()
        if time_now - last_time_photo_taken >= photo_delay:
            last_time_photo_taken = time_now
            camera.capture(image_file_name)
        # read from serial
        if ser.in_waiting > 0:
            msg = ser.readline().decode('utf-8').rstrip()
            if msg == "button_pressed":
                with open(image_file_name, 'rb') as photo:
                    print("Sending photo to telegram")
                    bot.send_photo(chat_id=chat_id, photo=photo)
except KeyboardInterrupt:
    print("Closing Serial")
    ser.close()
    print("Stopping Telegram updater...")
    updater.stop()