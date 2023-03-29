import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
button=2
led=3


gpio.setup(led,gpio.OUT)
gpio.setup(button,gpio.IN)
gpio.setup(button,gpio.IN)

while True:
    if gpio.input(button)==0:
        gpio.output(led,gpio.HIGH)
    else:
        gpio.output(led,gpio.LOW)
        