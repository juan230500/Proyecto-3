import serial
import time

arduino=serial.Serial("COM3",38400)
time.sleep(1.62) #tiempo de reacción experimental
while 1:
    a=arduino.readline()
    print(a)
