import RPi.GPIO as GPIO
import time

def dec2bin(a):
    return [int (digit) for digit in bin(a)[2:].zfill(8)]

dac = [26, 13, 19, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    print("input period: ")
    num = int(input())

    while True:
        for i in range(256):
            binary = dec2bin(i)
            GPIO.output(dac, binary)
            time.sleep(num / 512)

        for i in range(255, -1, -1):
            binary = dec2bin(i)
            GPIO.output(dac, binary)
            time.sleep(num / 512)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
