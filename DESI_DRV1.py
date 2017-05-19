#!/usr/bin/python
# @Author: Eddie Ruano
# @Date:   2017-05-01 05:14:54
# @Last Modified by:   Eddie Ruano
# @Last Modified time: 2017-05-18 19:08:37

"""
Basic DESI Driver for Prototyping
"""
import RPi.GPIO as GPIO
import time
# #Buttons# #
G_INSTART = 27
G_INPAUSE= 17
G_INSLOW = 22
G_INMED = 5
G_INFAST = 6
G_INFASTER = 13
G_INFASTEST = 19
# #Relays# #
GR_START = 20
GR_PAUSE = 21
#GR_OFF = 6
GR_ENTER = 23
# #Keypad Relays# #
GR_00 = 25
GR_01 = 24
GR_02 = 16
GR_03 = 12
GR_05 = 25
# #BOUNCE IN MS# #
bounceTime = 1000
# #STATE# #
state = "SpeedA"


### MAIN PROGRAM START ###
def main():
   GPIO.setmode(GPIO.BCM)
   initializeButtons(G_INSTART, G_INPAUSE)
   initializeKnob(G_INSLOW, G_INMED, G_INFAST, G_INFASTER, G_INFASTEST)
   initializeRelay(GR_START, GR_PAUSE, GR_ENTER, GR_00, GR_01, GR_02, GR_03, GR_05) 

   GPIO.add_event_detect(G_INSTART, GPIO.FALLING, performStart, bounceTime)
   GPIO.add_event_detect(G_INPAUSE, GPIO.FALLING, performStop, bounceTime)

   GPIO.add_event_detect(G_INSLOW, GPIO.FALLING, performS0, bounceTime)
   GPIO.add_event_detect(G_INMED, GPIO.FALLING, performS1, bounceTime)
   GPIO.add_event_detect(G_INFAST, GPIO.FALLING, performS2, bounceTime)
   GPIO.add_event_detect(G_INFASTER, GPIO.FALLING, performS3, bounceTime)

   activeFlag = True
   print("In Main Loop:\n")
   while activeFlag:
      activeFlag = True
      #if (state == "speed1"):
      #elif (state == "speed2"):
   #Should not get here
def performS0(channel):
   global state
   if state != "Speed0":
      # Trigger 1 twice
      GPIO.output(GR_00, GPIO.LOW)
      time.sleep(0.1)
      GPIO.output(GR_00, GPIO.HIGH)
      time.sleep(0.1)
      GPIO.output(GR_00, GPIO.LOW)
      time.sleep(0.1)
      GPIO.output(GR_00, GPIO.HIGH)
      time.sleep(0.1)
      #enter
      GPIO.output(GR_ENTER, GPIO.LOW)
      time.sleep(0.1)
      GPIO.output(GR_ENTER, GPIO.HIGH)
      time.sleep(0.1)
      global state
      state = "Speed0"
      print(state)
def performS1(channel):
   global state
   if state != "Speed1":
      # Trigger 1 twice
      GPIO.output(GR_01, GPIO.LOW)
      time.sleep(0.1)
      GPIO.output(GR_01, GPIO.HIGH)
      time.sleep(0.1)
      GPIO.output(GR_01, GPIO.LOW)
      time.sleep(0.1)
      GPIO.output(GR_01, GPIO.HIGH)
      time.sleep(0.1)
      #enter
      GPIO.output(GR_ENTER, GPIO.LOW)
      time.sleep(0.1)
      GPIO.output(GR_ENTER, GPIO.HIGH)
      time.sleep(0.1)
      global state
      state = "Speed1"
      print(state)
def performS2(channel):
   global state
   if state != "Speed2":
      # Trigger 1 twice
      GPIO.output(GR_02, GPIO.LOW)
      time.sleep(0.1)
      GPIO.output(GR_02, GPIO.HIGH)
      time.sleep(0.1)
      GPIO.output(GR_02, GPIO.LOW)
      time.sleep(0.1)
      GPIO.output(GR_02, GPIO.HIGH)
      time.sleep(0.1)
      #enter
      GPIO.output(GR_ENTER, GPIO.LOW)
      time.sleep(0.1)
      GPIO.output(GR_ENTER, GPIO.HIGH)
      time.sleep(0.1)
      #state variable
      global state
      state = "Speed2"
      print(state)
def performS3(channel):
   global state
   if state != "Speed3":
      # Trigger 1 twice
      GPIO.output(GR_03, GPIO.LOW)
      time.sleep(0.1)
      GPIO.output(GR_03, GPIO.HIGH)
      time.sleep(0.1)
      GPIO.output(GR_03, GPIO.LOW)
      time.sleep(0.1)
      GPIO.output(GR_03, GPIO.HIGH)
      time.sleep(0.1)
      #enter
      GPIO.output(GR_ENTER, GPIO.LOW)
      time.sleep(0.1)
      GPIO.output(GR_ENTER, GPIO.HIGH)
      time.sleep(0.1)
      #state variable
      global state
      state = "Speed3"
      print(state)
def performStart(channel):
   print("start")
   GPIO.output(GR_START, GPIO.LOW)
   time.sleep(0.1)
   GPIO.output(GR_START, GPIO.HIGH)
   time.sleep(0.1)
   GPIO.output(GR_ENTER, GPIO.LOW)
   time.sleep(0.1)
   GPIO.output(GR_ENTER, GPIO.HIGH)
   time.sleep(0.1)
def performStop(channel):
   print("stop")
   GPIO.output(GR_PAUSE, GPIO.LOW)
   time.sleep(0.1)
   GPIO.output(GR_PAUSE, GPIO.HIGH)
   time.sleep(0.1)
def initializeButtons(start, pause):
   GPIO.setup(start, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   GPIO.setup(pause, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   print("Buttons Complete.\n")
def initializeKnob(speed1, speed2, speed3, speed4, speed5):
   GPIO.setup(speed1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   GPIO.setup(speed2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   GPIO.setup(speed3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   GPIO.setup(speed4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   GPIO.setup(speed5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
   print("Knob Complete.\n")
def initializeRelay(start, pause, enter, k0, k1, k2, k3, k5):
   GPIO.setup(start, GPIO.OUT)
   GPIO.setup(pause, GPIO.OUT)
   GPIO.setup(enter, GPIO.OUT)
   GPIO.setup(k0, GPIO.OUT)
   GPIO.setup(k1, GPIO.OUT)
   GPIO.setup(k2, GPIO.OUT)
   GPIO.setup(k3, GPIO.OUT)
   GPIO.setup(k5, GPIO.OUT)
   GPIO.output(start, GPIO.HIGH)
   GPIO.output(pause, GPIO.HIGH)
   GPIO.output(enter, GPIO.HIGH)
   GPIO.output(k0, GPIO.HIGH)
   GPIO.output(k1, GPIO.HIGH)
   GPIO.output(k2, GPIO.HIGH)
   GPIO.output(k3, GPIO.HIGH)
   GPIO.output(k5, GPIO.HIGH)
   print("Relays Complete.\n")

###MAIN CALL ###
if __name__ == "__main__":
   main()
