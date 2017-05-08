#!/usr/bin/python
# @Author: Eddie Ruano
# @Date:   2017-05-01 05:14:54
# @Last Modified by:   Eddie Ruano
# @Last Modified time: 2017-05-08 05:49:37

"""
Basic DESI Driver for Prototyping
"""
import RPi.GPIO as GPIO
import time
# #Buttons# #
G_INSTART = 17
G_INSTOP = 27
G_INSLOW = 16
G_INMED = 20
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
bounceTime = 700
# #STATE# #
state = "speed0"


### MAIN PROGRAM START ###
def main():
   GPIO.setmode(GPIO.BCM)
   GPIO.cleanup()
   initializeButtons(G_INSTART, G_INSTOP)
   initializeKnob(G_INSLOW, G_INMED)
   #initializeRelay(GR_START, GR_OFF, GR_PAUSE, GR_ENTER, GR_00, GR_01, GR_02, GR_03)

   GPIO.add_event_detect(G_INSTART, GPIO.FALLING, performStart, bounceTime)
   GPIO.add_event_detect(G_INSTOP, GPIO.FALLING, performStop, bounceTime)
   GPIO.add_event_detect(G_INSLOW, GPIO.FALLING, performS1, bounceTime)


   activeFlag = True
   print("In Main Loop:\n")
   while activeFlag:
      if (state == "speed1"):
         GPIO.remove_event_detect(G_INSLOW)
           GPIO.add_event_detect(G_INMED, GPIO.FALLING, performS2, bounceTime)
      elif (state == "speed2"):
         GPIO.remove_event_detect(G_INSLOW)
         GPIO.add_event_detect(G_INSLOW, GPIO.FALLING, performS1, bounceTime)
      else
         print("error")

   GPIO.cleanup()

def performS1(channel):
   print("Speed1")
   state = "Speed1"
def performS2(channel):
   print("Speed1")
   state = "Speed1"
def performStart(channel):
   print("start")
   #GPIO.output(GR_START, GPIO.LOW)
   time.sleep(0.1)
   #GPIO.output(GR_START, GPIO.HIGH)
   time.sleep(0.1)
def performStop(channel):
   print("stop")
   #GPIO.output(GR_PAUSE, GPIO.LOW)
   time.sleep(0.1)
   #GPIO.output(GR_PAUSE, GPIO.HIGH)
   time.sleep(0.1)

def initializeButtons(start, stop):
   GPIO.setup(start, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   GPIO.setup(stop, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def initializeKnob(speed1, speed2):
   GPIO.setup(speed1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   GPIO.setup(speed2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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
