import matplotlib.pyplot as plt
from gpiozero import LED
from gpiozero import DistanceSensor
import time

sensor = DistanceSensor(echo = 23, trigger = 24)

red = LED(14)
yellow = LED(15)
green = LED(18)

while True:

    distance = sensor.distance * 100
    print("distance : ",  distance)
    plt.plot(distance)
    plt.show()
    if distance < 20:
        red.on()
        yellow.off()
        green.off()
    elif distance > 40:
        red.off()
        yellow.off()
        green.on()
    else:
        red.off()
        yellow.on()
        green.off()
    time.sleep(0.2)