import audioop
import RPi.GPIO as IO
import pyaudio
import wave
import time




######################################
#A class built to make the cube
#bounce to the beat of music.
#Unfortunatly we had some problems
#with this class. we are not sure if
#is the power of the pi or the code.
#I took an apporach of just turning
#on or off the four rows each time
#while leaving each column on at the
#start however this did not make much
#of a difference
######################################
class musicAnalyzer():
    def musicAnalyzerFunc(self,cube):
	#Pyaudio was utalized to take
	#input from the USb mic.
        chunk = 10000
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        RECORD_SECONDS = 2

        p=pyaudio.PyAudio()


	#Each one of the columns is turned on itially
	#this is to minimize the amount of code exicuted
	#each time the cube goes to update its leds
        cols = [19,26,14,15,11,5,6,13,27,22,10,9,2,3,4,17]
        IO.output(cols,0) 
        

        s = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk)

        while True:
            data = s.read(chunk)
            mx = audioop.max(data,2)
            time.sleep(.2)


            if(mx<1000):
                pass

            elif(mx > 3000 and mx < 3750):
                IO.output(24,1)
                IO.output(23,0)
                IO.output(18,0)
                IO.output(21,0)

            elif(mx>3750 and mx < 4500):
                IO.output(24,1)
                IO.output(23,1)
                IO.output(18,0)
                IO.output(21,0)


            elif(mx>4500 and mx < 5250):
                IO.output(24,1)
                IO.output(23,1)
                IO.output(18,1)
                IO.output(21,0)


            else:
                IO.output(24,1)
                IO.output(23,1)
                IO.output(18,1)
                IO.output(21,1)



