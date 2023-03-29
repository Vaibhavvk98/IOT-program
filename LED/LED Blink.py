import RPi.GPIO as pin
import time
pin.setmode(pin.BCM)

while True:
    pin.setup(2, pin.OUT)
    for blink in range(0,10):
        pin.output(2, pin.HIGH)
        time.sleep(1)
        pin.output(2, pin.LOW)
        time.sleep(1)
        
    pin.setup(3, pin.OUT)
    for blink in range(0,10):
        pin.output(3, pin.HIGH)
        time.sleep(0.5)
        pin.output(3, pin.LOW)
        time.sleep(0.5)
        
    pin.setup(4, pin.OUT)
    for blink in range(0,10):
        pin.output(4, pin.LOW)
        time.sleep(0.25)
        pin.output(4, pin.HIGH)
        time.sleep(0.25)
        
    pin.setup(5, pin.OUT)
    for blink in range(0,10):
        pin.output(5, pin.LOW)
        time.sleep(0.12)
        pin.output(5, pin.HIGH)
        time.sleep(0.12)