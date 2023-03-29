import RPi.GPIO as GPIO
import time

def dec2bin(a):
    return [int (digit) for digit in bin(a)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)

dac    = [26, 13, 19, 6, 5, 11, 9, 10]
comp   = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def adc():
    bin = 0
    for index in range(7, -1, -1):
        bin += 2**(index)
        GPIO.output(dac, dec2bin(bin))
        time.sleep(0.005)
        comp_val = GPIO.input(comp)
        
        if comp_val == 0:
            bin -= 2**(index)
    return bin


try:
    while True:
        index = adc()
        if index != 0:
            print(index, '{:.2f}v'.format(3.3 * index / 256))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()