import pygame
import resources as res
import game
import random
import turns
import animations as anim
import loot as lt

class Enemy:
    def __init__(self):
        self.loot = lt.Loot()
        self.difficultyLvl = 1
        ### Effect Status ###
        self.stunStatus = False
        self.absorbDamageStatus = False
        self.shieldStatus = False
        self.toxicStatus = False
        self.buffAttack = True
        self.bigBuffAttack = True
        self.curseStatus = False
        ### Enemies ###
        self.enemyList = ['slayer', 'minotaur', 'witch', 'golem', 'slayer']
        ### Bosses ###
        self.bossList = ['sorcerer', 'nightBorn']
        ### Enemies Statistics ###
        self.skeleton = {
            'currHP': 60,
            'maxHP': 60,
            'minDmg': 2,
            'maxDmg': 4,
            'reviveCounter': 0,
            'decreaseAttackCounter': 0,
            'deadStatus': 0
        }
        self.minotaur = {
            'currHP': 80,
            'maxHP': 80,
            'minDmg': 6,
            'maxDmg': 12,
            'healCounter': 3,
            'stunCounter': 3,
            'deadStatus': 0
        }
        self.witch = {
            'currHP': 45,
            'maxHP': 45,
            'minDmg': 6,
            'maxDmg': 14,
            'healCounter': 2,
            'deadStatus': 0
        }
        self.golem = {
            'currHP': 130,
            'maxHP': 130,
            'minDmg': 1,
            'maxDmg': 3,
            'shieldCounter': 0,
            'deadStatus': 0
        }
        self.slayer = {
            'currHP': 90,
            'maxHP': 90,
            'minDmg': 1,
            'maxDmg': 8,
            'toxicCounter': 0,
            'deadStatus': 0
        }
        ### Bosses Statistics ###
        self.sorcerer = {
            'currHP': 150,
            'maxHP': 150,
            'minDmg': 3,
            'maxDmg': 5,
            'curseCounter': 0,
            'deadStatus': 0
        }
        self.nightBorn = {
            'currHP': 110,
            'maxHP': 110,
            'minDmg': 3,
            'maxDmg': 7,
            'stunCounter': 0,
            'deadStatus': 0
        }

        if game.difficulty == 'Medium':
            self.difficultyLvl = 3
        elif game.difficulty == 'Hard':
            self.difficultyLvl = 5
        else:
            pass

        if not game.isBoss:
            self.randomEnemy = random.randrange(0, len(self.enemyList))

            if self.enemyList[self.randomEnemy] == 'skeleton':
                self.currHP = self.skeleton.get('currHP') + self.difficultyLvl
                self.maxHP = self.skeleton.get('maxHP') + self.difficultyLvl
                self.minDmg = self.skeleton.get('minDmg') + self.difficultyLvl
                self.maxDmg = self.skeleton.get('maxDmg') + self.difficultyLvl
                self.reviveCounter = self.skeleton.get('reviveCounter')
                self.decreaseAttackCounter = self.skeleton.get('decreaseAttackCounter')
                self.deadStatus = self.skeleton.get('deadStatus')
            elif self.enemyList[self.randomEnemy] == 'minotaur':
                self.currHP = self.minotaur.get('currHP') + self.difficultyLvl
                self.maxHP = self.minotaur.get('maxHP') + self.difficultyLvl
                self.minDmg = self.minotaur.get('minDmg') + self.difficultyLvl
                self.maxDmg = self.minotaur.get('maxDmg') + self.difficultyLvl
                self.healCounter = self.minotaur.get('healCounter')
                self.stunCounter = self.minotaur.get('stunCounter')
                self.deadStatus = self.minotaur.get('deadStatus')
            elif self.enemyList[self.randomEnemy] == 'witch':
                self.currHP = self.witch.get('currHP') + self.difficultyLvl
                self.maxHP = self.witch.get('maxHP') + self.difficultyLvl
                self.minDmg = self.witch.get('minDmg') + self.difficultyLvl
                self.maxDmg = self.witch.get('maxDmg') + self.difficultyLvl
                self.healCounter = self.witch.get('healCounter')
                self.deadStatus = self.witch.get('deadStatus')
            elif self.enemyList[self.randomEnemy] == 'golem':
                self.currHP = self.golem.get('currHP') + self.difficultyLvl
                self.maxHP = self.golem.get('maxHP') + self.difficultyLvl
                self.minDmg = self.golem.get('minDmg') + self.difficultyLvl
                self.maxDmg = self.golem.get('maxDmg') + self.difficultyLvl
                self.shieldCounter = self.golem.get('shieldCounter')
                self.deadStatus = self.golem.get('deadStatus')
            elif self.enemyList[self.randomEnemy] == 'slayer':
                self.currHP = self.slayer.get('currHP') + self.difficultyLvl
                self.maxHP = self.slayer.get('maxHP') + self.difficultyLvl
                self.minDmg = self.slayer.get('minDmg') + self.difficultyLvl
                self.maxDmg = self.slayer.get('maxDmg') + self.difficultyLvl
                self.toxicCounter = self.slayer.get('toxicCounter')
                self.deadStatus = self.slayer.get('deadStatus')
        else:
            self.randomBoss = random.randrange(0, len(self.bossList))
            if self.bossList[self.randomBoss] == 'sorcerer':
                self.currHP = self.sorcerer.get('currHP') + self.difficultyLvl
                self.maxHP = self.sorcerer.get('maxHP') + self.difficultyLvl
                self.minDmg = self.sorcerer.get('minDmg') + self.difficultyLvl
                self.maxDmg = self.sorcerer.get('maxDmg') + self.difficultyLvl
                self.curseCounter = self.sorcerer.get('curseCounter')
                self.deadStatus = self.sorcerer.get('deadStatus')
            elif self.bossList[self.randomBoss] == 'nightBorn':
                self.currHP = self.nightBorn.get('currHP') + self.difficultyLvl
                self.maxHP = self.nightBorn.get('maxHP') + self.difficultyLvl
                self.minDmg = self.nightBorn.get('minDmg') + self.difficultyLvl
                self.maxDmg = self.nightBorn.get('maxDmg') + self.difficultyLvl
                self.stunCounter = self.nightBorn.get('stunCounter')
                self.deadStatus = self.nightBorn.get('deadStatus')

    def getEnemyName(self):
        if not game.isBoss:
            return self.enemyList[self.randomEnemy]
        else:
            return self.bossList[self.randomBoss]

    def lossHP(self, damageReceive):
        if self.absorbDamageStatus:
            self.currHP -= round(damageReceive * 0.75)
        elif self.shieldStatus:
            damageReceive = 0
        else:
            self.currHP -= damageReceive

        if self.currHP <= 0:
            if self.currHP < 0:
                self.currHP = 0
        return damageReceive

    def onDamage(self):
        dmg = random.randrange(self.minDmg, self.maxDmg + 1)
        return dmg

    ### Skills ###

    def reviveSkill(self):
        if self.currHP == 0:
            heal = round(self.maxHP/2)
            self.currHP += heal

    def decreaseAttackSkill(self):
        if self.decreaseAttackCounter == 0:
            game.hero.minDmg = round(game.hero.minDmg * 0.75)
            game.hero.maxDmg = round(game.hero.maxDmg * 0.75)
            game.hero.minMDmg = round(game.hero.minMDmg * 0.75)
            game.hero.maxMDmg = round(game.hero.maxMDmg * 0.75)
            self.decreaseAttackCounter = 1

    def resetHeroAttack(self):
        if self.decreaseAttackCounter != 0:
            game.hero.minDmg = round(game.hero.minDmg / 0.75)
            game.hero.maxDmg = round(game.hero.maxDmg / 0.75)
            game.hero.minMDmg = round(game.hero.minMDmg / 0.75)
            game.hero.maxMDmg = round(game.hero.maxMDmg / 0.75)

    def healSkill(self):
        if self.getEnemyName() == 'minotaur':
            heal = random.randint(8, 15)
            self.currHP += heal
        elif self.getEnemyName() == 'witch':
            heal = random.randint(4, 9)
            self.currHP += heal
        self.healCounter = 0

    def stunSkill(self):
        self.stunStatus = True
        self.stunCounter = 0

    def drainSkill(self):
        amount = random.randint(self.minDmg, self.maxDmg)
        game.hero.lossHP(amount)
        self.currHP += amount

    ### Skeleton ###

    def skeletonAI(self):
        if self.currHP <= 0:
            if self.reviveCounter == 0:
                self.reviveSkill()
                self.reviveCounter = 1
                game.enemyAnimations.state = 1
                game.fightTurn.endTurn()

            else:
                self.deadStatus = 1
                game.enemyAnimations.state = 3
                if self.decreaseAttackCounter != 0:
                    self.resetHeroAttack()
                self.loot.loot(self.getEnemyName())
                game.hero.monsterKilled += 1

        else:
            if self.currHP >= self.maxHP/2:
                game.hero.lossHP(self.onDamage())
                game.enemyAnimations.state = 2
                game.fightTurn.endTurn()
            else:
                if self.decreaseAttackCounter == 0:
                    self.decreaseAttackSkill()
                    game.fightTurn.endTurn()
                else:
                    game.hero.lossHP(self.onDamage())
                    game.enemyAnimations.state = 2
                    game.fightTurn.endTurn()

    ### Minotaur ###

    def minotaurAI(self):
        self.stunStatus = False

        if self.currHP <= 0:
            game.enemyAnimations.state = 4
            self.deadStatus = 1
            self.loot.loot(self.getEnemyName())
            game.hero.monsterKilled += 1
        else:
            if self.healCounter == 3 and self.currHP <= self.maxHP * 0.6:
                game.enemyAnimations.state = 3
                self.healSkill()
                if self.stunCounter == 3:
                    pass
                else:
                    self.stunCounter += 1
                game.fightTurn.endTurn()
            else:
                if self.stunCounter == 3 and self.currHP <= self.maxHP * 0.3:
                    self.stunSkill()
                    game.enemyAnimations.state = 2
                    if self.healCounter == 2:
                        pass
                    else:
                        self.healCounter += 1
                    game.fightTurn.endTurn()
                else:
                    game.hero.lossHP(self.onDamage())
                    game.enemyAnimations.state = 1
                    if self.healCounter == 3:
                        pass
                    else:
                        self.healCounter += 1
                    if self.stunCounter == 3:
                        pass
                    else:
                        self.stunCounter += 1
                    game.fightTurn.endTurn()

    ### Witch ###

    def witchAI(self):
        if self.currHP <= 0:
            game.enemyAnimations.state = 3
            self.deadStatus = 1
            self.loot.loot(self.getEnemyName())
            game.hero.monsterKilled += 1
        else:
            if self.healCounter == 2 and self.currHP <= self.maxHP * 0.5:
                game.enemyAnimations.state = 2
                self.healSkill()
                game.fightTurn.endTurn()
            else:
                if game.hero.currHP <= round(game.hero.maxHP * 0.2):
                    game.enemyAnimations.state = 1
                    game.hero.lossHP(game.hero.currHP)
                    game.hero.lossHP(game.hero.currHP)
                    game.fightTurn.endTurn()
                else:
                    game.hero.lossHP(self.onDamage())
                    game.enemyAnimations.state = 1
                    if self.healCounter == 2:
                        pass
                    else:
                        self.healCounter += 1
                    game.fightTurn.endTurn()

    ### Golem ###

    def golemAI(self):
        if self.currHP <= 0:
            game.enemyAnimations.state = 3
            self.deadStatus = 1
            self.loot.loot(self.getEnemyName())
            game.hero.monsterKilled += 1
        else:
            if self.shieldCounter == 3:
                game.enemyAnimations.state = 2
                self.shieldStatus = True
                self.shieldCounter = 0
                game.fightTurn.endTurn()
            else:
                self.shieldCounter += 1
                if self.shieldCounter == 2:
                    self.shieldStatus = False
                if self.currHP <= round(self.maxHP * 0.4):
                    self.minDmg += 2
                    self.maxDmg += 2
                game.enemyAnimations.state = 1
                game.hero.lossHP(self.onDamage())
                game.fightTurn.endTurn()

    ### Slayer ###

    def slayerAI(self):
        if self.toxicStatus:
            game.hero.lossHP(5)

        if self.currHP <= 0:
            game.enemyAnimations.state = 4
            self.deadStatus = 1
            self.loot.loot(self.getEnemyName())
            game.hero.monsterKilled += 1
        else:
            if self.toxicCounter == 6:
                game.enemyAnimations.state = 3
                self.toxicStatus = True
                self.toxicCounter = 0
                game.fightTurn.endTurn()
            else:
                self.toxicCounter += 1
                if self.toxicCounter == 3:
                    self.toxicStatus = False
                if self.currHP <= round(self.maxHP * 0.5):
                    game.enemyAnimations.state = 2
                    self.drainSkill()
                    game.fightTurn.endTurn()
                else:
                    game.enemyAnimations.state = 1
                    game.hero.lossHP(self.onDamage())
                    game.fightTurn.endTurn()

    ### Sorcerer ###

    def sorcererAI(self):
        if self.currHP <= 0:
            game.enemyAnimations.state = 3
            self.deadStatus = 1
            self.loot.loot(self.getEnemyName())
            game.hero.monsterKilled += 5
        else:
            if self.curseCounter == 6:
                game.enemyAnimations.state = 2
                self.curseStatus = True
                self.curseCounter = 0
                game.fightTurn.endTurn()
            else:
                if self.curseCounter == 3:
                    self.curseStatus = False
                self.curseCounter += 1
                if self.currHP <= self.maxHP * 0.3 and self.bigBuffAttack:
                    self.minDmg += 8
                    self.maxDmg += 8
                    self.bigBuffAttack = False
                    game.fightTurn.endTurn()
                elif self.currHP <= self.maxHP * 0.6 and self.buffAttack:
                    self.minDmg += 3
                    self.maxDmg += 3
                    self.buffAttack = False
                    game.fightTurn.endTurn()
                else:
                    game.enemyAnimations.state = 1
                    game.hero.lossHP(self.onDamage())
                    game.fightTurn.endTurn()

    ### NightBorn ###

    def nightBornAI(self):
        if self.currHP <= 0:
            game.enemyAnimations.state = 3
            self.deadStatus = 1
            self.loot.loot(self.getEnemyName())
            game.hero.monsterKilled += 5
        else:
            if self.stunCounter == 4:
                game.enemyAnimations.state = 2
                self.stunStatus = True
                self.stunCounter = 0
                game.fightTurn.endTurn()
            else:
                if self.stunCounter == 2:
                    self.stunStatus = False
                self.stunCounter += 1
                if self.currHP <= self.maxHP * 0.25:
                    game.enemyAnimations.state = 1
                    amount = self.onDamage()
                    game.hero.lossHP(amount)
                    self.currHP += amount
                    game.hero.lossHP(amount)
                    self.currHP += amount
                    game.fightTurn.endTurn()
                else:
                    game.enemyAnimations.state = 1
                    game.hero.lossHP(self.onDamage())
                    game.hero.lossHP(self.onDamage())
                    game.fightTurn.endTurn()
