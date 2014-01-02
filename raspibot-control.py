#!/usr/bin/env python

###############################################################################
# Module:   raspibot-control.py
# Created:  2013-12-28
# Author:   Randy Greig
# Version:  0.1
'''

Dependencies:
  pygame   - http://www.pygame.org/
'''
###############################################################################

print "\n================================================"
print "        raspibot Joystick control"
print "================================================"

# Import dependent Python modules
import socket
try:
	import pygame.joystick
except:
	print "\nPlease install the 'pygame' module <http://www.pygame.org/>.\n"
	quit()

robotsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
robotsock.connect(("192.168.1.52", 9000))

# Allow for multiple joysticks
joy = []

# Handle joystick event
def handleJoyEvent(e):
    # Identify joystick axes and assign events
    if e.type == pygame.JOYAXISMOTION:
        axis = "unknown"
        if (e.dict['axis'] == 0):
            axis = "X"
        if (e.dict['axis'] == 1):
            axis = "Y"
        if (e.dict['axis'] == 2):
            axis = "Throttle"
        if (e.dict['axis'] == 3):
            axis = "Z"

        # Convert joystick value to servo position for each axis
        if (axis != "unknown"):
            # str = "Axis: %s; Value: %f" % (axis, e.dict['value'])
            pos = e.dict['value']
            move = round(pos * 90, 0)
            serv = int(90 + move)
            str = "Axis: %s; Value: %f" % (axis, serv)
            # Uncomment to display axis values:
            output(str, e.dict['joy'])

            # X Axis
            if (axis == "X"):
                pos = e.dict['value']
                # convert joystick position to servo increment, 0-180
                move = round(pos * 90, 0)
                serv = int(90 + move)
                # and send to Arduino over serial connection
                #servo.move(1, serv)
            # Y Axis
            if (axis == "Y"):
                pos = e.dict['value']
                move = round(pos * 90, 0)
                serv = int(90 + move)
                #servo.move(2, serv)
            # Z Axis
            if (axis == "Z"):
                pos = e.dict['value']
                move = round(pos * 90, 0)
                serv = int(90 + move)
                #servo.move(3, serv)
            # Throttle
            if (axis == "Throttle"):
                pos = e.dict['value']
                move = round(pos * 90, 0)
                serv = int(90 + move)
                #servo.move(4, serv)

    # Assign actions for Button DOWN events
    elif e.type == pygame.JOYBUTTONDOWN:
        # Button 1 (trigger)
        if (e.dict['button'] == 0):
            print "Trigger Down"
            robotsock.send('R')
        # Button 2
        if (e.dict['button'] == 1):
            print "Button 2 Down"
            robotsock.send('G')
        # Button 3
        if (e.dict['button'] == 2):
            print "Button 3 Down"
            robotsock.send('B')
        # Button 4
        if (e.dict['button'] == 3):
            print "Button 4 Down"
        # Button 5
        if (e.dict['button'] == 4):
            print "Button 5 Down"
        # Button 6
        if (e.dict['button'] == 5):
            print "Button 6 Down"
            robotsock.send('Q')
            quit()

    # Assign actions for Button UP events
    elif e.type == pygame.JOYBUTTONUP:
        # Button 1 (trigger)
        if (e.dict['button'] == 0):
            print "Trigger Up"
            # Set pin 13 LED to LOW for digital on/off demo
            #servo.move(99, 0)
        # Button 2
        if (e.dict['button'] == 1):
            print "Button 2 Up"
        # Button 3
        if (e.dict['button'] == 2):
            print "Button 3 Up"
        # Button 4
        if (e.dict['button'] == 3):
            print "Button 4 Up"
        # Button 5
        if (e.dict['button'] == 4):
            print "Button 5 Up"
        # Button 6
        if (e.dict['button'] == 5):
            print "Button 6 Up"

    else:
        pass

# Print the joystick position
def output(line, stick):
    print "Joystick: %d; %s" % (stick, line)

# Wait for joystick input
def joystickControl():
    while True:
        e = pygame.event.wait()
        if (e.type == pygame.JOYAXISMOTION or e.type == pygame.JOYBUTTONDOWN or e.type == pygame.JOYBUTTONUP):
            handleJoyEvent(e)

# Main method
def main():
    # Initialize pygame
    pygame.joystick.init()
    pygame.display.init()
    if not pygame.joystick.get_count():
        print "\nPlease connect a joystick and run again.\n"
        quit()
    print "\n%d joystick(s) detected." % pygame.joystick.get_count()
    for i in range(pygame.joystick.get_count()):
        myjoy = pygame.joystick.Joystick(i)
        myjoy.init()
        joy.append(myjoy)
        print "Joystick %d: " % (i) + joy[i].get_name()
    print "Depress joystick button 6 to quit.\n"

    # Run joystick listener loop
    joystickControl()

# Allow use as a module or standalone script
if __name__ == "__main__":
    main()
