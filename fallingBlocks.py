import time
import sys
from turnOff import *

sys.dont_write_bytecode= True




################################3##
#This class makes entire rows move
#Up and down
###################################

class fallingBlocks():
    def fallingBlocksFunc(self,cube):
        sleepTime = .08
        turnOffer = turnOff()
        for i in range(10):
            for e in range(4):         
                turnOffer.turnOffFunc(cube)
                for x in range(4):
                    for y in range(4):
                        cube[3-e][x][y].on()
                time.sleep(sleepTime)
                
        for i in range(4):
            turnOffer.turnOffFunc(cube)
            time.sleep(.25)
            for x in range(4):
                for y in range(4):
                    cube[0][x][y].on()
            time.sleep(.25)


        for i in range(10):
            for e in range(4):         
                turnOffer.turnOffFunc(cube)
                for x in range(4):
                    for y in range(4):
                        cube[e][x][y].on()
                time.sleep(sleepTime+(e/10))
        

        for i in range(4):
            turnOffer.turnOffFunc(cube)
            time.sleep(.25)
            for x in range(4):
                for y in range(4):
                    cube[3][x][y].on()
            time.sleep(.25)


        for i in range(5):
            for e in range(4):
                turnOffer.turnOffFunc(cube)
                for x in range(4):
                    for y in range(4):
                        cube[3-e][x][y].on()
                time.sleep(sleepTime)
            for e in range(4):
                turnOffer.turnOffFunc(cube)
                for x in range(4):
                    for y in range(4):
                        cube[e][x][y].on()
                time.sleep(sleepTime)
                






