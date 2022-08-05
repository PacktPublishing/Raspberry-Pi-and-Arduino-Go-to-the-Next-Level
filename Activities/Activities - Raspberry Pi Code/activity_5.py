#!/usr/bin/env python3
import serial
import time
import random

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print("Serial OK.")

try:
    while True:
        time.sleep(0.01)
        if ser.in_waiting > 0:
            msg = ser.readline().decode('utf-8').rstrip()
            if msg == "button_pressed":
                print("Button has been pressed")
                led = random.randint(0, 2)
                number = random.randint(0, 255)
                cmd = ""
                if led == 1:
                    cmd += "red:"
                elif led == 2:
                    cmd += "green:"
                else:
                    cmd += "blue:"
                cmd += str(number)
                cmd += "\n"
                print("Send command: " + cmd)
                ser.write(cmd.encode('utf-8'))
except KeyboardInterrupt:
    print("Close serial communication.")
    ser.close()


