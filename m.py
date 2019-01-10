import mido as m
import rtmidi_python as rtmidi
import RPi.GPIO as gpio
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(10, gpio.IN, pull_up_down=gpio.PUD_DOWN)


msg = m.Message('note_on', note=60)

outport = rtmidi.MidiOut()

outport.open_virtual_port('vp')
print('PORT CONNECTED')


print(msg)
print("we made it this far")
while True: 
        if  gpio.input(10) == gpio.HIGH:
                    print('BUTTON PRESSED')
                    outport.send_message([0x80, 60, 112])
                    print('MESSAGE SENT')
                    time.sleep(0.5)
                    #outport.send_message([0x80, 60, 0])



