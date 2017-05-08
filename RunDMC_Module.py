#!/usr/bin/env python
"""RunDMC_Module.py, by Eddie Ruano, January 2017
Basic Debugger and Tester tool for development of DESI System
"""

### IMPORT MODULES ###
import os
import time
import curses
import RPi.GPIO as GPIO

### MAIN PROGRAM START ###
def main():
    # Begin Sensor Read Code Debugger #
    #Set Mode on GPIO Pins
    GPIO.setmode(GPIO.BCM)
    # Set up Start/Stop Button functionality
    GPIO_START = 13
    GPIO_STOP = 19
    initStopLight(GPIO_START, GPIO_STOP)
    # Set up Relay Nodes
    POWER_RELAY = 26
    UP_RELAY = 5
    DOWN_RELAY = 6
    OFF_RELAY = 27
    initRelays(POWER_RELAY, UP_RELAY, DOWN_RELAY, OFF_RELAY)
    # Speed Levels
    level1 = 10
    level2 = 30
    level3 = 40
    # Set Up Voyager 1 & 2 Proximity Sensors
    GPIOV1_ECHO = 20
    GPIOV1_TRIG = 21
    GPIOV2_ECHO = 24
    GPIOV2_TRIG = 23
    #set GPIO direction (IN / OUT)
    GPIO.setup(GPIOV1_TRIG, GPIO.OUT)
    GPIO.setup(GPIOV1_ECHO, GPIO.IN)
    GPIO.setup(GPIOV2_TRIG, GPIO.OUT)
    GPIO.setup(GPIOV2_ECHO, GPIO.IN)
    # Create Display Window CURSES
    stdscr = curses.initscr()
    stdscr.border(0)
    curses.noecho()
    renderDisplay(stdscr)
    #### Begin Sensor Flow ####
    activeFlag = True
    count = 0
    status = "Green"
    stdscr.nodelay(True)
    while activeFlag == True:
        # Call for the distance
        try: 
            inchar = stdscr.getkey()
            if inchar == "q":
                activeFlag = False
                break
            elif inchar == "s":
                powerStart(OFF_RELAY)
            elif inchar == "p":
                powerStart(POWER_RELAY)
            elif inchar == "u":
                increaseSpeed(UP_RELAY, level1)
            elif inchar == "d":
                decreaseSpeed(DOWN_RELAY, level1)
        except:
            time.sleep(0.2)
        # Handle Start/Stop
        if GPIO.event_detected(GPIO_START):
           stdscr.addstr(40, 5, "Start Detected.")
           powerStart(POWER_RELAY)
        if GPIO.event_detected(GPIO_STOP):
           stdscr.addstr(40, 5, "Increase Detected. ")
           increaseSpeed(UP_RELAY, level1)
        # Handle Distance Queries
        distV1 = queryDistance(GPIOV1_TRIG, GPIOV1_ECHO)
        distV2 = queryDistance(GPIOV2_TRIG, GPIOV2_ECHO)
        status = updateV1(stdscr, distV1)
        updateV2(stdscr, distV2)
        error = str(distV2 - distV1)
        stdscr.addstr(13, 44, error)
        stdscr.refresh()
        if status == "Red":
            stdscr.addstr(17, 22, "RED ZONE TIMEOUT 10 sec.")
        else:
            # Find Average Distance w/ Two Sensors
            average = (distV1 + distV2) / 2
            # Find the Slack Left in Position Movement
            slack = 30 - average
            stdscr.addstr(18, 15, "Slack Dist: "+str(int(slack))+" cm ")
            # Find by how much percent-wise the speed should be reduced
            if status == "Yellow":
                # Subtract Green Zone 10 & divvy 2 & make percent by 10
                redux = ((average - 10) / 2) * 10
                redux = int(redux)
                redux_str = "Speed Redux By: " + str(redux) + " %      "
                stdscr.addstr(16, 24, redux_str) 
            else:
                stdscr.addstr(16, 24, "No Speed Adjustment")

        # Positioning Status
        printProgressBar(stdscr, average, 30, prefix = 'StartZone', suffix = 'RedZone', length = 35)

    # End the Window
    curses.echo()
    curses.endwin()
    # Closes Active GPIO Connections #
    GPIO.cleanup()

### END MAIN PROGRAM ###

### BEGIN FUNCTIONS ###
def updateV1(screen, distance):
    status = "Green"
    update = str(distance) +  " cm"
    screen.addstr(8, 8, update)
    if distance < 17.2:
        screen.addstr(14, 30, "Within Green Zone", curses.A_UNDERLINE)
    elif distance > 17.2 and distance < 30:
        screen.addstr(14, 30, "Within Yellow Zone", curses.A_UNDERLINE)
        status = "Yellow"
    else:
        screen.addstr(14, 30, "RED ZONE, Beginning Timeout", curses.A_UNDERLINE)
        status = "Red"

    return status
def updateV2(screen, distance):
    update = str(distance) + " cm"
    screen.addstr(8, 43, update)
    if distance < 17.2:
        screen.addstr(15, 30, "Within Green Zone", curses.A_UNDERLINE)
    elif distance > 17.2 and distance < 30:
        screen.addstr(15, 30, "Within Yellow Zone", curses.A_UNDERLINE)
    else:
        screen.addstr(15, 30, "RED ZONE, Beginning Timeout", curses.A_UNDERLINE)

def displayHeaderBar(stdscr):
    #Print the Greeting
    stdscr.addstr(1, 14, "*******  DESI Mission Control Module v1.0  *******")
    stdscr.addstr(2, 14, "**************  Updated April 2017  **************")

def renderDisplay(stdscr):
    v_box_ht = 5
    v_box_wt = 30
    # Display Top Bar
    displayHeaderBar(stdscr)
    # Create Left Window
    leftBox = stdscr.subwin(v_box_ht, v_box_wt, 5, 5)
    leftBox.box()
    # Create Right Window
    rightBox = stdscr.subwin(v_box_ht, v_box_wt, 5, 40)
    rightBox.box()
    leftBox.addstr(1, 5, "Voyager 1 Distance")
    rightBox.addstr(1, 5, "Voyager 2 Distance")
    updateView(stdscr, leftBox)
    updateView(stdscr, rightBox)
    # Create MidSetion Status
    midBox = stdscr.subwin(10, 60, 10, 10)
    midBox.box()
    midBox.addstr(1, 21, "Control Status")
    midBox.addstr(3, 5, "Voyager Disparity Error +/-: ")
    midBox.addstr(4, 5, "ProxV1 Status: ")
    midBox.addstr(5, 5, "ProxV2 Status: ")
    midBox.addstr(6, 5, "SlowDown Factor: 0x (in Green)")
    midBox.addstr(7, 5, "Timeout: 0 (in Green)")
    updateView(stdscr, midBox)
    # Create Touch Box
    touchBox = stdscr.subwin(10, 60, 25, 10)
    touchBox.box()
    touchBox.addstr(1, 21, "Cap Touch Status")
    updateView(stdscr, touchBox)
    # Create Serial Box

def queryDistance( trigger, echo):
    # set Trigger to HIGH
    GPIO.output(trigger, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(trigger, False)
    StartTime = time.time()
    StopTime = time.time()
    # save StartTime
    while GPIO.input(echo) == 0:
        StartTime = time.time()
    # save time of arrival
    while GPIO.input(echo) == 1:
        StopTime = time.time()
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    return distance

def updateView(main, box):
    main.refresh()
    box.refresh()

def printProgressBar (screen, iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    end = "%\r"
    buf = "%s |%s| %s %s %%" % (prefix, bar, suffix, percent)
    screen.addstr(22, 5, buf) 
    # Print New Line on Complete
    if iteration == total: 
        print()
def initStopLight(start, stop):
    # Set up the start input and set the pull down
    GPIO.setup(start, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(start, GPIO.FALLING) 
    # Set up the stop input and set the pull down
    GPIO.setup(stop, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(stop, GPIO.FALLING) 
def initRelays(power, up, down, off):
    GPIO.setup(power, GPIO.OUT)
    GPIO.setup(up, GPIO.OUT)
    GPIO.setup(down, GPIO.OUT)
    GPIO.setup(off, GPIO.OUT)
    # ALL LOW
    GPIO.output(power, GPIO.HIGH)
    GPIO.output(up, GPIO.HIGH)
    GPIO.output(down, GPIO.HIGH)
    GPIO.output(off, GPIO.HIGH)
def powerStart(GPIO_POWER):
        GPIO.output(GPIO_POWER, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(GPIO_POWER, GPIO.HIGH)
        time.sleep(0.1) 
def increaseSpeed(GPIO_UPSPEED, level):
    for x in range (0, level):
        GPIO.output(GPIO_UPSPEED, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(GPIO_UPSPEED, GPIO.HIGH)
        time.sleep(0.1)
def decreaseSpeed(GPIO_DOWNSPEED, level):
    for x in range (0, level):
        GPIO.output(GPIO_DOWNSPEED, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(GPIO_DOWNSPEED, GPIO.HIGH)
        time.sleep(0.1)
###MAIN CALL ###
if __name__ == "__main__":
    main()

