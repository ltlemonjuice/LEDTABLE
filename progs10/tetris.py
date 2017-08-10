#!/usr/bin/env python
#coding: utf8
import time
import array
import random
import sys
import select
import numpy
import functions
import threading
import fcntl

# Open SPI device
spidev = file("/dev/spidev0.0", "wb")
#byte array to store rgb values
rgb=bytearray(3)
#setting spi frequency to 400kbps
fcntl.ioctl(spidev, 0x40046b04, array.array('L', [400000]))

#creating 10x10 matrix
matrix = [[[0 for x in range(3)] for x in range(10)] for x in range(10)]
cmatrix = [[[0 for x in range(3)] for x in range(10)] for x in range(10)]


#Define Functions for Allocation and Display
def allocate():
	#gleich wie bei imgdisp.py, wird einfach noch gespiegelt
	#damit punkt 0/0 am linken oberen rand ist
	for x in range(0, 10):
		for y in range(0, 10):
			cmatrix[x][y][0] = matrix[x][y][0]
			cmatrix[x][y][1] = matrix[x][y][1]
			cmatrix[x][y][2] = matrix[x][y][2]

	#Column 1
	for x in range(1, 10, 2):
		for y in range(0, 10):
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
	print(cmatrix)
	for x in range(0, 10):
		for y in range(0, 10):
			rgb[0] = cmatrix[x][y][0]
			rgb[1] = cmatrix[x][y][1]
			rgb[2] = cmatrix[x][y][2]
			spidev.write(rgb)

	spidev.flush()



def clearMatrix():
	for x in range(0, 10):
		for y in range(0, 10):
			matrix[x][y][0] = 0
			matrix[x][y][1] = 0
			matrix[x][y][2] = 0

def setColor(x, y, color):
    matrix[x][y][0] = color[0]
    matrix[x][y][1] = color[1]
    matrix[x][y][2] = color[2]

def checkInput():
	try:
		if select.select([sys.stdin], [], [], 0)[0]:
			input = sys.stdin.readline().strip()

		if input == "left":
			game.current.left()
		elif input == "turn":
			game.current.turn()
		elif input == "right":
			game.current.right()
		elif input == "down":
			game.current.down()
		elif input == "exit":
			pass
		else:
			print "no valid command"
	except:
		pass




class game:
	current = None
	pieces = []
	finished = False

	def __init__(self):
		print("**Initiated Tetris**")
		self.current = self.getNew()
		self.update()


	def reset(self):
		clearMatrix()
		self.finished = False
		self.pieces = []
		self.current = self.getNew()
		self.update()

	def cleanPieces(self):
		for piece in self.pieces:
			if piece.blocks==[]:
				self.removePiece(piece)
				print("piece cleaned")

	def getNew(self):
		a = random.randint(0, 6)
		if a == 0:
			Quad()
		elif a == 1:
			SShape1()
		elif a == 2:
			SShape2()
		elif a == 3:
			LShape1()
		elif a == 4:
			LShape2()
		elif a == 5:
			Stick()
		elif a == 6:
			EShape()

	def paintPiece(self, piece):
		for block in piece.blocks:
			if (0 <= block[0] <= 9) and (0 <= block[1] <= 9):
				setColor(block[0], block[1], piece.color)

	def getPiece(self, x, y):
		for piece in self.pieces:
			for block in piece.blocks:
			    if block[0] == x and block[1] == y:
			        return piece
		return None

	def freeSquare(self, x, y):
		if self.getPiece(x, y):
			return False  # Square occupied
		else:
			return True  # Square free!

	def removePiece(self, piece):
		self.pieces.remove(piece)

	def addPiece(self, piece):
		self.pieces.append(piece)

	def checkEnd(self):
		if not self.current == None:
			if self.current.collided and self.current.y <= 1:
				print("GAME OVER!")
				return True
			return False

	def endAnimation(self):
		red = (255, 0, 0)
		for i in range(0, 10):
			for v in range (0, 10):
				setColor(i, v, red)
			display()
			time.sleep(0.0001)

	def removeRow(self, row):
		white = (255, 255, 255)
		for i in range(0, 10):
			setColor(i, row, white)
			piece = self.getPiece(i, row)
			piece.remBlock(i, row) #delete all blocks in row from pieces
		display()
		#readjust Board
		for piece in self.pieces:
			for block in piece.blocks:
				if block[1] < row and not piece==self.current:
					block[1] +=1


	def checkRows(self):
		count = 0

		for v in range(1, 10):
			for i in range(0, 10):
				if self.getPiece(i, v) == None:
					count = 0
					break
				else:
					count += 1

				if count == 10:
					print("Full Row")
					self.removeRow(v)
					count = 0

	def update(self):
		if self.checkEnd():
			self.endAnimation()
			#self.finished = True
			time.sleep(1)
			game.reset()
		else:


			if not self.current == None and self.current.collided:
				self.getNew()

			if not self.current == self.pieces[-1]:
				self.current = self.pieces[-1]
				self.checkRows()
				self.cleanPieces()

			clearMatrix()

			for piece in self.pieces:
				self.paintPiece(piece)
			display()





class Shape:
	color = []
	turnState = 0
	maxTurn = 1
	collided = False
	x = 4
	y = 0
	timer = None


	def __init__(self):
		game.pieces.append(self)
		self.updateBlocks()




	def updateBlocks(self):
		self.blocks = [x, y]

	def remBlock(self, x, y):
		for block in self.blocks:
			if block[0] == x and block[1] == y:
				self.blocks.remove(block)

	def checkBounds(self, x, y):
		if (0 <= x <= 9) and (0 <= y <= 9):
			return True
		return False

	def getDownBlocks(self):
		blockies= []
		for block in self.blocks:
			if not game.getPiece(block[0], block[1]+1) == self:
				blockies.append(block)
		return blockies

	def getLeftBlocks(self):
		blockies= []
		for block in self.blocks:
			if not game.getPiece(block[0]-1, block[1]) == self:
				blockies.append(block)
		return blockies

	def getRightBlocks(self):
		blockies= []
		for block in self.blocks:
			if not game.getPiece(block[0]+1, block[1]) == self:
				blockies.append(block)
		return blockies

	def getTurnBlocks(self):
		self.turnState += 1
		self.updateBlocks()
		blockies = self.blocks
		self.turnState -= 1
		self.updateBlocks()
		return blockies


	def checkDown(self):
		for block in self.getDownBlocks():
			if not game.freeSquare(block[0], block[1]+1) or not self.checkBounds(block[0], block[1]+1):
				return False
		return True

	def checkLeft(self):
		for block in self.getLeftBlocks():
			if not game.freeSquare(block[0]-1, block[1]) or not self.checkBounds(block[0]-1, block[1]):
				return False
		return True

	def checkRight(self):
		for block in self.getRightBlocks():
			if not game.freeSquare(block[0]+1, block[1]) or not self.checkBounds(block[0]+1, block[1]):
				return False
		return True

	def checkTurn(self):
			for block in self.getTurnBlocks():
				if (not game.getPiece(block[0], block[1]) == self and not game.freeSquare(block[0], block[1])):
					return False
				if not self.checkBounds(block[0], block[1]):
					return False
			return True


	def turn(self):
		if self.checkTurn():
			if self.turnState == self.maxTurn:
				self.turnState = 0
			else:
				self.turnState += 1
			self.updateBlocks()
			game.update()
			return True
		return False

	def down(self):
		if self.checkDown():
			self.y += 1
			self.updateBlocks()
			game.update()
			return True
		else:
			self.collided = True
			game.update()
			return True

		return False

	def left(self):
		if self.checkLeft():
			self.x -= 1
			self.updateBlocks()
			game.update()
			return True
		return False

	def right(self):
		if self.checkRight():
			self.x += 1
			self.updateBlocks()
			game.update()
			return True
		return False




class Quad(Shape):
	color = [255,255,0] #Yellow
	maxTurn = 0

	def updateBlocks(self):
		self.blocks = [[self.x,self.y],[self.x+1,self.y],[self.x+1,self.y-1],[self.x,self.y-1]]

	def turn(self):
		pass #since Quad, turn = no turn

class SShape1(Shape):
	color = [0,0,255] #Blue
	maxTurn = 1

	def updateBlocks(self):
		if self.turnState == 0:
			self.blocks = [[self.x,self.y],[self.x+1,self.y],[self.x+1,self.y+1],[self.x,self.y-1]]
		if self.turnState == 1:
			self.blocks = [[self.x,self.y],[self.x+1,self.y],[self.x,self.y+1],[self.x-1,self.y+1]]

class SShape2(Shape):
	color = [0,0,255] #Blue
	maxTurn = 1

	def updateBlocks(self):
		if self.turnState == 0:
			self.blocks = [[self.x,self.y],[self.x-1,self.y],[self.x-1,self.y+1],[self.x,self.y-1]]
		if self.turnState == 1:
			self.blocks = [[self.x,self.y],[self.x+1,self.y],[self.x,self.y-1],[self.x-1,self.y-1]]

class LShape1(Shape):
	color = [0,255,0] #Green
	maxTurn = 3

	def updateBlocks(self):
		if self.turnState == 0:
			self.blocks = [[self.x,self.y],[self.x-1,self.y-1],[self.x,self.y-1],[self.x,self.y+1]]
		if self.turnState == 1:
			self.blocks = [[self.x,self.y],[self.x+1,self.y],[self.x+1,self.y-1],[self.x-1,self.y]]
		if self.turnState == 2:
			self.blocks = [[self.x,self.y],[self.x,self.y-1],[self.x,self.y+1],[self.x+1,self.y+1]]
		if self.turnState == 3:
			self.blocks = [[self.x,self.y],[self.x-1,self.y+1],[self.x-1,self.y],[self.x+1,self.y]]

class LShape2(Shape):
	color = [0,255,0] #Green
	maxTurn = 3

	def updateBlocks(self):
		if self.turnState == 0:
			self.blocks = [[self.x,self.y],[self.x+1,self.y-1],[self.x,self.y-1],[self.x,self.y+1]]
		if self.turnState == 1:
			self.blocks = [[self.x,self.y],[self.x+1,self.y],[self.x+1,self.y+1],[self.x-1,self.y]]
		if self.turnState == 2:
			self.blocks = [[self.x,self.y],[self.x,self.y-1],[self.x,self.y+1],[self.x-1,self.y+1]]
		if self.turnState == 3:
			self.blocks = [[self.x,self.y],[self.x-1,self.y-1],[self.x-1,self.y],[self.x+1,self.y]]

class Stick(Shape):
	color = [255,0,0] #Red
	maxTurn = 1

	def updateBlocks(self):
		if self.turnState == 0:
			self.blocks = [[self.x,self.y],[self.x,self.y-1],[self.x,self.y+1],[self.x,self.y+2]]
		if self.turnState == 1:
			self.blocks = [[self.x,self.y],[self.x-1,self.y],[self.x+1,self.y],[self.x+2,self.y]]

class EShape(Shape):
	color = [0,255,255] #Cyan
	maxTurn = 3

	def updateBlocks(self):
		if self.turnState == 0:
			self.blocks = [[self.x,self.y],[self.x-1,self.y],[self.x,self.y-1],[self.x+1,self.y]]
		if self.turnState == 1:
			self.blocks = [[self.x,self.y],[self.x+1,self.y],[self.x,self.y-1],[self.x,self.y+1]]
		if self.turnState == 2:
			self.blocks = [[self.x,self.y],[self.x,self.y+1],[self.x+1,self.y],[self.x-1,self.y]]
		if self.turnState == 3:
			self.blocks = [[self.x,self.y],[self.x-1,self.y],[self.x,self.y+1],[self.x,self.y-1]]







#MAIN
clearMatrix()
game = game()

#game.endAnimation()
def timer():
	try:
		game.current.down()
		threading.Timer(0.5, timer).start()
	except:
		threading.Timer(0.5, timer).start()

timer()
#Startpoint
while not checkInput == "exit":
	checkInput()


#@!fold-children
