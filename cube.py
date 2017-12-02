import sys
from LED import *
import numpy as np

#Stops vim from generating a .pyc file
sys.dont_write_bytecode = True


####################################
#TODO: add the tmp LEDs to the array 
#      to create an array of LED 
#      objects to represent the cube
#
#      I need to google this because
#      the 3d numpy array expects
#      numbers only. but im on a 
#      fuckin plane rn LLLLMMMMAAAAAAAAOOOOOOOOOO
#################################### 
class cube():
	def __init__(self):
		#Creats a 2d array of values corresponding to where 
		#the cols are plugged into the rasp pi
		self.colArray = np.zeros((4,4))	
		self.colArray = [[19,26,14,15],
				 [11,5,6,13],
				 [27,22,10,9],
				 [2,3,4,17]]

	def buildCube(self):
		#Creats a 4x4x4 array to store all the 
 		#LED objects and represent the cube
		#all the led pins are initially set to 
		#1,1 which will be changed later
		LedArray = [[[LED(1,1) for i in range(4)] for j in range(4)] for k in range(4)]
		

		#A tripple nested for loop where z represents
		#what row (Height) we are on, and x and y are 
		#the coordinate positions of the LED we are 
		#currently creating.
		#
		#*Note: the commented number in each if
		#represents the GPIO of the row we are on.
		for x in range(4):
			for y in range(4):
				for z in range(4):
					if(x == 0):
						LedArray[x][y][z]=LED(24,self.colArray[y][z])
						#24
					elif(x == 1):
						LedArray[x][y][z]=LED(23,self.colArray[y][z])
						#23
					elif(x == 2):
						LedArray[x][y][z]=LED(18,self.colArray[y][z])
						#18
					elif(x == 3):
						LedArray[x][y][z]=LED(21,self.colArray[y][z])
						#21

		#return the created array of LED Objects
		return LedArray 
