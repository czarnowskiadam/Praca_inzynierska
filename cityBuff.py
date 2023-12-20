import pygame
import random
import game
import resources as res

class Buffs(object):
    def __init__(self):
        self.options = ['Increase Damage', 'Increase HP', 'More XP', 'Increase M. Damage', 'Increase Souls Gain',
                        'Increase Gold Gain']
        self.selected = []
        self.cost = 5
        self.randomOptions()

    def randomOptions(self):
        for i in range(0, 3):
            x = random.randint(0, len(self.options)-1)
            self.selected.append(self.options[x])

    def result(self, num):
        return self.selected[num]

    def whatPicked(self, option):
        if option == 'Increase Damage':
            game.hero.increaseDmgBuff()
            game.hero.gold -= self.cost
        if option == 'Increase HP':
            game.hero.increaseHpBuff()
            game.hero.gold -= self.cost
        if option == 'More XP':
            game.hero.moreXpBuff()
            game.hero.gold -= self.cost
        if option == 'Increase M. Damage':
            game.hero.increaseMagicDmgBuff()
            game.hero.gold -= self.cost
        if option == 'Increase Souls Gain':
            game.hero.moreSoulsBuff()
            game.hero.gold -= self.cost
        if option == 'Increase Gold Gain':
            game.hero.moreGoldBuff()
            game.hero.gold -= self.cost
