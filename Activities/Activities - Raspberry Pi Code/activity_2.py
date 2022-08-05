#!/usr/bin/env python3
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print("Serial OK.")

try:
    while True:
        if ser.in_waiting > 0:
            temperature = int(ser.readline().decode('utf-8').rstrip())
            if temperature < 15:
                print("Temperature lower than 15, LED on")
                ser.write("on\n".encode('utf-8'))
            else:
                print("Temperature greater than 15, LED off")
                ser.write("off\n".encode('utf-8'))
except KeyboardInterrupt:
    print("Close serial communication.")
    ser.close()