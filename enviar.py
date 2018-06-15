import serial
import time

arduino=serial.Serial("COM3",38400)
print("leds=111000,display=9".encode())
arduino.write(b"leds=111000,display=6;")
