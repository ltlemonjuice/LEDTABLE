#!/usr/bin/env python

import time
import array
import fcntl
import sys

spidev = file("/dev/spidev0.0", "wb")
#byte array to store rgb values
rgb=bytearray(3)
#setting spi frequency to 400kbps
fcntl.ioctl(spidev, 0x40046b04, array.array('L', [400000]))

#functions
def black():
	for i in range(0, 100):
		rgb[0] = 0
		rgb[1] = 0
		rgb[2] = 0
		spidev.write(rgb)
	spidev.flush()
	
def white():
	for i in range(0,100):
		rgb[0] = 255
		rgb[1] = 255
		rgb[2] = 255
		spidev.write(rgb)
	spidev.flush()
	
def red():
	for i in range(0,100):
		rgb[0] = 255
		rgb[1] = 0
		rgb[2] = 0
		spidev.write(rgb)
	spidev.flush()

def green():
	for i in range(0,100):
		rgb[0] = 0
		rgb[1] = 255
		rgb[2] = 0
		spidev.write(rgb)
	spidev.flush()
	
def blue():
	for i in range(0,100):
		rgb[0] = 0
		rgb[1] = 0
		rgb[2] = 255
		spidev.write(rgb)
	spidev.flush()
	
def cyan():
	for i in range(0,100):
		rgb[0] = 0
		rgb[1] = 255
		rgb[2] = 255
		spidev.write(rgb)
	spidev.flush()
	
def yellow():
	for i in range(0,100):
		rgb[0] = 255
		rgb[1] = 255
		rgb[2] = 0
		spidev.write(rgb)
	spidev.flush()
	
def purple():
	for i in range(0,100):
		rgb[0] = 255
		rgb[1] = 0
		rgb[2] = 255
		spidev.write(rgb)
	spidev.flush()
	
def orange():
	for i in range(0,100):
		rgb[0] = 255
		rgb[1] = 50
		rgb[2] = 0
		spidev.write(rgb)
	spidev.flush()


#if statements for colors


if sys.argv[1] == "black":
	black()
elif sys.argv[1] == "red":
	red()
elif sys.argv[1] == "green":
	green()
elif sys.argv[1] == "blue":
	blue()	
elif sys.argv[1] == "white":
	white()
elif sys.argv[1] == "cyan":
	cyan()
elif sys.argv[1] == "yellow":
	yellow()
elif sys.argv[1] == "purple":
	purple()
elif sys.argv[1] == "orange":
	orange()
else:
	print("Color as Argument needed!")
	
print("Color displayed!")
