#!/usr/bin/env python
"""
DESI Main Module
"""

# IMPORT MODULES #
import time
import RPi.GPIO as GPIO
import proxSensor

# MAIN PROGRAM START #
def main():

    GPIO.setmode(GPIO.BCM)
    # !!!!! INITIALIZATION OF VARIABLES OCCURS BELOW !!!!! #

    GPIO.cleanup()
    # !! INPUT BUTTON PINS !! #
    GPIO_START_IN = 17
    GPIO_STOP_IN = 27
    # !! PROXIMITY SENSOR PINS !! #
    GPIO_V1_TRIG = 20       # Voyager1 = Proximity Sensor 1 #
    GPIO_V1_ECHO = 21
    GPIO_V2_TRIG = 24       # Voyager2 = Proximity Sensor 2 #
    GPIO_V2_ECHO = 23
    # !! RELAY RUNNER PINS !! #
    GPIO_RELAY_ON = 5
    GPIO_RELAY_OFF = 6
    GPIO_RELAY_UP = 13
    GPIO_RELAY_DOWN = 19
    GPIO_RELAY_PAUSE = 26
    # !!!!! CREATE CLASS INSTANCES BELOW !!!!! #
    Voyager1 = proxSensor.proxSensor("Voyager1", GPIO_V1_TRIG, GPIO_V1_ECHO)
    Voyager1.proxInitSensor(GPIO_V1_TRIG, GPIO_V1_ECHO)
    Voyager2 = proxSensor.proxSensor("Voyager2", GPIO_V2_TRIG, GPIO_V2_ECHO)
    Voyager2.proxInitSensor(GPIO_V2_TRIG, GPIO_V2_ECHO)
    #Sentinel = Sentinel("Sentinel")

    activeFlag = True
    count  = 10
    # Initiate Main Loop
    while activeFlag:
        print("Voyager 1")
        distanceV1 = Voyager1.proxQueryDist()
        print(distanceV1)
        time.sleep(0.1)
        distanceV2 = Voyager2.proxQueryDist()
        print(distanceV2)
        time.sleep(0.1)
        if count > 10:
            activeFlag = False

    print("done")
    GPIO.cleanup()
# MAIN CALL #
if __name__ == "__main__":
    main()
