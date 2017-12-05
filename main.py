#Uncomment this when moved to rasp pi, I build this initially on my laptop.

import RPi.GPIO as IO
import sys
import time
import random
from LED import *
from cube import *
from loopAndBlink import *
from key import *
from Mphone import *
from turnOff import *
from musicAnalyzer import *
from randomEffect import *
from expandingCube import *
from idlePatter import *
from fallingBlocks import *
from spinner import *
import numpy as np


#stops python from generating a .pyc file
sys.dont_write_bytecode = True






IO.setwarnings(False)

IO.setmode(IO.BCM)

IO.setup(2,IO.OUT)
IO.setup(3,IO.OUT)
IO.setup(4,IO.OUT)
IO.setup(17,IO.OUT)
IO.setup(27,IO.OUT)
IO.setup(22,IO.OUT)
IO.setup(10,IO.OUT)
IO.setup(9,IO.OUT)
IO.setup(11,IO.OUT)
IO.setup(5,IO.OUT)
IO.setup(6,IO.OUT)
IO.setup(13,IO.OUT)
IO.setup(19,IO.OUT)
IO.setup(26,IO.OUT)
IO.setup(14,IO.OUT)
IO.setup(15,IO.OUT)
IO.setup(21,IO.OUT)
IO.setup(18,IO.OUT)
IO.setup(23,IO.OUT)
IO.setup(24,IO.OUT)









#Main Class


#Creates an LED cube Object
cube = cube()

#Fills a 4x4x4 array with LED Objects to represent the cube
#See the 'buildCube' method in cube.py
#All leds are turned off by defualt
cubeArray = cube.buildCube()



#an object that will be used to turn the cube off before and after each effect
turnOffer = turnOff()
turnOffer.turnOffFunc(cubeArray)


#A sparkfun sound detector is used to trigger various 
#effects with claps
#get user to select to either keyboard mode or microphone mode to enter input
mode = raw_input('Select a mode to run the cube in.  To run from the microphone enter "M" and to run from the keyboard enter "k".\nEnter mode: ')

while (mode !='k' and mode !='K' and mode != 'm' and mode != 'M'):
    try:
        print('select valid operation mode')
        mode = raw_input('Select a mode to run the cube in.  To run from the microphone enter "M" and to run from the keyboard enter "k".\nEnter mode: ')
    except TypeError:
        print('select valid operation mode')


choice = 0

#main code to run LED Cube
try:
    #get input from either the keyboard or microphone depending on the user's choice
    while True:

        if (ord(mode) == ord('k') or ord(mode) == ord('K')):
            choice = key()

        elif (ord(mode) == ord('m') or ord(mode) == ord('M')):
            choice = Mphone()

            

        #display what pattern will run and then run that pattern
        print('running pattern',choice,'\n')

        if choice == 0:
            print('no input detected')
        
        elif choice == 1:
                turnOffer.turnOffFunc(cubeArray)
                tmp = loopAndBlink()
                tmp.loopAndBlinkFunc(cubeArray)

        elif choice == 2:
                turnOffer.turnOffFunc(cubeArray)
                tmp = expandingCube()
                tmp.expandingCubeFunc(cubeArray)
        elif choice == 3:
                turnOffer.turnOffFunc(cubeArray)
                tmp = randomEffect()
                tmp.RandomFunc(cubeArray)

        elif choice == 4:
                turnOffer.turnOffFunc(cubeArray)
                tmp = fallingBlocks()
                tmp.fallingBlocksFunc(cubeArray)

        elif choice == 5:
                turnOffer.turnOffFunc(cubeArray)
                tmp = spinner()
                tmp.spinnerFunc(cubeArray)

        elif choice == 6:
            turnOffer.turnOffFunc(cubeArray)
            tmp = musicAnalyzer()
            tmp.musicAnalyzerFunc(cubeArray)

	elif choice == 7:
		turnOffer.turnOffFunc(cubeArray)
		tmp = idlePattern()
		tmp.idlePatternFunc(cubeArray)

        #can add more pattern choices below here

        #elif choice == 4:


            

        #if there are more counted sounds than patterns available
        else:
            print('invalid input, no corresponding pattern to run, try again')


#capture the control c and exit cleanly
except(KeyboardInterrupt, SystemExit): 
   print("\nUser requested exit... bye!")
   #GPIO.cleanup()











