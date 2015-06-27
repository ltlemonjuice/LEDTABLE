#!/usr/bin/env python
#coding: utf8 
from imgdisp import imgdisp
import time
import sys

#via commandline argument ist es möglich 
#die geschwindigkeit anzupass
if len(sys.argv) > 1:
	s = float(sys.argv[1])
else:
	#10 Bilder pro Sekunde
	s = 0.1

while True:
	for i in range(2, 92):
		file = "/home/pi/led/progs10/img/animation1/%d.png" %(i)
		imgdisp(file)
		time.sleep(s)