#########################################
#I will not beable to test this class
#until I get back to golden, so I 
#cant promise it will work, but it should
#in theory
#########################################
import time
import sys

#Stops python from generating a .pyc file
sys.dont_write_bytecode = True

#First effect finished. Loops through each LED turning it 
#on then off after a short delay.
class loopAndBlink():
	def loopAndBlinkFunc(self,cube):
		for x in range(4):
			for y in range(4):
				for z in range(4):
					#cube[x,y,z].on()

					#remove this later
					print(cube[x][y][z].getPins())
					time.sleep(.1)
					print(cube[x][y][z].getPins())

					#cube[x,y,z].off()
					
