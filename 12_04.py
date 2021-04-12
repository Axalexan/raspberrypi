import RPi.GPIO as GPIO
import time
chan_list = [26, 19, 13, 6, 5, 11, 9, 10, 17]
GPIO.setmode(GPIO.BCM)
GPIO.setup(chan_list, GPIO.OUT)


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



try:
    while True:

        print('Enter value (-1 to exit)')
        i = int(input())
        if i == -1:
            break
        print(i ,' = ', round(3.3*(i/255),2) ,'V')
        GPIO.output(chan_list,0)
        GPIO.output(17,1)
        num2dec(i)
        time.sleep(0.1)
finally:
    GPIO.cleanup()

