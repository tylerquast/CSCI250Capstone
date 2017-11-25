def Mphone():
    #import libraries
    import spidev
    import time
    #for ADC: from decimal import getcontext
    import RPi.GPIO as GPIO

#for ADC if used
##    #setup functions to run ADC
##    def bitstring(n): 
##        s = bin(n)[2:]
##        return '0'*(8-len(s)) + s #8bit
##
##    def read(adc_channel):
##        spi_channel=0 #default channel is 0
##        spi = spidev.SpiDev()
##        spi.open(adc_channel, spi_channel)
##        spi.max_speed_hz = 1000000 # 1.0 MHz (feel free to change this value to adjust speed at which inputs are read).
##        cmd = 128
##        if adc_channel:
##            cmd += 32
##        reply_bytes = spi.xfer2([cmd, 0])
##        reply_bitstring = ''.join(bitstring(n) for n in reply_bytes)
##        reply = reply_bitstring[5:15]
##        return int(reply, 2) / 2**10
##
##    #for ADC: getcontext().prec = 2
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.IN)
    
    sound =0
    time0 = time.time()
    stopTime = time0 + 5
    print('\n\n searching \n \n')
    while (time.time() < stopTime): #search for input for 5 seconds
            input = GPIO.input(27)
            #print(input)
            
            if input == True:
                sound+=1
            time.sleep(.04)
            
    return sound   
