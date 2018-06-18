import serial
import time

arduino=serial.Serial("COM3",38400)
time.sleep(1.62) #tiempo de reacción experimental
i=0
while 1:
    time.sleep(.1)
    if i==0:
        a=arduino.readline()
        print(a)
        i=0
    else:
        i+=1
