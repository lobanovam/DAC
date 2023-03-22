import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
print(decimal2binary(10))

dac = [21, 20, 16, 12, 7, 8, 25, 24]  

GPIO.setup(dac, GPIO.OUT)

try:
    while(1):
        value = input("please input a number in range 0-255")
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
        print("expected voltage is", (3.3/256) * value)

except ValueError:
    print("Error, not an integer")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()


p = GPIO.PWM(24, 50)
p.start(100)
input("Press return to stop")
p.stop()


