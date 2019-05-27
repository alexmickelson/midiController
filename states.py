
class blankState:
    def __init__(self, stateMachine):
        self.stateMachine=stateMachine

    def pressPedal1(self):
        self.stateMachine.midi.rec()
        self.stateMachine.currentState=self.stateMachine.recState

    def pressPedal2(self):
        pass

class recState:
    def __init__(self, stateMachine):
        self.sm=stateMachine

    def pressPedal1(self):
        self.sm.midi.rec() #should stop recording but continue playing
        self.sm.currentState=self.sm.playState

    def pressPedal2(self):
        self.sm.midi.pause()
        self.sm.currentState=self.sm.pauseState


class playState:
    def __init__(self, stateMachine):
        self.sm=stateMachine

    def pressPedal1(self):
        self.sm.midi.dub()
        self.sm.currentState=self.sm.dubState

    def pressPedal2(self):
        self.sm.midi.pause()
        self.sm.currentState=self.sm.pauseState
        
class pauseState:
    def __init__(self, stateMachine):
        self.sm=stateMachine

    def pressPedal1(self):
        self.sm.midi.unpause()
        self.sm.currentState=self.sm.playState

    def pressPedal2(self):
        pass

class dubState:
    def __init__(self, stateMachine):
        self.sm=stateMachine

    def pressPedal1(self):
        self.sm.midi.dub()
        self.sm.currentState=self.sm.playState

    def pressPedal2(self):
        self.sm.midi.pause()
        self.sm.currentState=self.sm.pauseState