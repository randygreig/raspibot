#!/usr/bin/env python
import time
import os
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
DEBUG = 1
LOGGER = 1
 
# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)
 
        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low
 
        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:   
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
 
        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1
 
        GPIO.output(cspin, True)
 
        adcout /= 2       # first bit is 'null' so drop it
        return adcout
 
# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25
 
# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)
 
# temperature sensor connected channel 0 of mcp3008
adcnum = 0
 
while True:
        # read the analog pin 0
        read_adc0 = readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)
 
        # convert analog reading to millivolts = ADC * ( 5000 / 1024 )
        millivolts = read_adc0 * ( 5000.0 / 1024.0)
 
        # remove decimal point from millivolts
        millivolts = "%d" % millivolts
 
        print("read_adc0:", millivolts)
 
        # read the analog pin 1
        read_adc1 = readadc(1, SPICLK, SPIMOSI, SPIMISO, SPICS)
 
        # convert analog reading to millivolts = ADC * ( 5000 / 1024 )
        millivolts = read_adc1 * ( 5000.0 / 1024.0)
 
        # remove decimal point from millivolts
        millivolts = "%d" % millivolts
 
        print("read_adc1:", millivolts)
 
        # read the analog pin  2
        read_adc2 = readadc(2, SPICLK, SPIMOSI, SPIMISO, SPICS)
 
        # convert analog reading to millivolts = ADC * ( 5000 / 1024 )
        millivolts = read_adc2 * ( 5000.0 / 1024.0)
 
        # remove decimal point from millivolts
        millivolts = "%d" % millivolts
 
        print("read_adc2:", millivolts)
 
        # read the analog pin 3
        read_adc3 = readadc(3, SPICLK, SPIMOSI, SPIMISO, SPICS)
 
        # convert analog reading to millivolts = ADC * ( 5000 / 1024 )
        millivolts = read_adc3 * ( 5000.0 / 1024.0)
 
        # remove decimal point from millivolts
        millivolts = "%d" % millivolts
 
        print("read_adc3:", millivolts)
 
        # read the analog pin 4
        read_adc4 = readadc(4, SPICLK, SPIMOSI, SPIMISO, SPICS)
 
        # convert analog reading to millivolts = ADC * ( 5000 / 1024 )
        millivolts = read_adc4 * ( 5000.0 / 1024.0)
 
        # remove decimal point from millivolts
        millivolts = "%d" % millivolts
 
        print("read_adc4:", millivolts)
        print("\n")
        print("\n")
        print("\n")
 
        time.sleep(5)


