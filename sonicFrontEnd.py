#!/usr/bin/python

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

TRIG1 = 23 
ECHO1 = 24

TRIG2 = 21
ECHO2 = 22

print "Initializing Sensor 1..."
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)

print "Initializing Sensor 2..."
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)

GPIO.output(TRIG1, False)
GPIO.output(TRIG2, False)
print "Sensor is settling..."
time.sleep(2)

GPIO.output(TRIG1, True)
GPIO.output(TRIG2, True)
time.sleep(0.00001)
GPIO.output(TRIG1, False)
GPIO.output(TRIG2, False)

while GPIO.input(ECHO1)==0:
  pulse_start1 = time.time()

while GPIO.input(ECHO1)==1:
  pulse_end1 = time.time()

while GPIO.input(ECHO2)==0:
  pulse_start1 = time.time()

while GPIO.input(ECHO2)==1:
  pulse_end1 = time.time()

pulse_duration1 = pulse_end1 - pulse_start1

distance1 = pulse_duration1 * 17150

distance1 = round(distance1, 2)

pulse_duration2 = pulse_end2 - pulse_start2

distance2 = pulse_duration2 * 17150

distance2 = round(distance2, 2)

print "Distance Sensor 1:",distance1,"cm"
print "Distance Sensor 2:",distance1,"cm"

GPIO.cleanup()