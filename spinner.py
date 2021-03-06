import time
import RPi.GPIO as IO
import sys

sys.dont_write_bytecode = True



##################################
#This is by far the most complex
#pattern. The paper goes into 
#great detail about how this
#pattern works.
##################################


class spinner():
    def spinnerFunc(self,cube):
        counter = 0
        sleepTime = .08
	for a in range(3):
		counter = 0
		for x in range(12):
		    if counter < 4:
			for y in range(4):
			    cube[y][0][counter].on()
			time.sleep(sleepTime)
		    elif counter > 3 and counter < 7:
			for y in range(4):
			    cube[y][counter - 3][3].on()
			time.sleep(sleepTime)
		    elif counter > 6 and counter < 10:
			for y in range(4):
			    cube[y][3][9-counter].on()
			time.sleep(sleepTime)
		    else:
			for y in range(4):
			    cube[y][12-counter][0].on()
			time.sleep(sleepTime)




		    counter = counter + 1





		counter = 0
		for x in range(12):
		    if counter < 4:
			for y in range(4):
			    cube[y][0][counter].off()
			    IO.output((24,23,18,21),1)
			time.sleep(sleepTime)
		    elif counter > 3 and counter < 7:
			for y in range(4):
			    cube[y][counter - 3][3].off()
			    IO.output((24,23,18,21),1)
			time.sleep(sleepTime)
		    elif counter > 6 and counter < 10:
			for y in range(4):
			    cube[y][3][9-counter].off()
			    IO.output((24,23,18,21),1)
			time.sleep(sleepTime)
		    else:
			for y in range(4):
			    cube[y][12-counter][0].off()
			    IO.output((24,23,18,21),0)

			time.sleep(sleepTime)




		    counter = counter + 1
