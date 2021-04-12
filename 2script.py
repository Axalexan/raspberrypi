import RPi.GPIO as GPIO
import time
chan_list = [26, 19, 13, 6, 5, 11, 9, 10, 17]
GPIO.setmode(GPIO.BCM)
GPIO.setup(chan_list, GPIO.OUT)


numbers={7:26, 6:19, 5:13, 4:6, 3:5, 2:11, 1:9, 0:10}
GPIO.output(chan_list,0)

GPIO.cleanup()