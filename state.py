#!/usr/bin/python
import rtmidi_python as rtmidi
import RPi.GPIO as gpio
import time as t

#init gpio port
gpio.setmode(gpio.BOARD)
gpio.setup(10, gpio.IN, pull_up_down=gpio.PUD_DOWN)

#init rtmidi
outport = rtmidi.MidiOut()
outport.open_virtual_port("vp")

#list of commands
#first
recordAll = [0xb0, 0x74, 0]



#loop 1
play1  = [0xb0, 0x74, 1]
mute1  = [0xb0, 0x74, 2]
unmute1  = [0xb0, 0x74, 3]
undo1  = [0xb0, 0x74, 4]
replace1  = [0xb0, 0x74, 5]

#loop 2
play2  = [0xb0, 0x74, 6]
mute2  = [0xb0, 0x74, 7]
unmute2  = [0xb0, 0x74, 8]
undo2  = [0xb0, 0x74, 9]
replace2  = [0xb0, 0x74, 10]

#loop 3
play3  = [0xb0, 0x74, 11]
mute3  = [0xb0, 0x74, 12]
unmute3  = [0xb0, 0x74, 13]
undo3  = [0xb0, 0x74, 14]
replace3  = [0xb0, 0x74, 15]

#loop 4
play4  = [0xb0, 0x74, 16]
mute4  = [0xb0, 0x74, 17]
unmute4  = [0xb0, 0x74, 18]
undo4  = [0xb0, 0x74, 19]
replace4  = [0xb0, 0x74, 20]


while True:
    if  gpio.input(10) == gpio.HIGH:
        outport.send_message([0xb0, 0x74, 50])
        print('BUTTON PRESSED')
        t.sleep(0.05)


