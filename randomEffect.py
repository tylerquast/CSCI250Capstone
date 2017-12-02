import time
import sys
import random

sys.dont_write_bytecode = True

class randomEffect():
    def RandomFunc(self,cube):
        selections = []
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    selections.append([x,y,z])

        random.shuffle(selections)
        for i in range(64):
            time.sleep(.05)
            cube[selections[i][0]][selections[i][1]][selections[i][2]].on()
            time.sleep(.05)
            cube[selections[i][0]][selections[i][1]][selections[i][2]].off()


