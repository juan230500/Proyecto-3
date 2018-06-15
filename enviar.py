import serial
import time

arduino=serial.Serial("COM3",38400)
time.sleep(1.62) #tiempo de reacción experimental
for i in range(10):
    arduino.write(b'leds=101010,display='+str(i).encode()+b';')
    time.sleep(1)

arduino.close()
