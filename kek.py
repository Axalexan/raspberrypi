import RPi.GPIO as GPIO
import time
chan_list = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(chan_list, GPIO.OUT)


numbers={7:26, 6:19, 5:13, 4:6, 3:5, 2:11, 1:9, 0:10}


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

print('Введите число повторений')


try:
    def scr(t):
        for i in range(t):
            for j in range(256):
                GPIO.output(chan_list,0)
                num2dec(j)
                time.sleep(0.01)
            for k in range(255,-1,-1):
                GPIO.output(chan_list,0)
                num2dec(k)
                time.sleep(0.01)
    t = int(input())
    scr(t)
except Exception:
    print('Error')

finally:
    GPIO.output(chan_list,0)


GPIO.cleanup()


