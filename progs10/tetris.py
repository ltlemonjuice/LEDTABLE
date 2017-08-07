#!/usr/bin/env python
#coding: utf8
import time, threading
import array
import random
import sys
import select
import numpy
import functions

try:
	from imgdisp import imgdisp
	import fcntl
except:
	pass

rgb=bytearray(3)

try:
	# Open SPI device
	spidev = file("/dev/spidev0.0", "wb")
	#byte array to store rgb values

	#setting spi frequency to 400kbps
	fcntl.ioctl(spidev, 0x40046b04, array.array('L', [400000]))
except:
	pass

#creating 10x10 matrix (last object may not be used)
matrix = [[[0 for x in range(3)] for x in range(10)] for x in range(10)]
#cmatrix = [[[0 for x in range(3)] for x in range(10)] for x in range(10)]


#DATA
posX = 0
posY = 0
delay = 1
global current
global sched
parts = []
colors = []


#@fold-children
#Define global Functions
cmatrix = functions.allocate(matrix)


def display():
	#allocating
	cmatrix = functions.allocate(matrix)
	for x in range(0, 10):
	    for y in range(0, 10):
	        rgb[0] = cmatrix[x][y][0]
	        rgb[1] = cmatrix[x][y][1]
	        rgb[2] = cmatrix[x][y][2]
	        try:
	            spidev.write(rgb)
	        except:
	            pass


	try:
	    spidev.flush()
	except:
	    pass

	f = open("save.matrix", "w+")
	f.write(numpy.array2string(numpy.flipud(numpy.rot90(matrix)), separator=", "))

def clearMatrix():
	for x in range(0, 10):
		for y in range(0, 10):
			matrix[x][y][0] = 0
			matrix[x][y][1] = 0
			matrix[x][y][2] = 0

def checkNegPixel(pixelx, pixely):
	if (pixelx < 0) or (pixely < 0):
		return False
	else:
		return True

def checkPixel(pixel):
	print "Pixels: " + str(pixel)
	if (pixel[0] + pixel[1] + pixel[2]) == 0:
		return True
	else:
		return False

def newBlock():
	#rand = random.randint(0,6)
	rand = 1
	#clearMatrix()

	if rand == 0:
		current = Quad(4,-3)
	elif rand == 1:
		current = SShape1(4,-3)
	elif rand == 2:
		current = SShape2(4,-3)
	elif rand == 3:
		current = LShape1(4,-3)
	elif rand == 4:
		current = LShape2(4,-3)
	elif rand == 5:
		current = Stick(4,-3)
	elif rand == 6:
		current = EShape(4,-3)

	current.paint()
	return current



def move(current):

	sched = threading.Timer(1,move).start()
	if current.checkColl("down", current.turnState):
		current.delOld()
		current.y = current.y + 1
		current.paint()
		display()

		time.sleep(delay)
		return True
	else:
		print ("Collided DOWN")
		newBlock()
		sched
		return False


def right(current):
	if current.checkColl("right", current.turnState):
		current.delOld()

		current.x = current.x + 1
		current.paint()
		display()
		return True
	else:
		print ("Collided RIGHT")
		return False

def left(current):
	if current.checkColl("left", current.turnState):
		current.delOld()
		current.x = current.x - 1
		current.paint()
		display()
		return True
	else:
		print ("Collided LEFT")
		return False

def checkRow():
	return None


def checkInput(current):
	try:
		if select.select([sys.stdin], [], [], 0)[0]:
			input = sys.stdin.readline().strip()
	except:
		input=raw_input("Input: ")

	if input == "left" and 0 < current.x < 9:

		left(current)
	elif input == "turn":
		current.turn()
	elif input == "right":
		right(current)
	elif input == "down":
		current.y = current.y + 1
	else:
		print "no valid command"












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



	def checkColl(self, direction, turn):
		self.blocks1 = [[self.x,self.y],[self.x+1,self.y],[self.x+1,self.y+1],[self.x,self.y-1]]
		self.blocks2 = [[self.x,self.y],[self.x+1,self.y],[self.x,self.y+1],[self.x-1,self.y+1]]

		if direction == "down":
			if turn == 0:
				print("DOWN 0")
				if checkPixel(matrix[(self.blocks1[0][0])][(self.blocks1[0][1])+1]) and checkPixel(matrix[(self.blocks1[0][0])+1][(self.blocks1[0][1])+2]):
					return True
				else:
					return False
			elif turn == 1:
				if checkPixel(matrix[self.blocks1[0][0]][(self.blocks1[0][1])+2]) and checkPixel(matrix[(self.blocks1[0][0])+1][(self.blocks1[0][1])+1]) and checkPixel(matrix[(self.blocks1[0][0])-1][(self.blocks1[0][1])+2]):
					return True
				else:
					return False
		elif direction == "left":
			if turn == 0:
				if checkPixel(matrix[(self.blocks1[0][0])-1][(self.blocks1[0][1])-1]) and checkPixel(matrix[(self.blocks1[0][0])-1][self.blocks1[0][1]]) and checkPixel(matrix[self.blocks1[0][0]][(self.blocks1[0][1])+1]):
					return True
				else:
					return False
			elif turn == 1:
				if checkPixel(matrix[(self.blocks1[0][0])-1][self.blocks1[0][1]]) and checkPixel(matrix[(self.blocks1[0][0])-2][self.blocks1[0][1]]):
					return True
				else:
					return False
		elif direction == "right":
			if turn == 0:
				if checkPixel(matrix[(self.blocks1[0][0])-1][(self.blocks1[0][1])-1]) and checkPixel(matrix[(self.blocks1[0][0])-1][self.blocks1[0][1]]) and checkPixel(matrix[self.blocks1[0][0]][(self.blocks1[0][1])+1]):
					return True
				else:
					return False
			elif turn == 1:
				if checkPixel(matrix[(self.blocks1[0][0])-1][self.blocks1[0][1]]) and checkPixel(matrix[(self.blocks1[0][0])-2][self.blocks1[0][1]]):
					return True
				else:
					return False
		else:
			pass

	def turn(self):
		if self.turnState == 0:
			#checkColl(1)
			self.delOld()
			self.turnState = 1

		elif self.turnState == 1:
			self.delOld()
			self.turnState = 0

		return None



	def delOld(self):
		if self.turnState == 0:
			blocks = self.blocks1
		elif self.turnState == 1:
			blocks = self.blocks2

		matrix[blocks[0][0]][blocks[0][1]] = [0,0,0]
		matrix[blocks[1][0]][blocks[1][1]] = [0,0,0]
		matrix[blocks[2][0]][blocks[2][1]] = [0,0,0]
		matrix[blocks[3][0]][blocks[3][1]] = [0,0,0]



	def paint(self):
		if (0 <= self.x+1 <= 9) and (0 <= self.y+1 <= 9):
			if self.turnState == 0:
				self.delOld()
				self.blocks1 = [[self.x,self.y],[self.x+1,self.y],[self.x+1,self.y+1],[self.x,self.y-1]]


				if checkNegPixel(self.blocks1[0][0],self.blocks1[0][1]):
					matrix[self.blocks1[0][0]][self.blocks1[0][1]] = self.color
				if checkNegPixel(self.blocks1[1][0],self.blocks1[1][1]):
					matrix[self.blocks1[1][0]][self.blocks1[1][1]] = self.color
				if checkNegPixel(self.blocks1[2][0],self.blocks1[2][1]):
					matrix[self.blocks1[2][0]][self.blocks1[2][1]] = self.color
				if checkNegPixel(self.blocks1[3][0],self.blocks1[3][1]):
					matrix[self.blocks1[3][0]][self.blocks1[3][1]] = self.color

				count = 0
				for i in range(0,len(matrix)):
					if checkPixel(matrix[i]):
						count = count + 1

				print("%d active Pixels" % count)



			elif self.turnState == 1:
				self.delOld()
				self.blocks2 = [[self.x,self.y],[self.x+1,self.y],[self.x,self.y+1],[self.x-1,self.y+1]]

				matrix[self.blocks2[0][0]][self.blocks2[0][1]] = self.color
				matrix[self.blocks2[1][0]][self.blocks2[1][1]] = self.color
				matrix[self.blocks2[2][0]][self.blocks2[2][1]] = self.color
				matrix[self.blocks2[3][0]][self.blocks2[3][1]] = self.color






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







#MAIN
#while True:
print("**Initiated Tetris**")

	#while True:
clearMatrix()
current = newBlock()
matrix[5][7][0] = 255

for i in range(0,2):
	current = newBlock()
	checkInput(current)
	coll = True

	while coll:
	#	checkInput(current)
		coll = move(current)


"""
current = newBlock()

checkInput(current)

for i in range(0,8):
	checkInput(current)
	"""





#@!fold-children
