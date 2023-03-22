import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)

p = GPIO.PWM(24, 0.5)
p.start(0)

try:
    while (1):
        dc = int(input("Please, enter a duty cycle"))
        p.start(dc)
except ValueError:
    print("you mast enter an integer")
finally:
    p.stop()
    GPIO.output(24, 0)
    GPIO.cleanup()