import resources as res
import pygame
import game
import random
import enemy as en
import turns

# heroLvl = 1
# heroExp = 0
# heroRang = 0
# heroMaxExp = 10
# currentHP = 100
# maxHealthPoints = 100
# minDamage = 2
# maxDamage = 8
# minMagicDamage = 4
# maxMagicDamage = 10
# soulsGained = 0
# goldGained = 0
# monsterCounter = 0


heroStats = {
            'heroLvl': 1,
            'heroExp': 0,
            'heroRang': 0,
            'heroMaxExp': 10,
            'currentHP': 60,
            'maxHP': 60,
            'minDamage': 2,
            'maxDamage': 6,
            'minMagicDamage': 5,
            'maxMagicDamage': 7,
            'soulsGained': 0,
            'goldGained': 0,
            'monsterCounter': 0
        }

class Player:
    def __init__(self):
        self.scoreTable = []
        self.lvl = heroStats.get('heroLvl')
        self.exp = heroStats.get('heroExp')
        self.rang = heroStats.get('heroRang')
        self.maxExp = heroStats.get('heroMaxExp')
        self.currHP = heroStats.get('currentHP')
        self.maxHP = heroStats.get('maxHP')
        self.minDmg = heroStats.get('minDamage')
        self.maxDmg = heroStats.get('maxDamage')
        self.minMDmg = heroStats.get('minMagicDamage')
        self.maxMDmg = heroStats.get('maxMagicDamage')
        self.gold = heroStats.get('goldGained')
        self.souls = heroStats.get('soulsGained')
        self.monsterKilled = heroStats.get('monsterCounter')
        self.isDefence = False
        self.isRage = False
        self.isXpBuff = False
        self.isSoulsBuff = False
        self.isGoldBuff = False

    def updateStats(self):
        heroStats.update({'heroLvl': self.lvl})
        heroStats.update({'heroExp': self.exp})
        heroStats.update({'heroRang': self.rang})
        heroStats.update({'heroMaxExp': self.maxExp})
        heroStats.update({'currentHP': self.currHP})
        heroStats.update({'maxHP': self.maxHP})
        heroStats.update({'minDamage': self.minDmg})
        heroStats.update({'maxDamage': self.maxDmg})
        heroStats.update({'minMagicDamage': self.minMDmg})
        heroStats.update({'maxMagicDamage': self.maxMDmg})
        heroStats.update({'soulsGained': self.souls})
        heroStats.update({'goldGained': self.gold})
        heroStats.update({'monsterCounter': self.monsterKilled})

    def countScore(self):
        self.scoreTable.append(self.lvl * 5)
        self.scoreTable.append(self.rang * 5)
        self.scoreTable.append(self.souls * 10)
        self.scoreTable.append(self.gold * 2)
        self.scoreTable.append(self.monsterKilled * 2)
        score = sum(self.scoreTable)
        return score

    def reset(self):
        self.lvl = 0
        self.exp = 0
        self.maxExp = 10
        self.currHP = 60
        self.maxHP = 60
        self.minDmg = 2
        self.maxDmg = 6
        self.minMDmg = 5
        self.maxMDmg = 7

    def expUP(self, expRecived):
        if self.isXpBuff:
            self.exp += (expRecived + 2)
        else:
            self.exp += expRecived

        if self.exp < self.maxExp:
            pass
        else:
            self.lvl += 1
            self.exp = 0
            self.maxExp += 5
            self.minDmg += 2
            self.maxDmg += 2
            self.minMDmg += 3
            self.maxMDmg += 3
            self.maxHP += 10
            self.currHP = self.maxHP

    def lossHP(self, damageReceive):
        if self.isDefence:
            self.currHP -= round(damageReceive * 0.75)
            if self.currHP <= 0:
                if self.currHP < 0:
                    self.currHP = 0
            return round(damageReceive * 0.75)
        else:
            self.currHP -= damageReceive
            if self.currHP <= 0:
                if self.currHP < 0:
                    self.currHP = 0

            return damageReceive

    def onDamage(self):
        if self.isRage:
            dmg = round(random.randrange(self.minDmg, self.maxDmg + 1) * 1.5)
            return dmg
        else:
            dmg = random.randrange(self.minDmg, self.maxDmg + 1)
            return dmg

    def onMagicDamage(self):
        mDmg = random.randrange(self.minMDmg, self.maxMDmg + 1)
        return mDmg

    def heal(self):
        heal = random.randrange(round(self.maxHP * 0.04), round(self.maxHP * 0.12))
        if self.currHP == self.maxHP:
            pass
        elif (self.maxHP - self.currHP) < heal:
            heal = (self.maxHP - self.currHP)
            self.currHP += heal
        else:
            self.currHP += heal
        return heal

    def defense(self):
        self.isDefence = True

    def rage(self):
        self.isRage = True

    def drainDmg(self):
        mDmg = round(random.randrange(self.minMDmg, self.maxMDmg + 1) * 0.5)
        return mDmg

    def drainHeal(self):
        heal = round(random.randrange(round(self.maxHP * 0.02), round(self.maxHP * 0.08)) * 0.5)
        if self.currHP == self.maxHP:
            pass
        elif (self.maxHP - self.currHP) < heal:
            heal = (self.maxHP - self.currHP)
            self.currHP += heal
        else:
            self.currHP += heal
        return heal

    def bonfireHeal(self):
        heal = round(self.maxHP * 0.25)
        if self.currHP == self.maxHP:
            pass
        elif (self.maxHP - self.currHP) < heal:
            heal = (self.maxHP - self.currHP)
            self.currHP += heal
        else:
            self.currHP += heal
        return heal

    def addGold(self, amount):
        if self.isGoldBuff:
            self.gold += (amount + 2)
        else:
            self.gold += amount

    def addSouls(self, amount):
        if self.isSoulsBuff:
            self.souls += (amount + 2)
        else:
            self.souls += amount

    def increaseDmgBuff(self):
        self.minDmg += 2
        self.maxDmg += 2

    def increaseHpBuff(self):
        self.currHP += 10
        self.maxHP += 10

    def increaseMagicDmgBuff(self):
        self.minMDmg += 2
        self.maxMDmg += 2

    def moreXpBuff(self):
        self.isXpBuff = True

    def moreGoldBuff(self):
        self.isGoldBuff = True

    def moreSoulsBuff(self):
        self.isSoulsBuff = True

