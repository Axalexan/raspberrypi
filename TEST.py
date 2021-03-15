import RPi.GPIO as GPIO
GPIO.cleanup()
import time
chan_list = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setmode(GPIO.BCM)
GPIO.setup(chan_list, GPIO.OUT)


numbers={7:21, 6:20, 5:16, 4:12, 3:7, 2:8, 1:25, 0:24}


def lightup(ledNumber, period):
    GPIO.output(numbers[ledNumber],1)
    time.sleep(period)
    GPIO.output(numbers[ledNumber],0)


def lightdown(ledNumber, period):
    GPIO.output(numbers[ledNumber],0)
    time.sleep(period)
    GPIO.output(numbers[ledNumber],1)


def blink(ledNumber, blinkCount, BlinkPeriod):
    for i in range(0,blinkCount):
        lightup(ledNumber, BlinkPeriod)
        lightdown(ledNumber, BlinkPeriod)


def runningLight(count, period):
    for i in range(count):
        for j in range(8):
            lightup(j, period)


def runningDark(count, period):
    GPIO.output(chan_list,1)
    for i in range(count):
        for j in range(8):
            lightdown(j, period)
    else:
        GPIO.output(chan_list,0)


def decToBinList(decNumber):
    s = []
    while decNumber > 0:
        s.append(decNumber % 2)
        decNumber //= 2
    while len(s) < 8:
        s.append(0)
    a = []
    for i in range(len(s) - 1, -1, -1):
        a.append(s[i])
    return s


def lightNumber(number):
    s = decToBinList(number)
    for i in range(7,-1,-1):
       GPIO.output(numbers[i],s[i])
    else:
        time.sleep(1)


def light2(s):
    for i in range(7,-1,-1):
       GPIO.output(numbers[i],s[i]) 


def runningPattern(pattern , direction):
    s = decToBinList(pattern)
    p = pattern
    while True:
        pattern = p
        for i in range(8):
            time.sleep(0.5)
            GPIO.output(chan_list,0)
            lightNumber(pattern)
            pattern = pattern << 1
        


runningPattern(2, 1)


GPIO.cleanup()


