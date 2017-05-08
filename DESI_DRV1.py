#!/usr/bin/python
# @Author: Eddie Ruano
# @Date:   2017-05-01 05:14:54
# @Last Modified by:   Eddie Ruano
# @Last Modified time: 2017-05-08 03:36:55

"""
Basic DESI Driver for Prototyping
"""
import RPi.GPIO as GPIO
import time
# #Buttons# #
G_INSTART = 2
G_INSTOP = 3
G_INSLOW = 17
G_INMED = 27
G_INFAST = 22
# #Relays# #
GR_START = 5
GR_PAUSE = 6
GR_OFF = 13
GR_ENTER = 19
# #Keypad Relays# #
GR_00 = 12
GR_01 = 26
GR_02 = 14
GR_03 = 15
# #BOUNCE IN MS# #
bounceTime = 300


### MAIN PROGRAM START ###
def main():
	GPIO.setmode(GPIO.BCM)

	initializeButtons(G_INSTART, G_INSTOP)
	initializeRelay(GR_START, GR_OFF, GR_PAUSE, GR_ENTER, GR_00, GR_01, GR_02, GR_03)

	GPIO.add_event_detect(G_INSTART, GPIO.FALLING, performStart, bounceTime)
	GPIO.add_event_detect(G_INSTOP, GPIO.FALLING, performStop, bounceTime)

	activeFlag = True
	print("In Main Loop:\n")
	while activeFlag:
		

def performStart(channel):
	GPIO.output(GR_START, GPIO.LOW)
   time.sleep(0.1)
   GPIO.output(GR_START GPIO.HIGH)
   time.sleep(0.1)
def performStop(channel):
	GPIO.output(GR_STOP, GPIO.LOW)
   time.sleep(0.1)
   GPIO.output(GR_STOP GPIO.HIGH)
   time.sleep(0.1)

def initializeButtons(start, stop):
	GPIO.setup(start, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(stop, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def initializeRelay(start, stop, pause, enter, k0, k1, k2, k3):
	GPIO.setup(start, GPIO.OUT)
	GPIO.setup(stop, GPIO.OUT)
	GPIO.setup(pause, GPIO.OUT)
	GPIO.setup(enter, GPIO.OUT)
	GPIO.setup(k0, GPIO.OUT)
	GPIO.setup(k1, GPIO.OUT)
	GPIO.setup(k2, GPIO.OUT)
	GPIO.setup(k3, GPIO.OUT)
	##
	## 
	##
	GPIO.output(start, GPIO.HIGH)
	GPIO.output(stop, GPIO.HIGH)
	GPIO.output(pause, GPIO.HIGH)
	GPIO.output(enter, GPIO.HIGH)
	GPIO.output(k0, GPIO.HIGH)
	GPIO.output(k1, GPIO.HIGH)
	GPIO.output(k2, GPIO.HIGH)
	GPIO.output(k3, GPIO.HIGH)
	print("Relays Complete.\n")

###MAIN CALL ###
if __name__ == "__main__":
   main()
