#!/usr/bin/python
import rtmidi_python as rtmidi
import RPi.GPIO as g
import time as t

#init g port
g.setmode(g.BOARD)
g.setup(12, g.IN, pull_up_down=g.PUD_DOWN)
g.setup(10, g.IN, pull_up_down=g.PUD_DOWN)

#init rtmidi
outport = rtmidi.MidiOut()
outport.open_virtual_port("vp")

#0=base 1=rec 2=play
state = 0
count = 1
#loop 1
def loop1(cmd):
    if cmd=='rec':
        outport.send_message([0xb0, 0x73, 0])
    if cmd=='pause':
        outport.send_message([0xb0, 0x74, 0])
    if cmd =='unpause':
        outport.send_message([0xb0, 0x72, 0])
    if cmd=='mute':
        outport.send_message([0xb0, 0x75, 0])
    if cmd=='unmute':
        outport.send_message([0xb0, 0x76, 0])
    if cmd=='undo':
        outport.send_message([0xb0, 0x77, 0])
    if cmd=='replace':
        outport.send_message([0xb0, 0x78, 0])
    if cmd=='dub':
        outport.send_message([0xb0, 0x79, 0])

def rec1(c):
    loop1('rec')
    #outport.send_message(rec1)
    print('REC START')
    t.sleep(0.4)
    while g.input(10)==g.LOW:
        pass
    loop1('rec')
    print('REC DONE')
    t.sleep(0.4)

def dub1():
    loop1('dub')
    print('DUB START')
    t.sleep(0.4)
    while g.input(10)==g.LOW:
        pass
    loop1('dub')
    print('DUB DONE')
    t.sleep(0.4)

def pause1():
    loop1('pause')
    print('PAUSED')
    while g.input(10)==g.LOW:
        pass
    loop1('unpause')
    print('UN-PAUSED')
    t.sleep(0.4)
    

def state2():
    if g.input(10)==g.HIGH:
        dub1()
        #print('DUB')
        t.sleep(0.4)
    if g.input(12)==g.HIGH:
        pause1()


def state1():
    if g.input(10)==g.HIGH:
        rec1(10)
        while True:
            #when done go to state 2
            state2()

print('ready')
while True:
    state1()




