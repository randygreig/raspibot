#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)

GPIO.output(7, True)
time.sleep(2)
GPIO.output(8, True)
time.sleep(2)
GPIO.output(9, True)
time.sleep(2)

GPIO.output(7, False)
GPIO.output(8, False)
GPIO.output(9, False)

GPIO.cleanup()

