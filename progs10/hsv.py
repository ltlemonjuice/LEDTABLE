#!/usr/bin/env python
import time
import array
import fcntl
import sys
import select

spidev = file("/dev/spidev0.0", "wb")
#byte array to store rgb values
rgb=bytearray(3)
#setting spi frequency to 400kbps
fcntl.ioctl(spidev, 0x40046b04, array.array('L', [400000]))


def display():
	for i in range(0, 100):
		rgb[0] = r
		rgb[1] = g
		rgb[2] = b
		spidev.write(rgb)
	spidev.flush()
	
				
s = 0.001

while 1:
	#1
	r = 255
	b = 0
	for i in range(0,255):
		g = i
		display()
		time.sleep(s)

	#2
	g = 255
	b = 0
	for i in range(0,255):
		r = 255-i
		display()
		time.sleep(s)
	
	#3
	g = 255
	r = 0
	for i in range(0,255):
		b = i
		display()
		time.sleep(s)
	
	#4
	b = 255
	r = 0
	for i in range(0,255):
		g = 255-i
		display()
		time.sleep(s)
	
	#5
	b = 255
	g = 0
	for i in range(0,255):
		r = i
		display()
		time.sleep(s)
	
	#6
	r = 255
	g = 0
	for i in range(0,255):
		b = 255-i
		display()
		time.sleep(s)

