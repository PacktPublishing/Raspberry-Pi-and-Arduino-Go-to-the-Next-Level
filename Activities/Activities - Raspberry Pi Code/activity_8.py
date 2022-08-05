#!/usr/bin/env python3
import serial
import time
from telegram.ext import Updater, CommandHandler

while True:
    try:
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
        print("Successfully connected to Serial. Wait 3 seconds...")
        break
    except serial.SerialException:
        print("Could not connect to Serial, retrying in 1 second...")
        time.sleep(1)

time.sleep(3)
ser.reset_input_buffer()
print("Serial OK.")

def start_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Welcome!")
    
    # /lcd command
def lcd_handler(update, context):
    text = update.message.text[5:]
    cmd = "print_text:" + text + "\n"
    ser.write(cmd.encode('utf-8'))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="OK")
    
    # /rgb command
def rgb_handler(update, context):
    text = update.message.text[5:]
    cmd = "set_led:" + text + "\n"
    ser.write(cmd.encode('utf-8'))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="OK")

with open('/home/pi/.local/share/.telegram_bot_token', 'r') as f:
    telegram_token = f.read().rstrip()
updater = Updater(token=telegram_token)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start_handler))
dispatcher.add_handler(CommandHandler('lcd', lcd_handler))
dispatcher.add_handler(CommandHandler('rgb', rgb_handler))
updater.start_polling()

try:
    while True:
        time.sleep(0.01)
except KeyboardInterrupt:
    print("Closing Serial.")
    ser.close()
    print("Stopping telegram updater.")
    updater.stop()
