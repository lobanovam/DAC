import RPi.GPIO as GPIO
import time as time 

GPIO.setmode(GPIO.BCM)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


dac = [26, 19, 13, 6, 5, 11, 9, 10]  
GPIO.setup(dac, GPIO.OUT)

try:
    period = float(input("please input a period: "))
    while True:
        for i in range(0, 256, 1):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(period)
        for i in range(255, -1, -1):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(period)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()