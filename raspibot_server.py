#!/usr/bin/python

import RPi.GPIO as GPIO
import socket
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)

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
    if sockdata == 'R':
        print "red"
        GPIO.output(7, True)
        time.sleep(2)
    if sockdata == 'G':
        print "green"
        GPIO.output(8, True)
        time.sleep(2)
    if sockdata == 'B':
        print "blue"
        GPIO.output(9, True)
        time.sleep(2)
    if sockdata == 'Q':
        break

GPIO.output(7, False)
GPIO.output(8, False)
GPIO.output(9, False)

GPIO.cleanup()

