import rtmidi_python as rtmidi


#init rtmidi
outport = rtmidi.MidiOut()
outport.open_virtual_port("vp")

#list of commands
#first
recordAll = [0xb0, 0x74, 0]

#loop 1
class loop:
    def __init__(self, loopNumber):
        self.loopNumber = loopNumber

    def rec(self):
        outport.send_message([0xb0, 0x73, self.loopNumber])
        print("MIDI: Record loop "+self.loopNumber)

    def pause(self):
        outport.send_message([0xb0, 0x74, self.loopNumber])
        print("MIDI: Pause loop "+self.loopNumber)

    def unpause(self):
        outport.send_message([0xb0, 0x72, self.loopNumber])
        print("MIDI: Unpause loop "+self.loopNumber)

    def mute(self):
        outport.send_message([0xb0, 0x75, self.loopNumber])
        print("MIDI: Mute loop "+self.loopNumber)

    def unmute(self):
        outport.send_message([0xb0, 0x76, self.loopNumber])
        print("MIDI: unMute loop "+self.loopNumber)

    def undo(self):
        outport.send_message([0xb0, 0x77, self.loopNumber])
        print("MIDI: Undo loop "+self.loopNumber)

    def replace(self):
        outport.send_message([0xb0, 0x78, self.loopNumber])
        print("MIDI: Replace loop "+self.loopNumber)

    def dub(self):
        outport.send_message([0xb0, 0x79, self.loopNumber])
        print("MIDI: Overdub loop "+self.loopNumber)



