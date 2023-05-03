import  RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)
#------------------------------------
leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

#--------------------------------------

def dec2bin(val):
    return [int(element) for element in bin(val)[2:].zfill(8)]

def output_leds(num):
    GPIO.output(leds, dec2bin(num))

def num2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac, signal)
    return signal

def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        GPIO.output(dac, dec2bin(k))
        time.sleep(0.005)
        if GPIO.input(comp)==0:
            k-=2**i
    return k

try:
    GPIO.output(17, 0)
    data = []
    begin = time.time()
    
    v = 0
    i = 0
    #----------(зарядка)----------------
    while v < 3.0:
        num = adc()
        data.append(num)
        v = num * 3.3 / 256
        print(v)
        output_leds(num)
        i+=1
    #----------(разрядка)---------------
    GPIO.output(17, 1)
    while v > 0.8:
        num = adc()
        data.append(num)
        v = num * 3.3 / 256
        print(v)
        output_leds(num)
        i+=1
    #-----------------------------------
    end = time.time()

    length = begin - end

    plt.plot(data)
    #plt.xlim (1, )
    plt.show()
    #--сохраняем данные--------------------
    data_str = [str(item) for item in data]

    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(data_str))

    with open('settings.txt', 'w') as f:
        f.write(str(1/(length/i) + '\n'))
      
    
finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()