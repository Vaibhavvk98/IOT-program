#from flask import Flask,render_template,request
import RPi.GPIO as gpio
import time
#import Adafruit_DHT
import urllib.request
from PIL import Image
gpio.setmode(gpio.BCM)


trig = 2
echo = 3
#dhtpin=17
#bulbpin=27
buz=14

#GPIO.setup(dhtpin, GPIO.IN)
#GPIO.setup(bulbpin, GPIO.OUT)
gpio.setup(trig,gpio.OUT)
gpio.setup(echo,gpio.IN)
gpio.setup(buz,gpio.OUT)


while True:
    gpio.output(trig,gpio.HIGH)
    time.sleep(0.00001)
    gpio.output(trig,gpio.LOW)
    
    
while gpio.input(echo)==0:
    start_time = time.time()
    
while gpio.input(echo)==1:
    end_time = time.time()
    pulse_duration = end_time - start_time
    distance = round(pulse_duration * 0.034/2, 2)
    print ("DISTANCE:",distance);
    
    if distance<20:
        gpio.output(buz,gpio.HIGH)
        
    else:
        gpio.output(buz,gpio.LOW)
   