import RPi.GPIO as pin
import time
pin.setmode(pin.BCM)
pin.setwarnings(False)

ir=2
led=3

pin.setup(ir,pin.IN)
pin.setup(led,pin.OUT)

while True:
    if pin.input(ir)==True:
        pin.output(led,pin.OUT)
    else:
        pin.out(led,pin.LOW)