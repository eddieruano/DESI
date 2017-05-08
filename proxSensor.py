#!/usr/bin/python
# @Author: Eddie Ruano
# @Date:   2017-05-01 04:45:20
# @Last Modified by:   Eddie Ruano
# @Last Modified time: 2017-05-01 05:47:59
"""
Module/Driver for a Standard HCSR04 UltraSonic Sensor
"""

# Imports #
import time
import RPi.GPIO as GPIO


class proxSensor(object):
    """ Begin proxSensor Class Structure """
    def __init__(self, name, trigger, echo):
        self.name = name
        self.trigger = trigger
        self.echo = echo
    def proxInitSensor(self, GPIOTrigger, GPIOEcho):
        # Set GPIO Input/Output Direction
        # Trigger is an output
        theTime = time.ctime()
        GPIO.setup(GPIOTrigger, GPIO.OUT)
        # Echo is an input
        GPIO.setup(GPIOEcho, GPIO.IN)
        return "Prox Sensor Inititalized: " + "T: " + str(GPIOTrigger)
        + "E: " + str(GPIOEcho) + "at: " + theTime

    def proxQueryDist(self):
        # set Trigger to HIGH
        print(self.trigger)
        GPIO.output(self.trigger, True)
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.trigger, False)
        StartTime = time.time()
        StopTime = time.time()
        # save StartTime
        while GPIO.input(self.echo) == 0:
            StartTime = time.time()
        # save time of arrival
        while GPIO.input(self.echo) == 1:
            StopTime = time.time()
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # & divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
        return distance

    def proxCleanUp(self):
        # Reset these GPIO Pins after this script runs
        GPIO.cleanup()
        return "Success"
