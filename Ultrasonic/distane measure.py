import RPi.GPIO as pin
import time

pin.setwarnings(False)
trig=int(2)
echo=int(3)
pin.setmode(pin.BCM)

pin.setup(trig, pin.OUT)
pin.setup(echo, pin.IN)

while True:
    pin.output(trig,False)
    time.sleep(0.000002)
    pin.output(trig,True)
    time.sleep(0.000010)
    pin.output(trig,False)
    
    StarTime=time.time()
    StopTime=time.time()
    
    while pin.input(echo)==0:
        StartTime=time.time()
        
    while pin.input(echo)==1:
        StopTime=time.time()
        
    TimeElapsed=StopTime-StartTime
    distance=(timeElapsed*34300)/2
    distance=int(distance)
    if(distance<=20):
        print("Higher Distance:",distance)
        break
    print(distance)
    time.sleep(0.1)                                                                                                                                