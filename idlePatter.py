from loopAndBlink import *
from key import *
from Mphone import *
from turnOff import *
from musicAnalyzer import *
from randomEffect import *
from expandingCube import *
from fallingBlocks import *
from spinner import *
import numpy as np
import random





class idlePattern():
	def idlePatternFunc(self,cube):
		while True:
			choice = random.randint(1,5)
			turnOffer = turnOff()
			turnOffer.turnOffFunc(cube)
			if choice == 1:
				tmp = loopAndBlink()
				tmp.loopAndBlinkFunc(cube)
			if choice == 2:
				tmp = expandingCube()
				tmp.expandingCubeFunc(cube)
			if choice == 3:
				tmp = randomEffect()
				tmp.RandomFunc(cube)
			if choice == 4:
				tmp = fallingBlocks()
				tmp.fallingBlocksFunc(cube)
			if choice == 5:
				tmp = spinner()
				tmp.spinnerFunc(cube)

