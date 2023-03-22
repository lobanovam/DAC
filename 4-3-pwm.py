import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(18, 1000)
p.start(0)

try:
    while True:
        dc = int(input("Please, enter a duty cycle: "))
        if dc > 100:
            print("dc must be less than 100")
            continue
        p.ChangeDutyCycle(dc)
        print(dc / 100 * 3.3)
        

except ValueError:
    print("you mast enter an integer")

finally:
    p.stop()
    GPIO.output(18, 0)
    GPIO.cleanup()