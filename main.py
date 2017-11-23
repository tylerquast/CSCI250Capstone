#Uncomment this when moved to rasp pi, I build this initially on my laptop.

######################
#import RPi.GPIO as IO
######################
import time
import random
from LED import *
from cube import *
from loopAndBlink import *
import numpy as np

#Main Class


#Creates an LED cube Object
cube = cube()

#Fills a 4x4x4 array with LED Objects to represent the cube
#See the 'buildCube' method in cube.py
#All leds are turned off by defualt
cubeArray = cube.buildCube()


#A sparkfun sound detector is used to trigger various 
#effects with claps

#############################################
#code to work with the audio sensor goes here
#############################################


####################################################
#Example: say the blink every LED effect was called:
#This will be removed later
####################################################

tmp = loopAndBlink()
tmp.loopAndBlinkFunc(cubeArray)

