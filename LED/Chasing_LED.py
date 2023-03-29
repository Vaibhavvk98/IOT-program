import RPi.GPIO as pin
import time
import array
led = array.array('i', [2,3,4,17,27])
pin.setmode(pin.BCM)
for i in range (0,5):
    pin.setup(led[i], pin.OUT)

while True:
    for i in range (0,5):
        pin.output ( led [i],pin.HIGH)
        time.sleep(0.25)
            
    for i in reversed(range (0,5)):
        pin.output ( led [i],pin.LOW)
        time.sleep(0.25)