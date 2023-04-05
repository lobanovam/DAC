import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def num2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal

def adc():
    for value in range (0, 256):
        signal = num2dac(value)
        time.sleep(0.001)
        compValue = GPIO.input(comp)
        if compValue == 0:
            print(signal)
            return value
        

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        v_dec = adc()
        v = v_dec*3.3/256
        print(v, "\n")


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()