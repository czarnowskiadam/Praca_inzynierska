import random
import game

class HuntingHut(object):
    def __init__(self):
        self.rangAmount = {'rang1': 25,
                              'rang2': 50,
                              'rang3': 100,
                              'rang4': 150,
                              'rang5': 200,
                              'rang6': 250,
                              'rang7': 300,
                              'rang8': 350,
                              'rang9': 400,
                              'rang10': 500}

    def update(self):
        if game.hero.rang == 0:
            game.hero.monsterKilled -= self.rangAmount.get('rang1')
            game.hero.rang += 1
            game.hero.increaseHpBuff()
        elif game.hero.rang == 1:
            game.hero.monsterKilled -= self.rangAmount.get('rang2')
            game.hero.rang += 1
            game.hero.increaseMagicDmgBuff()
        elif game.hero.rang == 2:
            game.hero.monsterKilled -= self.rangAmount.get('rang2')
            game.hero.rang += 1
            game.hero.increaseDmgBuff()
        elif game.hero.rang == 3:
            game.hero.monsterKilled -= self.rangAmount.get('rang3')
            game.hero.rang += 1
            game.hero.increaseHpBuff()
        elif game.hero.rang == 4:
            game.hero.monsterKilled -= self.rangAmount.get('rang4')
            game.hero.rang += 1
            game.hero.increaseDmgBuff()
        elif game.hero.rang == 5:
            game.hero.monsterKilled -= self.rangAmount.get('rang5')
            game.hero.rang += 1
            game.hero.increaseDmgBuff()
        elif game.hero.rang == 6:
            game.hero.monsterKilled -= self.rangAmount.get('rang6')
            game.hero.rang += 1
            game.hero.increaseHpBuff()
        elif game.hero.rang == 7:
            game.hero.monsterKilled -= self.rangAmount.get('rang7')
            game.hero.rang += 1
            game.hero.increaseMagicDmgBuff()
        elif game.hero.rang == 8:
            game.hero.monsterKilled -= self.rangAmount.get('rang8')
            game.hero.rang += 1
            game.hero.increaseHpBuff()
        elif game.hero.rang == 9:
            game.hero.monsterKilled -= self.rangAmount.get('rang9')
            game.hero.rang += 1
            game.hero.increaseMagicDmgBuff()
        elif game.hero.rang == 10:
            game.hero.monsterKilled -= self.rangAmount.get('rang10')
            game.hero.rang += 1
            game.hero.increaseDmgBuff()