#!/usr/bin/env python
import time
import array
import fcntl
import random
import sys
import select
from imgdisp import imgdisp

# Open SPI device
spidev = file("/dev/spidev0.0", "wb")
#byte array to store rgb values
rgb=bytearray(3)
#setting spi frequency to 400kbps
fcntl.ioctl(spidev, 0x40046b04, array.array('L', [400000]))

#creating 10x10 matrix (last object may not be used)
matrix = [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]
			
cmatrix = [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]
			


			

#Define Functions for Allocation and Display
def allocate():

	for x in range(0,10):
		for y in range (0,10):
			cmatrix[x][y][0] = matrix[x][y][0] 
			cmatrix[x][y][1] = matrix[x][y][1] 
			cmatrix[x][y][2] = matrix[x][y][2]
			
			#Column 1
			col = 1
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1] 
				cmatrix[x][y][2] = matrix[col][9][2]			
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]			
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]	
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]	
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]
				
				#Column 3
			col = 3
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1] 
				cmatrix[x][y][2] = matrix[col][9][2]			
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]			
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]	
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]	
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]
				
				#Column 5
			col = 5
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1] 
				cmatrix[x][y][2] = matrix[col][9][2]			
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]			
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]	
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]	
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]
			
			#Column 7
			col = 7
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1] 
				cmatrix[x][y][2] = matrix[col][9][2]			
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]			
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]	
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]	
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]
				
				#Column 9
			col = 9
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1] 
				cmatrix[x][y][2] = matrix[col][9][2]			
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]			
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]	
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]	
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]
				
	cmatrix.reverse()
				
def display():
	#allocating
	allocate()
	for x in range(0, 10):
		for y in range(0, 10):	
			rgb[0] = cmatrix[x][y][0]
			rgb[1] = cmatrix[x][y][1]
			rgb[2] = cmatrix[x][y][2]
			spidev.write(rgb)
								
	spidev.flush()
	

class Data:
	posX = 0
	posY = 0
	delay = .25

#Figures Classes	
class Quad:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.blocks = [[self.x,self.y],[self.x+1,self.y],[self.x+1,self.y+1],[self.x,self.y+1]]

		self.color = [255,255,0] #Yellow
	
	def turn(self):
		return None
	
	def delOld(self):
		matrix[self.blocks[0][0]][self.blocks[0][1]] = [0,0,0]
		matrix[self.blocks[1][0]][self.blocks[1][1]] = [0,0,0]
		matrix[self.blocks[2][0]][self.blocks[2][1]] = [0,0,0]
		matrix[self.blocks[3][0]][self.blocks[3][1]] = [0,0,0]
	
	def paint(self):
		if self.x+1 <= 9 and self.y+1 <= 9:
			self.delOld()
			self.blocks = [[self.x,self.y],[self.x+1,self.y],[self.x+1,self.y+1],[self.x,self.y+1]]
			
			matrix[self.blocks[0][0]][self.blocks[0][1]] = self.color
			matrix[self.blocks[1][0]][self.blocks[1][1]] = self.color
			matrix[self.blocks[2][0]][self.blocks[2][1]] = self.color
			matrix[self.blocks[3][0]][self.blocks[3][1]] = self.color
			display()
		else:
			return None
		return None
		
		
class SShape1:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.turnState = 0
		self.color = [0,0,255] #Blue
		self.blocks1 = [[self.x,self.y],[self.x+1,self.y],[self.x+1,self.y+1],[self.x,self.y-1]]
		self.blocks2 = [[self.x,self.y],[self.x+1,self.y],[self.x,self.y+1],[self.x-1,self.y+1]]
		
		
	def turn(self):
		if self.turnState == 0:
			self.turnState = 1
			self.delOld(self.blocks1)
		elif self.turnState == 1:
			self.turnState = 0
			self.delOld(self.blocks2)
		return None
	
	def delOld(self, blocks):
		matrix[blocks[0][0]][blocks[0][1]] = [0,0,0] 
		matrix[blocks[1][0]][blocks[1][1]] = [0,0,0]
		matrix[blocks[2][0]][blocks[2][1]] = [0,0,0]
		matrix[blocks[3][0]][blocks[3][1]] = [0,0,0]
	
	def paint(self):
		if self.x+1 <= 9 and self.y+1 <= 9:
			if self.turnState == 0:
				self.delOld(self.blocks1)
				self.blocks1 = [[self.x,self.y],[self.x+1,self.y],[self.x+1,self.y+1],[self.x,self.y-1]]
				
				matrix[self.blocks1[0][0]][self.blocks1[0][1]] = self.color
				matrix[self.blocks1[1][0]][self.blocks1[1][1]] = self.color
				matrix[self.blocks1[2][0]][self.blocks1[2][1]] = self.color
				matrix[self.blocks1[3][0]][self.blocks1[3][1]] = self.color
				
			elif self.turnState == 1:
				self.delOld(self.blocks2)
				self.blocks2 = [[self.x,self.y],[self.x+1,self.y],[self.x,self.y+1],[self.x-1,self.y+1]]
				
				matrix[self.blocks2[0][0]][self.blocks2[0][1]] = self.color
				matrix[self.blocks2[1][0]][self.blocks2[1][1]] = self.color
				matrix[self.blocks2[2][0]][self.blocks2[2][1]] = self.color
				matrix[self.blocks2[3][0]][self.blocks2[3][1]] = self.color
			
			display()
			

class SShape2:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.turnState = 0
		self.color = [0,0,255] #Blue
		self.blocks1 = [[self.x,self.y],[self.x-1,self.y],[self.x-1,self.y+1],[self.x,self.y-1]]
		self.blocks2 = [[self.x,self.y],[self.x+1,self.y],[self.x,self.y-1],[self.x-1,self.y-1]]
		
		
	def turn(self):
		if self.turnState == 0:
			self.turnState = 1
			self.delOld(self.blocks1)
		elif self.turnState == 1:
			self.turnState = 0
			self.delOld(self.blocks2)
		return None
	
	def delOld(self, blocks):
		matrix[blocks[0][0]][blocks[0][1]] = [0,0,0] 
		matrix[blocks[1][0]][blocks[1][1]] = [0,0,0]
		matrix[blocks[2][0]][blocks[2][1]] = [0,0,0]
		matrix[blocks[3][0]][blocks[3][1]] = [0,0,0]
	
	def paint(self):
		if self.x+1 <= 9 and self.y+1 <= 9:
			if self.turnState == 0:
				self.delOld(self.blocks1)
				self.blocks1 = [[self.x,self.y],[self.x-1,self.y],[self.x-1,self.y+1],[self.x,self.y-1]]
				
				matrix[self.blocks1[0][0]][self.blocks1[0][1]] = self.color
				matrix[self.blocks1[1][0]][self.blocks1[1][1]] = self.color
				matrix[self.blocks1[2][0]][self.blocks1[2][1]] = self.color
				matrix[self.blocks1[3][0]][self.blocks1[3][1]] = self.color
				
			elif self.turnState == 1:
				self.delOld(self.blocks2)
				self.blocks2 = [[self.x,self.y],[self.x+1,self.y],[self.x,self.y-1],[self.x-1,self.y-1]]
				
				matrix[self.blocks2[0][0]][self.blocks2[0][1]] = self.color
				matrix[self.blocks2[1][0]][self.blocks2[1][1]] = self.color
				matrix[self.blocks2[2][0]][self.blocks2[2][1]] = self.color
				matrix[self.blocks2[3][0]][self.blocks2[3][1]] = self.color
			
			display()
		

class LShape1:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.turnState = 0
		self.color = [0,255,0] #Green
		self.blocks1 = [[self.x,self.y],[self.x-1,self.y-1],[self.x,self.y-1],[self.x,self.y+1]]
		self.blocks2 = [[self.x,self.y],[self.x+1,self.y],[self.x+1,self.y-1],[self.x-1,self.y]]
		self.blocks3 = [[self.x,self.y],[self.x,self.y-1],[self.x,self.y+1],[self.x+1,self.y+1]]
		self.blocks4 = [[self.x,self.y],[self.x-1,self.y-1],[self.x-1,self.y],[self.x+1,self.y]]
		
		
	def turn(self):
		if self.turnState == 0:
			self.turnState = 1
			self.delOld(self.blocks1)
		elif self.turnState == 1:
			self.turnState = 2
			self.delOld(self.blocks2)
		elif self.turnState == 2:
			self.turnState = 3
			self.delOld(self.blocks3)
		elif self.turnState == 3:
			self.turnState = 0
			self.delOld(self.blocks4)
		return None
	
	def delOld(self, blocks):
		matrix[blocks[0][0]][blocks[0][1]] = [0,0,0] 
		matrix[blocks[1][0]][blocks[1][1]] = [0,0,0]
		matrix[blocks[2][0]][blocks[2][1]] = [0,0,0]
		matrix[blocks[3][0]][blocks[3][1]] = [0,0,0]
	
	def paint(self):
		if self.x+1 <= 9 and self.y+1 <= 9:
			if self.turnState == 0:
				self.delOld(self.blocks1)
				self.blocks1 = [[self.x,self.y],[self.x-1,self.y-1],[self.x,self.y-1],[self.x,self.y+1]]
				
				matrix[self.blocks1[0][0]][self.blocks1[0][1]] = self.color
				matrix[self.blocks1[1][0]][self.blocks1[1][1]] = self.color
				matrix[self.blocks1[2][0]][self.blocks1[2][1]] = self.color
				matrix[self.blocks1[3][0]][self.blocks1[3][1]] = self.color
				
			elif self.turnState == 1:
				self.delOld(self.blocks2)
				self.blocks2 = [[self.x,self.y],[self.x+1,self.y],[self.x+1,self.y-1],[self.x-1,self.y]]
				
				matrix[self.blocks2[0][0]][self.blocks2[0][1]] = self.color
				matrix[self.blocks2[1][0]][self.blocks2[1][1]] = self.color
				matrix[self.blocks2[2][0]][self.blocks2[2][1]] = self.color
				matrix[self.blocks2[3][0]][self.blocks2[3][1]] = self.color
			
			elif self.turnState == 2:
				self.delOld(self.blocks3)
				self.blocks3 = [[self.x,self.y],[self.x,self.y-1],[self.x,self.y+1],[self.x+1,self.y+1]]				
				
				matrix[self.blocks3[0][0]][self.blocks3[0][1]] = self.color
				matrix[self.blocks3[1][0]][self.blocks3[1][1]] = self.color
				matrix[self.blocks3[2][0]][self.blocks3[2][1]] = self.color
				matrix[self.blocks3[3][0]][self.blocks3[3][1]] = self.color
				
			elif self.turnState == 3:
				self.delOld(self.blocks4)
				self.blocks4 = [[self.x,self.y],[self.x-1,self.y-1],[self.x-1,self.y],[self.x+1,self.y]]
				
				matrix[self.blocks4[0][0]][self.blocks4[0][1]] = self.color
				matrix[self.blocks4[1][0]][self.blocks4[1][1]] = self.color
				matrix[self.blocks4[2][0]][self.blocks4[2][1]] = self.color
				matrix[self.blocks4[3][0]][self.blocks4[3][1]] = self.color
			
			display()


class LShape2:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.turnState = 0
		self.color = [0,255,0] #Green
		self.blocks1 = [[self.x,self.y],[self.x+1,self.y-1],[self.x,self.y-1],[self.x,self.y+1]]
		self.blocks2 = [[self.x,self.y],[self.x+1,self.y],[self.x+1,self.y-1],[self.x-1,self.y]]
		self.blocks3 = [[self.x,self.y],[self.x,self.y-1],[self.x,self.y+1],[self.x+1,self.y+1]]
		self.blocks4 = [[self.x,self.y],[self.x-1,self.y-1],[self.x-1,self.y],[self.x+1,self.y]]
		
		
	def turn(self):
		if self.turnState == 0:
			self.turnState = 1
			self.delOld(self.blocks1)
		elif self.turnState == 1:
			self.turnState = 2
			self.delOld(self.blocks2)
		elif self.turnState == 2:
			self.turnState = 3
			self.delOld(self.blocks3)
		elif self.turnState == 3:
			self.turnState = 0
			self.delOld(self.blocks4)
		return None
	
	def delOld(self, blocks):
		matrix[blocks[0][0]][blocks[0][1]] = [0,0,0] 
		matrix[blocks[1][0]][blocks[1][1]] = [0,0,0]
		matrix[blocks[2][0]][blocks[2][1]] = [0,0,0]
		matrix[blocks[3][0]][blocks[3][1]] = [0,0,0]
	
	def paint(self):
		if self.x+1 <= 9 and self.y+1 <= 9:
			if self.turnState == 0:
				self.delOld(self.blocks1)
				self.blocks1 = [[self.x,self.y],[self.x+1,self.y-1],[self.x,self.y-1],[self.x,self.y+1]]
				
				matrix[self.blocks1[0][0]][self.blocks1[0][1]] = self.color
				matrix[self.blocks1[1][0]][self.blocks1[1][1]] = self.color
				matrix[self.blocks1[2][0]][self.blocks1[2][1]] = self.color
				matrix[self.blocks1[3][0]][self.blocks1[3][1]] = self.color
				
			elif self.turnState == 1:
				self.delOld(self.blocks2)
				self.blocks2 = [[self.x,self.y],[self.x+1,self.y],[self.x+1,self.y-1],[self.x-1,self.y]]
				
				matrix[self.blocks2[0][0]][self.blocks2[0][1]] = self.color
				matrix[self.blocks2[1][0]][self.blocks2[1][1]] = self.color
				matrix[self.blocks2[2][0]][self.blocks2[2][1]] = self.color
				matrix[self.blocks2[3][0]][self.blocks2[3][1]] = self.color
			
			elif self.turnState == 2:
				self.delOld(self.blocks3)
				self.blocks3 = [[self.x,self.y],[self.x,self.y-1],[self.x,self.y+1],[self.x+1,self.y+1]]				
				
				matrix[self.blocks3[0][0]][self.blocks3[0][1]] = self.color
				matrix[self.blocks3[1][0]][self.blocks3[1][1]] = self.color
				matrix[self.blocks3[2][0]][self.blocks3[2][1]] = self.color
				matrix[self.blocks3[3][0]][self.blocks3[3][1]] = self.color
				
			elif self.turnState == 3:
				self.delOld(self.blocks4)
				self.blocks4 = [[self.x,self.y],[self.x-1,self.y-1],[self.x-1,self.y],[self.x+1,self.y]]
				
				matrix[self.blocks4[0][0]][self.blocks4[0][1]] = self.color
				matrix[self.blocks4[1][0]][self.blocks4[1][1]] = self.color
				matrix[self.blocks4[2][0]][self.blocks4[2][1]] = self.color
				matrix[self.blocks4[3][0]][self.blocks4[3][1]] = self.color
			
			display()
			
			
class Stick:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.turnState = 0
		self.color = [255,0,0] #Red
		self.blocks1 = [[self.x,self.y],[self.x,self.y-1],[self.x,self.y+1],[self.x,self.y+2]]
		self.blocks2 = [[self.x,self.y],[self.x-1,self.y],[self.x+1,self.y],[self.x+2,self.y]]
		
		
	def turn(self):
		if self.turnState == 0:
			self.turnState = 1
			self.delOld(self.blocks1)
		elif self.turnState == 1:
			self.turnState = 0
			self.delOld(self.blocks2)
		
	
	def delOld(self, blocks):
		matrix[blocks[0][0]][blocks[0][1]] = [0,0,0] 
		matrix[blocks[1][0]][blocks[1][1]] = [0,0,0]
		matrix[blocks[2][0]][blocks[2][1]] = [0,0,0]
		matrix[blocks[3][0]][blocks[3][1]] = [0,0,0]
	
	def paint(self):
		if self.turnState == 0 and (self.x <= 9 and self.y+2 <= 9):
			self.delOld(self.blocks1)
			self.blocks1 = [[self.x,self.y],[self.x,self.y-1],[self.x,self.y+1],[self.x,self.y+2]]
			
			matrix[self.blocks1[0][0]][self.blocks1[0][1]] = self.color
			matrix[self.blocks1[1][0]][self.blocks1[1][1]] = self.color
			matrix[self.blocks1[2][0]][self.blocks1[2][1]] = self.color
			matrix[self.blocks1[3][0]][self.blocks1[3][1]] = self.color
		
		elif self.turnState == 1 and (1 <= self.x <= 7 and self.y <= 10):
			self.delOld(self.blocks2)
			self.blocks2 = [[self.x,self.y],[self.x-1,self.y],[self.x+1,self.y],[self.x+2,self.y]]
			
			matrix[self.blocks2[0][0]][self.blocks2[0][1]] = self.color
			matrix[self.blocks2[1][0]][self.blocks2[1][1]] = self.color
			matrix[self.blocks2[2][0]][self.blocks2[2][1]] = self.color
			matrix[self.blocks2[3][0]][self.blocks2[3][1]] = self.color
				
		display()			
			
			
class EShape:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.turnState = 0
		self.color = [0,255,255] #Cyan
		self.blocks1 = [[self.x,self.y],[self.x-1,self.y],[self.x,self.y-1],[self.x+1,self.y]]
		self.blocks2 = [[self.x,self.y],[self.x+1,self.y],[self.x,self.y-1],[self.x,self.y+1]]
		self.blocks3 = [[self.x,self.y],[self.x,self.y+1],[self.x+1,self.y],[self.x-1,self.y]]
		self.blocks4 = [[self.x,self.y],[self.x-1,self.y],[self.x,self.y+1],[self.x,self.y-1]]
		
		
	def turn(self):
		if self.turnState == 0:
			self.turnState = 1
			self.delOld(self.blocks1)
		elif self.turnState == 1:
			self.turnState = 2
			self.delOld(self.blocks2)
		elif self.turnState == 2:
			self.turnState = 3
			self.delOld(self.blocks3)
		elif self.turnState == 3:
			self.turnState = 0
			self.delOld(self.blocks4)
		return None
	
	def delOld(self, blocks):
		matrix[blocks[0][0]][blocks[0][1]] = [0,0,0] 
		matrix[blocks[1][0]][blocks[1][1]] = [0,0,0]
		matrix[blocks[2][0]][blocks[2][1]] = [0,0,0]
		matrix[blocks[3][0]][blocks[3][1]] = [0,0,0]
	
	def paint(self):
		if self.x+1 <= 9 and self.y+1 <= 9:
			if self.turnState == 0:
				self.delOld(self.blocks1)
				self.blocks1 = [[self.x,self.y],[self.x-1,self.y],[self.x,self.y-1],[self.x+1,self.y]]
				
				matrix[self.blocks1[0][0]][self.blocks1[0][1]] = self.color
				matrix[self.blocks1[1][0]][self.blocks1[1][1]] = self.color
				matrix[self.blocks1[2][0]][self.blocks1[2][1]] = self.color
				matrix[self.blocks1[3][0]][self.blocks1[3][1]] = self.color
				
			elif self.turnState == 1:
				self.delOld(self.blocks2)
				self.blocks2 = [[self.x,self.y],[self.x+1,self.y],[self.x,self.y-1],[self.x,self.y+1]]
				
				matrix[self.blocks2[0][0]][self.blocks2[0][1]] = self.color
				matrix[self.blocks2[1][0]][self.blocks2[1][1]] = self.color
				matrix[self.blocks2[2][0]][self.blocks2[2][1]] = self.color
				matrix[self.blocks2[3][0]][self.blocks2[3][1]] = self.color
			
			elif self.turnState == 2:
				self.delOld(self.blocks3)
				self.blocks3 = [[self.x,self.y],[self.x,self.y+1],[self.x+1,self.y],[self.x-1,self.y]]		
				
				matrix[self.blocks3[0][0]][self.blocks3[0][1]] = self.color
				matrix[self.blocks3[1][0]][self.blocks3[1][1]] = self.color
				matrix[self.blocks3[2][0]][self.blocks3[2][1]] = self.color
				matrix[self.blocks3[3][0]][self.blocks3[3][1]] = self.color
				
			elif self.turnState == 3:
				self.delOld(self.blocks4)
				self.blocks4 = [[self.x,self.y],[self.x-1,self.y],[self.x,self.y+1],[self.x,self.y-1]]
				
				matrix[self.blocks4[0][0]][self.blocks4[0][1]] = self.color
				matrix[self.blocks4[1][0]][self.blocks4[1][1]] = self.color
				matrix[self.blocks4[2][0]][self.blocks4[2][1]] = self.color
				matrix[self.blocks4[3][0]][self.blocks4[3][1]] = self.color
			
			display()
			
			
def clearMatrix():
	for x in range(0, 10):
		for y in range(0, 10):	
			matrix[x][y][0] = 0
			matrix[x][y][1] = 0
			matrix[x][y][2] = 0
				

def checkCol():
	return None
	
	
def checkInput(object):
	if select.select([sys.stdin], [], [], 0)[0]:
		input = sys.stdin.readline().strip()
		if input == "left" and 0 < object.x < 9:
			object.x = object.x - 1
		elif input == "turn": 
			object.turn()
		elif input == "right":
			object.x = object.x + 1
		elif input == "down":
			object.y = object.y + 1
		else:
			print "no valid command"
		
	else:
		pass
	
def setMatrix():
	return None
		

def move(object):
	object.y = object.y + 1
	object.paint()
	time.sleep(Data.delay)

def newBlock():
	#rand = random.randint(0,6)
	rand = 5
	clearMatrix()
	
	if rand == 0:
		object = Quad(4,0)
	elif rand == 1:
		object = SShape1(4,0)
	elif rand == 2:
		object = SShape2(4,0)
	elif rand == 3:
		object = LShape1(4,0)
	elif rand == 4:
		object = LShape2(4,0)
	elif rand == 5:
		object = Stick(4,0)
	elif rand == 6:
		object = EShape(4,0)
	
	object.paint()
	return object

	
#MAIN

while True:
	object = newBlock()
	
	for i in range(0,8):
		checkInput(object)
		move(object)
		
	
	
	