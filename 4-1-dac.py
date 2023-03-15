import RPi.GPIO as GPIO

def dec2bin(a):
    return [int (digit) for digit in bin(a)[2:].zfill(8)]

def inputData():
    try:
        str = input()
        num = int(str)

        if num < 0:
            print('enter positive numbers!')
            return -1
        elif num > 255:
            print('enter number no more than 255')
            return -1
        else:
            return num

    except otherWay:
        if str == "q":
            exit()
        else:
            print("Incorrect input. Try again!")
            return -1



dac = [26, 13, 19, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while (True):
        print("Enter value from 0 to 255")

        num = inputData()

        if num != -1:
            binary = dec2bin(num)
            GPIO.output(dac, binary)
            print("Volt: ", 3.3 / 256 * num)
    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
