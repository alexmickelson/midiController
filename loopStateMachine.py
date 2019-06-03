import states
import midiFunctions as midi

class loopStateMachine:
    def __init__(self, loopNumber):
        print(loopNumber)
        self.midi=midi.loop(loopNumber)

        self.blankState=states.blankState(self)
        self.recState=states.recState(self)
        self.playState=states.playState(self)
        self.pauseState=states.pauseState(self)
        self.dubState=states.dubState(self)
        
        self.currentState = self.blankState
    
    def pressPedal1(self):
        self.currentState.pressPedal1()

    def pressPedal2(self):
        self.currentState.pressPedal2()

