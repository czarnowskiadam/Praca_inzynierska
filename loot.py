import random
import game
import resources as res
import time

class Loot(object):
    def __init__(self):
        self.lootList = []
        self.commonEnemySouls = 1

    def loot(self, enemy):
        if enemy == 'skeleton':
            exp = random.randint(2, 4)
            gold = random.randint(2, 5)
            game.hero.expUP(exp)
            game.hero.addGold(gold)
            game.hero.addSouls(self.commonEnemySouls)
            self.lootList.extend([exp, gold, self.commonEnemySouls])
        elif enemy == 'witch':
            exp = random.randint(3, 5)
            gold = random.randint(4, 6)
            game.hero.expUP(exp)
            game.hero.addGold(gold)
            game.hero.addSouls(self.commonEnemySouls)
            self.lootList.extend([exp, gold, self.commonEnemySouls])
        elif enemy == 'golem':
            exp = random.randint(1, 5)
            gold = random.randint(5, 10)
            game.hero.expUP(exp)
            game.hero.addGold(gold)
            game.hero.addSouls(self.commonEnemySouls)
            self.lootList.extend([exp, gold, self.commonEnemySouls])
        elif enemy == 'slayer':
            exp = random.randint(5, 7)
            gold = random.randint(1, 5)
            game.hero.expUP(exp)
            game.hero.addGold(gold)
            game.hero.addSouls(self.commonEnemySouls)
            self.lootList.extend([exp, gold, self.commonEnemySouls])
        elif enemy == 'minotaur':
            exp = random.randint(3, 6)
            gold = random.randint(1, 5)
            game.hero.expUP(exp)
            game.hero.addGold(gold)
            game.hero.addSouls(self.commonEnemySouls)
            self.lootList.extend([exp, gold, self.commonEnemySouls])
        elif enemy == 'sorcerer':
            exp = random.randint(10, 15)
            gold = random.randint(15, 20)
            game.hero.expUP(exp)
            game.hero.addGold(gold)
            game.hero.addSouls(10)
            self.lootList.extend([exp, gold, 10])
        elif enemy == 'nightBorn':
            exp = random.randint(10, 15)
            gold = random.randint(15, 20)
            game.hero.expUP(exp)
            game.hero.addGold(gold)
            game.hero.addSouls(10)
            self.lootList.extend([exp, gold, 10])

    def getLoot(self, num):
        return self.lootList[num]

