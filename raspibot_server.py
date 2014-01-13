#!/usr/bin/python

import RPi.GPIO as GPIO
import socket
import time
import nxt.locator
from nxt.motor import *
from nxt.sensor import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)

brick = nxt.locator.find_one_brick()
print "Connected to NXT..."
m_left = Motor(brick, PORT_B)
m_right = Motor(brick, PORT_C)
both = nxt.SynchronizedMotors(m_left, m_right, 0)

robotsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
robotsock.bind(('', 9000))
robotsock.listen(1)
print "Listening on TCP 9000"

print "Waiting for connection..."
connection, addr = robotsock.accept()
connection.setblocking(0)
print "Connected by", addr[0]

while(1):
    GPIO.output(7, False)
    GPIO.output(8, False)
    GPIO.output(9, False)
    while(1):
        try:
            sockdata = connection.recv(1)
            break
        except:
            pass
    if sockdata == 'M':
        print "beep"
        brick.play_tone_and_wait(1000, 500)
    if sockdata == 'F':
        print "forward"
        both.turn(100, 360, False)
    if sockdata == 'B':
        print "backwards"
        both.turn(-100, 360, False)
    if sockdata == 'R':
        print "right"
        m_right.turn(100, 360, False)
    if sockdata == 'L':
        print "left"
        m_left.turn(100, 360, False)
    if sockdata == 'Q':
        break
    print 'Distance:', Ultrasonic(brick, PORT_4).get_sample()
    if Ultrasonic(brick, PORT_4).get_sample() < 20:
        both.brake()

GPIO.output(7, False)
GPIO.output(8, False)
GPIO.output(9, False)

GPIO.cleanup()

