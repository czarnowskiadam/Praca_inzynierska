import random
import resources as res
import game

class LuckTest(object):
    def __init__(self):
        self.table = []
        self.createTable()
        self.clickedTiles = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.playerResult = []
        self.comResult = []
        self.completionNum = 3

    def createTable(self):
        for i in range(0, 9):
            num = random.randint(0, 9)
            self.table.append(num)

    def displayTiles(self):
        if self.clickedTiles[0] == 1:
            res.textSetting(game.screen, (470, 130), res.pixelFont, res.red, str(self.table[0]))
        else:
            res.textSetting(game.screen, (470, 130), res.pixelFont, res.menuTextColour, '1')

        if self.clickedTiles[1] == 1:
            res.textSetting(game.screen, (660, 130), res.pixelFont, res.red, str(self.table[1]))
        else:
            res.textSetting(game.screen, (660, 130), res.pixelFont, res.menuTextColour, '2')

        if self.clickedTiles[2] == 1:
            res.textSetting(game.screen, (850, 130), res.pixelFont, res.red, str(self.table[2]))
        else:
            res.textSetting(game.screen, (850, 130), res.pixelFont, res.menuTextColour, '3')

        if self.clickedTiles[3] == 1:
            res.textSetting(game.screen, (470, 280), res.pixelFont, res.red, str(self.table[3]))
        else:
            res.textSetting(game.screen, (470, 280), res.pixelFont, res.menuTextColour, '4')

        if self.clickedTiles[4] == 1:
            res.textSetting(game.screen, (660, 280), res.pixelFont, res.red, str(self.table[4]))
        else:
            res.textSetting(game.screen, (660, 280), res.pixelFont, res.menuTextColour, '5')

        if self.clickedTiles[5] == 1:
            res.textSetting(game.screen, (850, 280), res.pixelFont, res.red, str(self.table[5]))
        else:
            res.textSetting(game.screen, (850, 280), res.pixelFont, res.menuTextColour, '6')

        if self.clickedTiles[6] == 1:
            res.textSetting(game.screen, (470, 430), res.pixelFont, res.red, str(self.table[6]))
        else:
            res.textSetting(game.screen, (470, 430), res.pixelFont, res.menuTextColour, '7')

        if self.clickedTiles[7] == 1:
            res.textSetting(game.screen, (660, 430), res.pixelFont, res.red, str(self.table[7]))
        else:
            res.textSetting(game.screen, (660, 430), res.pixelFont, res.menuTextColour, '8')

        if self.clickedTiles[8] == 1:
            res.textSetting(game.screen, (850, 430), res.pixelFont, res.red, str(self.table[8]))
        else:
            res.textSetting(game.screen, (850, 430), res.pixelFont, res.menuTextColour, '9')

    def sumPlayerResult(self):
        return sum(self.playerResult)

    def sumComResult(self):
        return sum(self.comResult)

    def playerTurnAction(self, pos):
        self.clickedTiles[pos] = 1
        self.playerResult.append(self.table[pos])

    def comTurnAction(self):
        test = True
        while test:
            choice = random.randint(0, 8)
            if self.clickedTiles[choice] == 0:
                self.clickedTiles[choice] = 1
                self.comResult.append(self.table[choice])
                test = False

    def getClickedTile(self, pos):
        return self.clickedTiles[pos]

    def gameReward(self):
        if self.sumPlayerResult() - self.sumComResult() >= 22:
            return 50
        elif 22 > self.sumPlayerResult() - self.sumComResult() >= 14:
            return 35
        elif 14 > self.sumPlayerResult() - self.sumComResult() >= 6:
            return 20
        elif 6 > self.sumPlayerResult() - self.sumComResult() >= 1:
            return 10
        else:
            return 0

    def finalResult(self):
        if self.sumPlayerResult() > self.sumComResult():
            return 'You won!'
        elif self.sumPlayerResult() < self.sumComResult():
            return 'You lose!'
        else:
            return 'Draw!'