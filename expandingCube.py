import time
import sys
import random
from turnOff import *
sys.dont_write_bytecode=True

class expandingCube():
    def expandingCubeFunc(self,cube):
        sleepTime = .08 
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    cube[x][y][z].on()

        time.sleep(sleepTime)
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    cube[x][y][z].on()

        time.sleep(sleepTime)
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    cube[x][y][z].on()

        time.sleep(sleepTime)
        turnOffer = turnOff()
        turnOffer.turnOffFunc(cube)
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    cube[x][y][z].on()

 
        time.sleep(sleepTime)
        turnOffer = turnOff()
        turnOffer.turnOffFunc(cube)
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    cube[x][y][z].on()
        time.sleep(sleepTime)
        turnOffer.turnOffFunc(cube)
        time.sleep(sleepTime)


        for x in range(2):
            for y in range(2):
                for z in range(2):
                    cube[x][3-y][3-z].on()

        time.sleep(sleepTime)
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    cube[x][3-y][3-z].on()

        time.sleep(sleepTime)
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    cube[x][y][z].on()

        time.sleep(sleepTime)
        turnOffer.turnOffFunc(cube)
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    cube[x][3-y][3-z].on()


        time.sleep(sleepTime)
        turnOffer.turnOffFunc(cube)
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    cube[x][3-y][3-z].on()

        time.sleep(sleepTime)
        turnOffer.turnOffFunc(cube)
        time.sleep(sleepTime)

        cube[1][1][1].on()
        cube[1][2][1].on()
        cube[1][1][2].on()
        cube[1][2][2].on()
        cube[2][1][1].on()
        cube[2][2][1].on()
        cube[2][1][2].on()
        cube[2][2][2].on()

        time.sleep(sleepTime)
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    cube[x][y][z].on()

        time.sleep(sleepTime)
        turnOffer.turnOffFunc(cube)
        cube[1][1][1].on()
        cube[1][2][1].on()
        cube[1][1][2].on()
        cube[1][2][2].on()
        cube[2][1][1].on()
        cube[2][2][1].on()
        cube[2][1][2].on()
        cube[2][2][2].on()

        time.sleep(sleepTime)
        turnOffer.turnOffFunc(cube)






