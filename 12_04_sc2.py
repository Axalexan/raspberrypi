import RPi.GPIO as GPIO
import time
chan_list = [26, 19, 13, 6, 5, 11, 9, 10, 17]
chan_list1 = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(chan_list, GPIO.OUT)
GPIO.setup(4, GPIO.IN)


numbers={7:26, 6:19, 5:13, 4:6, 3:5, 2:11, 1:9, 0:10}

GPIO.output(17, 1)


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

def num2dec(value):
    k = decToBinList(value)
    for i in range(8):
        if k[i] == 1:
            GPIO.output(numbers[i],1)
        else:
            GPIO.output(numbers[i],0)

try:
    GPIO.setwarnings(False)
    k=-1
    while True:
        #if  GPIO.input(4)==0:
        for i in range(256):
            num2dec(i)
            time.sleep(0.001)
            if GPIO.input(4) == 0:
                print('Digital value ',i, ', Analog value:', round(3.3*(i/255),1), 'V')
                break
          

finally:
    GPIO.cleanup()