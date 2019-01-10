import rtmidi_python as rtmidi
import RPi.GPIO as gpio
import time as t

gpio.setmode(gpio.BOARD)

gpio.setup(10, gpio.IN, pull_up_down=gpio.PUD_DOWN)

outport = rtmidi.MidiOut()
outport.open_virtual_port("vp")

while True:
    if  gpio.input(10) == gpio.HIGH:
        outport.send_message([0xb0, 0x74, 124])
        print('BUTTON PRESSED')
        t.sleep(0.05)
        #outport.send_message([0x90, 60, 0])
