import random

class Generator(object):
    def __init__(self):
        self.luckTest = True
        self.treasure = True
        self.stages = []
        self.pos = 0

        for i in range(0, 8):
            self.stages.append('Fight')

        x = random.randint(1, 6)
        if self.stages[x] == 'Fight':
            self.stages[x] = 'Bonfire'

        while self.luckTest:
            x = random.randint(0, 7)
            if self.stages[x] == 'Fight':
                self.stages[x] = 'Luck Test'
            else:
                pass

            if self.stages.count('Luck Test') == 1:
                self.luckTest = False

        while self.treasure:
            x = random.randint(0, 7)
            if self.stages[x] == 'Fight':
                self.stages[x] = 'Treasure'
            else:
                pass

            if self.stages.count('Treasure') == 1:
                self.treasure = False

        self.stages.append('Bonfire')
        self.stages.append('Boss')

    def getStages(self):
        return self.stages

    def getPos(self):
        return self.stages[self.pos]

    def nextStage(self):
        self.pos += 1

    def getStage(self):
        return self.pos

    def reset(self):
        self.pos = 0
        self.stages.clear()
        self.luckTest = True
        self.treasure = True
