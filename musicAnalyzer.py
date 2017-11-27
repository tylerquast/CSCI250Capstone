import audioop
import pyaudio
import wave

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 2

p=pyaudio.PyAudio()

s = p.open(format = FORMAT,
	channels = CHANNELS,
	rate = RATE,
	input = True,
	frames_per_buffer = chunk)

while True:
	data = s.read(chunk)
	mx = audioop.max(data,2)
	print(mx)




