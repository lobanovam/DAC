import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


dac = [26, 19, 13, 6, 5, 11, 9, 10]  

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        value = input("please input a number in range 0-255: ")
        if (value == 'q'):
            break
        value = int(value)

        if (value > 255):
            print("ERROR: out of range")
            value = 0
        if (value < 0):
            print("ERROR: only positive integers")
            value = 0
        GPIO.output(dac, decimal2binary(value))
        print(decimal2binary(value))
        print("expected voltage is", (3.3/256) * value)

except ValueError:
    print("Error, not an integer")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()




