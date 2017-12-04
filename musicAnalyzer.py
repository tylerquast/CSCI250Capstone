import audioop
import RPi.GPIO as IO
import pyaudio
import wave
import time

class musicAnalyzer():
    def musicAnalyzerFunc(self,cube):
        chunk = 10000
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        RECORD_SECONDS = 2

        p=pyaudio.PyAudio()




       #jank central
        cols = [19,26,14,15,11,5,6,13,27,22,10,9,2,3,4,17]
        IO.output(cols,1) 
        






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
                IO.output(24,0)
                IO.output(23,1)
                IO.output(18,1)
                IO.output(21,1)

            elif(mx>3750 and mx < 4500):
                IO.output(24,0)
                IO.output(23,0)
                IO.output(18,1)
                IO.output(21,1)


            elif(mx>4500 and mx < 5250):
                IO.output(24,0)
                IO.output(23,0)
                IO.output(18,0)
                IO.output(21,1)


            else:
                IO.output(24,0)
                IO.output(23,0)
                IO.output(18,0)
                IO.output(21,0)



