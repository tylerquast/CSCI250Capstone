#import RPi.GPIO as IO
class LED():
	def __init__(self,pinRow,pinCol):
		self.pinRow=pinRow
		self.pinCol=pinCol
		self.isOn = False
		
		
	#Turns on the LED accessing the Rasp pi	
	def on(self):
		self.isOn = True
		#IO.output(self.pinRow,0)
		#IO.output(self.pinCol,1)

	#Turns off the LED accessing the Rasp pi	
	def off(self):
		self.isOn = False
	#	IO.output(self.pinRow,1)
	#	IO.output(self.pinCol,0)

	def getIsOn(self):
		return self.isOn

	def getPins(self):
		return [self.pinRow,self.pinCol]
