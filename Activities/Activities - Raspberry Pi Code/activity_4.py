#!/usr/bin/env python3
import serial
import time

last_time_reset_counter = time.time()
reset_counter_delay = 10.0

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print("Serial OK.")

try:
    while True:
        time.sleep(0.01)
        # action 1
        time_now = time.time()
        if time_now - last_time_reset_counter >= reset_counter_delay:
            last_time_reset_counter = time_now
            print("Send reset counter command")
            ser.write("reset_counter\n".encode('utf-8'))
        # action 2
        if ser.in_waiting > 0:
            counter = int(ser.readline().decode('utf-8').rstrip())
            print("Received counter: " + str(counter))
except KeyboardInterrupt:
    print("Close serial communication.")
    ser.close()

