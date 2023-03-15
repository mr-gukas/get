import RPi.GPIO as GPIO
import time

def dec2bin(a):
    return [int (digit) for digit in bin(a)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)

dac = [26, 13, 19, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)


pwm = GPIO.PWM(2, 1000)
pwm.start(0)

try:
    while True:
        duty = int(input())
        pwm.ChangeDutyCycle(duty)
        
        GPIO.output(dac, dec2bin(int(duty * 255 / 100)))

        print("Volt: {:.2f}".format(duty * 3.3 / 100))
        
finally:
    GPIO.output(2, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()