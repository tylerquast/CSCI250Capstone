#Uncomment this when moved to rasp pi, I build this initially on my laptop.

######################
#import RPi.GPIO as IO
######################
import sys
import time
import random
from LED import *
from cube import *
from loopAndBlink import *
from key import *
from Mphone import *
import numpy as np


#stops python from generating a .pyc file
sys.dont_write_bytecode = True


#Main Class


#Creates an LED cube Object
cube = cube()

#Fills a 4x4x4 array with LED Objects to represent the cube
#See the 'buildCube' method in cube.py
#All leds are turned off by defualt
cubeArray = cube.buildCube()


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
		print('pattern One')

        elif choice == 2:
		print('pattern Two')

        elif choice == 3:
		print('pattern Three')

        #can add more pattern choices below here

        #elif choice == 4:


            

        #if there are more counted sounds than patterns available
        else:
            print('invalid input, no corresponding pattern to run, try again')


#capture the control c and exit cleanly
except(KeyboardInterrupt, SystemExit): 
   print("\nUser requested exit... bye!")
   #GPIO.cleanup()











