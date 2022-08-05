#!/usr/bin/env python3
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print("Serial OK.")

try:
    while True:
        user_input = input("Select 'on' or 'off': ")
        if user_input in ['on', 'off']:
            print("Send command to Arduino: " + user_input)
            str_to_send = user_input + "\n"
            ser.write(str_to_send.encode('utf-8'))
except KeyboardInterrupt:
    print("Close serial communication.")
    ser.close()
    