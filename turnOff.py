import sys

sys.dont_write_bytecode =True

#############################
#A simple class that simply
#turns off the LED cube
#############################

class turnOff():
    def turnOffFunc(self,cube):
        for x in range (4):
            for y in range (4):
                for z in range(4):
                    cube[x][y][z].off()
