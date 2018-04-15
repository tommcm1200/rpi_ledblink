#import the GPIO and time package
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

chan_list = [7,11,13]
GPIO.setup(chan_list, GPIO.OUT)

# GPIO.setup(7, GPIO.OUT)
# loop through 50 times, on/off for 1 second
GPIO.output(13,True)

for i in range(50):
    GPIO.output(7,True)
    GPIO.output(11,False)
    GPIO.output(13,False)
    time.sleep(1)
    GPIO.output(7,False)
    GPIO.output(11,True)
    GPIO.output(13,False)
    time.sleep(1)
    GPIO.output(7,False)
    GPIO.output(11,False)
    GPIO.output(13,True)
    time.sleep(1)
GPIO.cleanup()