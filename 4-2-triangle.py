import RPi.GPIO as GPIO
import time as time 

GPIO.setmode(GPIO.BCM)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
print(decimal2binary(10))

dac = [21, 20, 16, 12, 7, 8, 25, 24] 
GPIO.setup(dac, GPIO.OUT)

try:
    print("triangle shit")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()