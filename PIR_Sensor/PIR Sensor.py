import RPi.GPIO as pin
import time
pir=3
pin.setmode(pin.BCM)
pin.setup(pir,pin.IN)

while True:
   value=pin.input(pir)
   if (value==0):
       print("No intruders",value)
       time.sleep(0.5)
    elif(value==1):
        print("Intruder detected",value)
        time.sleep(0.5)
