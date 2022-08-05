#!/usr/bin/env python3
import serial
import time
from picamera import PiCamera
import os

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

# Init Camera
print("Init camera.")
camera = PiCamera()
camera.resolution = (640, 480)
camera.rotation = 180
image_folder_name = "/home/pi/camera"
if not os.path.exists(image_folder_name):
    os.mkdir(image_folder_name)
image_file_name = image_folder_name + "/door_camera.jpg"
print("Camera OK.")

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
                print("Open door request. Taking a photo.")
                send_to_arduino("print_text:Please wait for a few seconds.")
                camera.capture(image_file_name)
            else:
                ser.reset_input_buffer()
except KeyboardInterrupt:
    print("---")
    print("Closing Serial communication.")
    ser.close()
    print("End of program.")
    
    








