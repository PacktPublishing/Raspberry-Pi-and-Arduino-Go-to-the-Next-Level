#!/usr/bin/env python3
import serial
import time

# Init Serial
print("Trying to connect to Serial.")
while True:
    try:
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
        print("Successfully connected to Serial.")
        break
    except serial.SerialException:
        print("Could not connect to Serial. Retrying in 1 second...")
        time.sleep(1)

def send_to_arduino(text):
    str_to_send = text.rstrip() + "\n"
    ser.write(str_to_send.encode('utf-8'))

# Wait after setup
print("Waiting for 3 seconds...")
time.sleep(3)
ser.reset_input_buffer()
send_to_arduino("print_text:Push on button to call.")
send_to_arduino("set_led:000,000,255")
print("OK. Main loop is starting.")
    
# Run main loop
try:
    while True:
        time.sleep(0.01)
        if ser.in_waiting > 0:
            msg = ser.readline().decode('utf-8').rstrip()
            if msg == "button_pressed":
                print("Open door request.")
                send_to_arduino("print_text:Please wait for a few seconds.")
            else:
                ser.reset_input_buffer()
except KeyboardInterrupt:
    print("---")
    print("Closing Serial communication.")
    ser.close()
    print("End of program.")
    
    







