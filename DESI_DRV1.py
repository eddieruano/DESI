#!/usr/bin/python
# @Author: Eddie Ruano
# @Date:   2017-05-01 05:14:54
# @Last Modified by:   Eddie Ruano
# @Last Modified time: 2017-05-08 08:23:59

"""
Basic DESI Driver for Prototyping
"""
import RPi.GPIO as GPIO
import time
# #Buttons# #
G_INSTART = 17
G_INPAUSE= 27
G_INSLOW = 22
G_INMED = 20
#G_INFAST = 16
# #Relays# #
GR_START = 20
GR_PAUSE = 21
#GR_OFF = 6
GR_ENTER = 23
# #Keypad Relays# #
#GR_00 = 12
GR_01 = 24
GR_02 = 16
#GR_03 = 15
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
   initializeRelay(GR_START, GR_PAUSE, GR_ENTER, GR_01, GR_02)

   GPIO.add_event_detect(G_INSTART, GPIO.FALLING, performStart, bounceTime)
   GPIO.add_event_detect(G_INPAUSE, GPIO.FALLING, performStop, bounceTime)

   GPIO.add_event_detect(G_INSLOW, GPIO.FALLING, performS1, bounceTime)
   GPIO.add_event_detect(G_INMED, GPIO.FALLING, performS2, bounceTime)

   activeFlag = True
   print("In Main Loop:\n")
   while activeFlag:
      if (state == "speed1"):
         
      elif (state == "speed2"):
         

   GPIO.cleanup()

def performS1(channel):
   print("Speed1")
   state = "Speed1"
   GPIO.remove_event_detect(G_INSLOW)
   GPIO.add_event_detect(G_INMED, GPIO.FALLING, performS2, bounceTime)
def performS2(channel):
   print("Speed2")
   state = "Speed2"
   GPIO.remove_event_detect(G_INMED)
   GPIO.add_event_detect(G_INSLOW, GPIO.FALLING, performS1, bounceTime)

def performStart(channel):
   print("start")
   GPIO.output(GR_START, GPIO.LOW)
   time.sleep(0.1)
   GPIO.output(GR_START, GPIO.HIGH)
   time.sleep(0.1)
   # Now press enter
   GPIO.output(GR_ENTER, GPIO.LOW)
   time.sleep(0.1)
   GPIO.output(GR_ENTER, GPIO.HIGH)
   time.sleep(0.1)
   # done
def performStop(channel):
   print("stop")
   GPIO.output(GR_PAUSE, GPIO.LOW)
   time.sleep(0.1)
   GPIO.output(GR_PAUSE, GPIO.HIGH)
   time.sleep(0.1)
   #done

def initializeButtons(start, pause):
   GPIO.setup(start, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   GPIO.setup(pause, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def initializeKnob(speed1, speed2):
   GPIO.setup(speed1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   GPIO.setup(speed2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def initializeRelay(start, pause, enter, k1, k2):
   GPIO.setup(start, GPIO.OUT)
   #GPIO.setup(stop, GPIO.OUT)
   GPIO.setup(pause, GPIO.OUT)
   GPIO.setup(enter, GPIO.OUT)
   #GPIO.setup(k0, GPIO.OUT)
   GPIO.setup(k1, GPIO.OUT)
   GPIO.setup(k2, GPIO.OUT)
   #GPIO.setup(k3, GPIO.OUT)
   ##
   ## 
   ##
   GPIO.output(start, GPIO.HIGH)
   #GPIO.output(stop, GPIO.HIGH)
   GPIO.output(pause, GPIO.HIGH)
   GPIO.output(enter, GPIO.HIGH)
   #GPIO.output(k0, GPIO.HIGH)
   GPIO.output(k1, GPIO.HIGH)
   GPIO.output(k2, GPIO.HIGH)
   #GPIO.output(k3, GPIO.HIGH)
   print("Relays Complete.\n")

###MAIN CALL ###
if __name__ == "__main__":
   main()
