import game
import resources as res
import player as pl

cactusLvl = {'cactusLvl': 0}

class Cactus(object):
    def __init__(self):
        self.lvl = cactusLvl.get('cactusLvl')
        self.lvlReq = [20, 25, 30, 35, 40, 45, 50, 55]

    def update(self):
        cactusLvl.update({'cactusLvl': self.lvl})

    def reset(self):
        self.lvl = 0

    def leveling(self, num):
        if self.lvl == num and game.hero.souls >= self.lvlReq[num]:
            self.lvl += 1
            game.hero.souls -= self.lvlReq[num]
            if self.lvl == 1:
                game.hero.minDmg += 1
                game.hero.maxDmg += 1
            if self.lvl == 2:
                game.hero.maxHP += 5
            if self.lvl == 3:
                game.hero.maxHP += 5
            if self.lvl == 4:
                game.hero.minDmg += 1
                game.hero.maxDmg += 1
            if self.lvl == 5:
                game.hero.minMDmg += 1
                game.hero.maxMDmg += 1
            if self.lvl == 6:
                game.hero.minMDmg += 1
                game.hero.maxMDmg += 1
            if self.lvl == 7:
                game.hero.maxHP += 10
            if self.lvl == 8:
                game.hero.minDmg += 3
                game.hero.maxDmg += 3


    def lvlGet(self):
        return self.lvl

    def currSoulsGet(self):
        return self.currSouls

    def lvlReqGet(self, num):
        return self.lvlReq[num]

    def info(self):
        if self.lvl < len(self.lvlReq):
            res.textSetting(game.screen, (620, 10), res.pixelFont, res.menuTextColour, f'Lvl: {self.lvl}')
            res.textSetting(game.screen, (500, 40), res.pixelFont, res.menuTextColour, f'Next Lvl for: {self.lvlReq[self.lvl]} Souls')
        else:
            res.textSetting(game.screen, (620, 10), res.pixelFont, res.menuTextColour, f'Lvl: MAX')