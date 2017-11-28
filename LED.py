import RPi.GPIO as IO
import sys


#stops vim from generating a .pyc file
sys.dont_write_bytecode = True

#Class to house the LED objects. Each led in the cube will have
#its own LED object, therefor 64 LED objects per cube
class LED():
	def __init__(self,pinRow,pinCol):
		self.pinRow=pinRow
		self.pinCol=pinCol
		self.isOn = False
		
		
	#Turns on the LED accessing the Rasp pi	
	def on(self):
		self.isOn = True
		IO.output(self.pinRow,0)
		IO.output(self.pinCol,1)

	#Turns off the LED accessing the Rasp pi	
	def off(self):
		self.isOn = False
	        IO.output(self.pinRow,1)
	        IO.output(self.pinCol,0)

	#returns if the LED is on or off. Will be usefull for
	#debugging and building new effects
	def getIsOn(self):
		return self.isOn

	#Returns an array in the form of [pinRow, pinCol]
	#again will be usefull for debugging
	def getPins(self):
		return [self.pinRow,self.pinCol]
