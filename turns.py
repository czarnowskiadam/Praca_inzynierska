import random

class Turn:
    def __init__(self):
        self.startCount = 0
        self.startTurn = random.randrange(0, 2)
        if self.startTurn == 0:
            self.turn = 1
        else:
            self.turn = 2

    def getTurn(self):
        return self.turn

    def endTurn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def resetStartCount(self):
        self.startCount = 0

    def reset(self):
        self.startTurn = random.randrange(0, 2)
        self.turn = 0





