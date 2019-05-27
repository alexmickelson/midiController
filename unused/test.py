import time as t
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)

gpio.setup(12, gpio.IN, pull_up_down=gpio.PUD_DOWN)


count = 0
print("we made it this far")
while True: 
    if  gpio.input(12) == gpio.HIGH:
        count +=1
        print(count)
        t.sleep(0.2)
