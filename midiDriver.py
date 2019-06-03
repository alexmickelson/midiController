#!/usr/bin/python
import rtmidi_python as rtmidi
import RPi.GPIO as g
import time as t
import loopStateMachine

#init g port
g.setmode(g.BOARD)
g.setup(12, g.IN, pull_up_down=g.PUD_DOWN)
g.setup(10, g.IN, pull_up_down=g.PUD_DOWN)

def pedal1():
    return g.inpu(10)==g.HIGH
def pedal2():
    return g.inpu(12)==g.HIGH


#init rtmidi
outport = rtmidi.MidiOut()
outport.open_virtual_port("vp")

loop1 = loopStateMachine(1)

print('starting loop pedal')
while True:
    if pedal1():
        loop1.pressPedal1()
    if pedal2():
        loop1.pressPedal2()
        for i in range(10):
            t.sleep(.1)
            if not pedal2():
                break