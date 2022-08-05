#!/usr/bin/env python3
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print("Serial OK.")

last_time_servo_move = time.time()
servo_delays = [0.005, 0.01, 0.015, 0.02]
servo_delay_index = 0
servo_delay = servo_delays[servo_delay_index]

servo_angle = 90
servo_going_up = True

try:
    while True:
        time.sleep(0.001)
        time_now = time.time()
        
        # Sweep servo
        if time_now - last_time_servo_move >= servo_delay:
            last_time_servo_move = time_now
            if servo_going_up:
                servo_angle += 1
                if servo_angle == 180:
                    servo_going_up = False
            else:
                servo_angle -= 1
                if servo_angle == 0:
                    servo_going_up = True
            cmd = "servo:" + str(servo_angle) + "\n"
            ser.write(cmd.encode('utf-8'))
            
        # Change servo speed
        if ser.in_waiting > 0:
            msg = ser.readline().decode('utf-8').rstrip()
            if msg == "button_pressed":
                servo_delay_index += 1
                if servo_delay_index >= len(servo_delays):
                    servo_delay_index = 0
                servo_delay = servo_delays[servo_delay_index]
except KeyboardInterrupt:
    print("Close serial communication.")
    ser.close()


