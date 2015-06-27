#!/usr/bin/env python
def imgdisp(filename):
	import time
	import array
	import fcntl
	import sys
	import Image
	import math

	# Open SPI device
	spidev = file("/dev/spidev0.0", "wb")
	#byte array to store rgb values
	rgb=bytearray(3)
	#setting spi frequency to 400kbps
	fcntl.ioctl(spidev, 0x40046b04, array.array('L', [400000]))

	#creating 10x10 matrix (last digit may be used later for alpha control)
	matrix = [[[0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255]],
			  [[0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255]],
			  [[0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255]],
			  [[0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255]],
			  [[0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255]],
			  [[0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255]],
			  [[0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255]],
			  [[0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255]],
			  [[0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255]],
			  [[0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255], [0, 0, 0, 255]]]


	#get image size. IMAGE MUST BE 10x10 pixels if not must resize
	img       = Image.open(filename)
	img = img.rotate(180)
	pixels    = img.load()

	#print "Allocating..."
	#re-allocate columns 1,3,5,7,9 for correct view
	for x in range(0,10):
		for y in range (0,10):
			matrix[x][y][0] = pixels[x,y][0] 
			matrix[x][y][1] = pixels[x,y][1] 
			matrix[x][y][2] = pixels[x,y][2]
			
			#Column 1
			col = 1
			if x == col and y == 0:
				matrix[x][y][0] = pixels[col,9][0] 
				matrix[x][y][1] = pixels[col,9][1] 
				matrix[x][y][2] = pixels[col,9][2]			
			elif x == col and y == 1:
				matrix[x][y][0] = pixels[col,8][0] 
				matrix[x][y][1] = pixels[col,8][1] 
				matrix[x][y][2] = pixels[col,8][2]	
			elif x == col and y == 2:
				matrix[x][y][0] = pixels[col,7][0] 
				matrix[x][y][1] = pixels[col,7][1] 
				matrix[x][y][2] = pixels[col,7][2]	
			elif x == col and y == 3:
				matrix[x][y][0] = pixels[col,6][0] 
				matrix[x][y][1] = pixels[col,6][1] 
				matrix[x][y][2] = pixels[col,6][2]
			elif x == col and y == 4:
				matrix[x][y][0] = pixels[col,5][0] 
				matrix[x][y][1] = pixels[col,5][1] 
				matrix[x][y][2] = pixels[col,5][2]
			if x == col and y == 5:
				matrix[x][y][0] = pixels[col,4][0] 
				matrix[x][y][1] = pixels[col,4][1] 
				matrix[x][y][2] = pixels[col,4][2]			
			elif x == col and y == 6:
				matrix[x][y][0] = pixels[col,3][0] 
				matrix[x][y][1] = pixels[col,3][1] 
				matrix[x][y][2] = pixels[col,3][2]	
			elif x == col and y == 7:
				matrix[x][y][0] = pixels[col,2][0] 
				matrix[x][y][1] = pixels[col,2][1] 
				matrix[x][y][2] = pixels[col,2][2]	
			elif x == col and y == 8:
				matrix[x][y][0] = pixels[col,1][0] 
				matrix[x][y][1] = pixels[col,1][1] 
				matrix[x][y][2] = pixels[col,1][2]
			elif x == col and y == 9:
				matrix[x][y][0] = pixels[col,0][0] 
				matrix[x][y][1] = pixels[col,0][1] 
				matrix[x][y][2] = pixels[col,0][2]
				
				#Column 3
			col = 3
			if x == col and y == 0:
				matrix[x][y][0] = pixels[col,9][0] 
				matrix[x][y][1] = pixels[col,9][1] 
				matrix[x][y][2] = pixels[col,9][2]			
			elif x == col and y == 1:
				matrix[x][y][0] = pixels[col,8][0] 
				matrix[x][y][1] = pixels[col,8][1] 
				matrix[x][y][2] = pixels[col,8][2]	
			elif x == col and y == 2:
				matrix[x][y][0] = pixels[col,7][0] 
				matrix[x][y][1] = pixels[col,7][1] 
				matrix[x][y][2] = pixels[col,7][2]	
			elif x == col and y == 3:
				matrix[x][y][0] = pixels[col,6][0] 
				matrix[x][y][1] = pixels[col,6][1] 
				matrix[x][y][2] = pixels[col,6][2]
			elif x == col and y == 4:
				matrix[x][y][0] = pixels[col,5][0] 
				matrix[x][y][1] = pixels[col,5][1] 
				matrix[x][y][2] = pixels[col,5][2]
			if x == col and y == 5:
				matrix[x][y][0] = pixels[col,4][0] 
				matrix[x][y][1] = pixels[col,4][1] 
				matrix[x][y][2] = pixels[col,4][2]			
			elif x == col and y == 6:
				matrix[x][y][0] = pixels[col,3][0] 
				matrix[x][y][1] = pixels[col,3][1] 
				matrix[x][y][2] = pixels[col,3][2]	
			elif x == col and y == 7:
				matrix[x][y][0] = pixels[col,2][0] 
				matrix[x][y][1] = pixels[col,2][1] 
				matrix[x][y][2] = pixels[col,2][2]	
			elif x == col and y == 8:
				matrix[x][y][0] = pixels[col,1][0] 
				matrix[x][y][1] = pixels[col,1][1] 
				matrix[x][y][2] = pixels[col,1][2]
			elif x == col and y == 9:
				matrix[x][y][0] = pixels[col,0][0] 
				matrix[x][y][1] = pixels[col,0][1] 
				matrix[x][y][2] = pixels[col,0][2]
				
				#Column 5
			col = 5
			if x == col and y == 0:
				matrix[x][y][0] = pixels[col,9][0] 
				matrix[x][y][1] = pixels[col,9][1] 
				matrix[x][y][2] = pixels[col,9][2]			
			elif x == col and y == 1:
				matrix[x][y][0] = pixels[col,8][0] 
				matrix[x][y][1] = pixels[col,8][1] 
				matrix[x][y][2] = pixels[col,8][2]	
			elif x == col and y == 2:
				matrix[x][y][0] = pixels[col,7][0] 
				matrix[x][y][1] = pixels[col,7][1] 
				matrix[x][y][2] = pixels[col,7][2]	
			elif x == col and y == 3:
				matrix[x][y][0] = pixels[col,6][0] 
				matrix[x][y][1] = pixels[col,6][1] 
				matrix[x][y][2] = pixels[col,6][2]
			elif x == col and y == 4:
				matrix[x][y][0] = pixels[col,5][0] 
				matrix[x][y][1] = pixels[col,5][1] 
				matrix[x][y][2] = pixels[col,5][2]
			if x == col and y == 5:
				matrix[x][y][0] = pixels[col,4][0] 
				matrix[x][y][1] = pixels[col,4][1] 
				matrix[x][y][2] = pixels[col,4][2]			
			elif x == col and y == 6:
				matrix[x][y][0] = pixels[col,3][0] 
				matrix[x][y][1] = pixels[col,3][1] 
				matrix[x][y][2] = pixels[col,3][2]	
			elif x == col and y == 7:
				matrix[x][y][0] = pixels[col,2][0] 
				matrix[x][y][1] = pixels[col,2][1] 
				matrix[x][y][2] = pixels[col,2][2]	
			elif x == col and y == 8:
				matrix[x][y][0] = pixels[col,1][0] 
				matrix[x][y][1] = pixels[col,1][1] 
				matrix[x][y][2] = pixels[col,1][2]
			elif x == col and y == 9:
				matrix[x][y][0] = pixels[col,0][0] 
				matrix[x][y][1] = pixels[col,0][1] 
				matrix[x][y][2] = pixels[col,0][2]
			
			#Column 7
			col = 7
			if x == col and y == 0:
				matrix[x][y][0] = pixels[col,9][0] 
				matrix[x][y][1] = pixels[col,9][1] 
				matrix[x][y][2] = pixels[col,9][2]			
			elif x == col and y == 1:
				matrix[x][y][0] = pixels[col,8][0] 
				matrix[x][y][1] = pixels[col,8][1] 
				matrix[x][y][2] = pixels[col,8][2]	
			elif x == col and y == 2:
				matrix[x][y][0] = pixels[col,7][0] 
				matrix[x][y][1] = pixels[col,7][1] 
				matrix[x][y][2] = pixels[col,7][2]	
			elif x == col and y == 3:
				matrix[x][y][0] = pixels[col,6][0] 
				matrix[x][y][1] = pixels[col,6][1] 
				matrix[x][y][2] = pixels[col,6][2]
			elif x == col and y == 4:
				matrix[x][y][0] = pixels[col,5][0] 
				matrix[x][y][1] = pixels[col,5][1] 
				matrix[x][y][2] = pixels[col,5][2]
			if x == col and y == 5:
				matrix[x][y][0] = pixels[col,4][0] 
				matrix[x][y][1] = pixels[col,4][1] 
				matrix[x][y][2] = pixels[col,4][2]			
			elif x == col and y == 6:
				matrix[x][y][0] = pixels[col,3][0] 
				matrix[x][y][1] = pixels[col,3][1] 
				matrix[x][y][2] = pixels[col,3][2]	
			elif x == col and y == 7:
				matrix[x][y][0] = pixels[col,2][0] 
				matrix[x][y][1] = pixels[col,2][1] 
				matrix[x][y][2] = pixels[col,2][2]	
			elif x == col and y == 8:
				matrix[x][y][0] = pixels[col,1][0] 
				matrix[x][y][1] = pixels[col,1][1] 
				matrix[x][y][2] = pixels[col,1][2]
			elif x == col and y == 9:
				matrix[x][y][0] = pixels[col,0][0] 
				matrix[x][y][1] = pixels[col,0][1] 
				matrix[x][y][2] = pixels[col,0][2]
				
				#Column 9
			col = 9
			if x == col and y == 0:
				matrix[x][y][0] = pixels[col,9][0] 
				matrix[x][y][1] = pixels[col,9][1] 
				matrix[x][y][2] = pixels[col,9][2]			
			elif x == col and y == 1:
				matrix[x][y][0] = pixels[col,8][0] 
				matrix[x][y][1] = pixels[col,8][1] 
				matrix[x][y][2] = pixels[col,8][2]	
			elif x == col and y == 2:
				matrix[x][y][0] = pixels[col,7][0] 
				matrix[x][y][1] = pixels[col,7][1] 
				matrix[x][y][2] = pixels[col,7][2]	
			elif x == col and y == 3:
				matrix[x][y][0] = pixels[col,6][0] 
				matrix[x][y][1] = pixels[col,6][1] 
				matrix[x][y][2] = pixels[col,6][2]
			elif x == col and y == 4:
				matrix[x][y][0] = pixels[col,5][0] 
				matrix[x][y][1] = pixels[col,5][1] 
				matrix[x][y][2] = pixels[col,5][2]
			if x == col and y == 5:
				matrix[x][y][0] = pixels[col,4][0] 
				matrix[x][y][1] = pixels[col,4][1] 
				matrix[x][y][2] = pixels[col,4][2]			
			elif x == col and y == 6:
				matrix[x][y][0] = pixels[col,3][0] 
				matrix[x][y][1] = pixels[col,3][1] 
				matrix[x][y][2] = pixels[col,3][2]	
			elif x == col and y == 7:
				matrix[x][y][0] = pixels[col,2][0] 
				matrix[x][y][1] = pixels[col,2][1] 
				matrix[x][y][2] = pixels[col,2][2]	
			elif x == col and y == 8:
				matrix[x][y][0] = pixels[col,1][0] 
				matrix[x][y][1] = pixels[col,1][1] 
				matrix[x][y][2] = pixels[col,1][2]
			elif x == col and y == 9:
				matrix[x][y][0] = pixels[col,0][0] 
				matrix[x][y][1] = pixels[col,0][1] 
				matrix[x][y][2] = pixels[col,0][2]


	#print "Displaying..."
	for x in range(0, 10):
		for y in range(0, 10):	
			rgb[0] = matrix[x][y][0]
			rgb[1] = matrix[x][y][1]
			rgb[2] = matrix[x][y][2]
			spidev.write(rgb)
								
	spidev.flush()		
	
