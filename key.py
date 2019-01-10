import RPi.GPIO as gpio
import time
from subprocess import Popen, PIPE

rkey = 'key R'


gpio.setmode(gpio.BOARD)

gpio.setup(10, gpio.IN, pull_up_down=gpio.PUD_DOWN)

def kp(key):
    p = Popen(['xte', 'key r'], stdin=PIPE)
    #p.communicate(input='''key a''')

while True:
    if  gpio.input(10) == gpio.HIGH:
        print('BUTTON PRESSED')
        kp(rkey)

