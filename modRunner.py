#!/usr/bin/python
# @Author: Eddie Ruano
# @Date:   2017-05-08 01:16:02
# @Last Modified by:   Eddie Ruano
# @Last Modified time: 2017-05-09 19:17:25
# 
import RPi.GPIO as GPIO

def runnerInit(GSTART, GPAUSE, GOFF, GSLOW, GMED, GFAST):
	#Set up each relay pin as an out
	# Set Mode on GPIO Pins BCM
   GPIO.setmode(GPIO.BCM)
   # Set as Outputs
   GPIO.setup(GSTART, GPIO.OUT)
   GPIO.setup(GPAUSE, GPIO.OUT)
   GPIO.setup(GOFF, GPIO.OUT)
   # Speed Relays
   GPIO.setup(GSLOW, GPIO.OUT)
   GPIO.setup(GMED, GPIO.OUT)
   GPIO.setup(GFAST, GPIO.OUT)
   # Set as Active Low-> 1-> 0 causes relay trip
   GPIO.output(GSTART, GPIO.HIGH)
   GPIO.output(GPAUSE, GPIO.HIGH)
   GPIO.output(GOFF, GPIO.HIGH)
   # Speed Lows
   GPIO.output(GSLOW, GPIO.HIGH)
   GPIO.output(GMED, GPIO.HIGH)
   GPIO.output(GFAST, GPIO.HIGH)


def runnerStatus():
