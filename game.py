import sys
import pygame
import save
import controlUI as cui
import resources as res
import player as pl
import enemy as en
import turns
import mapGenerator as mg
import time
import testLuckGame as tlg
import cityBuff
import cactus
import treasure as tr
import animations as anim
import huntingHut as hh
import score
import miniGame
import equipment as eq
import math
import random

### Pygame init ###
gameClock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption('SoulCollector')
windowSize = (1360, 768)
screen = pygame.display.set_mode(windowSize, 0, 32)

save.readSave()
save.readCactusSave()
save.readGlorySave()

timeStart = 0

hero = pl.Player()

fightTurn = turns.Turn()

cactus = cactus.Cactus()

hunt = hh.HuntingHut()

gameMap = mg.Generator()

treasure = tr.Treasure()

playerAnimations = anim.PlayerAnimations()
enemyAnimations = anim.EnemyAnimations()

isBoss = False

difficulty = 'Easy'

def mapPosition(pos):
    if pos == 'Fight':
        fightScreen()
    if pos == 'Bonfire':
        bonfireMap()
    if pos == 'Treasure':
        treasureMap()
    if pos == 'Luck Test':
        x = random.randint(0, 1)
        if x == 0:
            luckTestMap()
        else:
            miniGameScreen()
    if pos == 'Boss':
        fightScreen()

### Menu ###

def startScreen():
    startButton = cui.Button(screen, 50, 350, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                             'Play')
    optionsButton = cui.Button(screen, 50, 450, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                               'Options')
    exitButton = cui.Button(screen, 50, 550, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True, 'Quit')

    while True:
        screen.blit(res.bgMenu, (0, 0))
        res.textSetting(screen, (500, 250), res.pixelTitleFont, res.menuTextColour, 'SoulCollector')

        if startButton.drawButton():
            gameScreen()
        if optionsButton.drawButton():
            optionsScreen()
        if exitButton.drawButton():
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        gameClock.tick(60)

### Options ###

def optionsScreen():
    global difficulty
    run = True
    exitButton = cui.Button(screen, 1150, 650, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            'Exit')
    difficultyEasyButton = cui.Button(screen, 500, 200, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            'Easy')
    difficultyMediumButton = cui.Button(screen, 700, 200, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                                  'Medium')
    difficultyHardButton = cui.Button(screen, 900, 200, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                                  'Hard')

    while run:
        screen.fill((0, 0, 0))
        res.textSetting(screen, (550, 100), res.pixelTitleFont, res.menuTextColour, 'Options')
        res.textSetting(screen, (200, 225), res.pixelFont, res.menuTextColour, f'Difficulty: {difficulty}')

        if exitButton.drawButton():
            run = False

        if difficultyEasyButton.drawButton():
            difficulty = 'Easy'
        if difficultyMediumButton.drawButton():
            difficulty = 'Medium'
        if difficultyHardButton.drawButton():
            difficulty = 'Hard'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        pygame.display.update()
        gameClock.tick(60)

### Game ###

def gameScreen():

    expeditionButton = cui.Button(screen, 615, 560, res.cityTextColour, res.cityTextColourClicked, res.pixelCityFont,
                                  False, 'Expedition')
    homeButton = cui.Button(screen, 460, 360, res.cityTextColour, res.cityTextColourClicked, res.pixelCityFont, False,
                            'Home')
    magicButton = cui.Button(screen, 400, 230, res.cityTextColour, res.cityTextColourClicked, res.pixelCityFont, False,
                             'Magic Buffs')
    healingButton = cui.Button(screen, 530, 205, res.cityTextColour, res.cityTextColourClicked, res.pixelCityFont,
                               False, 'Healing')
    gloryButton = cui.Button(screen, 710, 350, res.cityTextColour, res.cityTextColourClicked, res.pixelCityFont, False,
                             'Hall of Glory')
    huntingHutButton = cui.Button(screen, 750, 235, res.cityTextColour, res.cityTextColourClicked, res.pixelCityFont,
                                False, 'Hunting Hut')

    gameMap.__init__()
    while True:
        screen.blit(res.bgCity, (0, 0))
        res.balance(screen)

        if expeditionButton.drawButton():
            spawnMap()
        if homeButton.drawButton():
            homeScreen()
        if magicButton.drawButton():
            cityBuffs()
        if healingButton.drawButton():
            healingCentre()
        if gloryButton.drawButton():
            glory()
        if huntingHutButton.drawButton():
            huntHut()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save.makeSave()
                pygame.quit()
                sys.exit()

        pygame.display.update()
        gameClock.tick(60)

### Fight ###

def fightScreen():
    global isBoss
    run = True
    isEquipmentOn = False

    nextButton = cui.Button(screen, 1150, 350, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            'Next')

    attackButton = cui.Button(screen, 340, 520, res.menuTextColour, res.menuTextColourClicked, res.explorationFont,
                              True, 'Attack')
    magicAttackButton = cui.Button(screen, 570, 520, res.menuTextColour, res.menuTextColourClicked, res.explorationFont,
                                   True, 'Magic Attack')
    defenceButton = cui.Button(screen, 340, 600, res.menuTextColour, res.menuTextColourClicked, res.explorationFont,
                               True, 'Defence')
    healButton = cui.Button(screen, 570, 600, res.menuTextColour, res.menuTextColourClicked, res.explorationFont, True,
                            'Heal')
    skillOneButton = cui.Button(screen, 340, 680, res.menuTextColour, res.menuTextColourClicked, res.explorationFont,
                                True, 'Rage')
    skillTwoButton = cui.Button(screen, 570, 680, res.menuTextColour, res.menuTextColourClicked, res.explorationFont,
                                True, 'Drain')
    equipmentButton = cui.Button(screen, 10, 350, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                                 'EQ')

    enemy = en.Enemy()

    while run:
        screen.blit(res.explorationHUD, (0, 0))

        cui.heroInfo(screen, hero.lvl, hero.exp, hero.maxExp, hero.rang)
        cui.heroStatistics(screen, hero.currHP, hero.maxHP, hero.minDmg, hero.maxDmg, hero.minMDmg, hero.maxMDmg)
        cui.expeditionEnemy(screen)
        cui.expeditionActions(screen)
        cui.enemyInfo(screen, enemy.getEnemyName(), enemy.currHP, enemy.maxHP, enemy.minDmg, enemy.maxDmg)

        res.textSetting(screen, (150, 50), res.pixelTitleFont, res.green, f'{hero.currHP}/{hero.maxHP}')
        res.textSetting(screen, (1000, 50), res.pixelTitleFont, res.red, f'{enemy.currHP}/{enemy.maxHP}')

        if playerAnimations.state == 0:
            playerAnimations.updateIdleAnimation()
            playerAnimations.displayIdleAnimation()
        elif playerAnimations.state == 1:
            playerAnimations.updateAttackAnimation()
            playerAnimations.displayAttackAnimation()
        elif playerAnimations.state == 2:
            playerAnimations.updateDefAnimation()
            playerAnimations.displayDefAnimation()

        enemyAnimations.currentDisplayAnimation(enemy)

        if fightTurn.getTurn() == 1 and enemyAnimations.state == 0:
            if enemy.deadStatus == 0:
                cui.fightTurn(screen, fightTurn.getTurn(), (600, 50))
                if enemy.stunStatus:
                    fightTurn.endTurn()
                if enemy.curseStatus:
                    hero.lossHP(3)
                    fightTurn.endTurn()

                if attackButton.drawButton():
                    playerAnimations.state = 1
                    enemy.lossHP(hero.onDamage())
                if magicAttackButton.drawButton():
                    playerAnimations.state = 1
                    enemy.lossHP(hero.onMagicDamage())
                if defenceButton.drawButton():
                    playerAnimations.state = 2
                    hero.defense()
                if healButton.drawButton():
                    playerAnimations.state = 2
                    hero.heal()
                if skillOneButton.drawButton():
                    playerAnimations.state = 2
                    hero.rage()
                if skillTwoButton.drawButton():
                    playerAnimations.state = 1
                    enemy.lossHP(hero.drainDmg())
                    hero.drainHeal()

        if fightTurn.getTurn() == 2:
            if enemy.deadStatus == 0:
                cui.fightTurn(screen, fightTurn.getTurn(), (600, 50))
                if enemy.getEnemyName() == 'skeleton':
                    enemy.skeletonAI()
                elif enemy.getEnemyName() == 'minotaur':
                    enemy.minotaurAI()
                elif enemy.getEnemyName() == 'witch':
                    enemy.absorbDamageStatus = True
                    enemy.witchAI()
                elif enemy.getEnemyName() == 'golem':
                    enemy.golemAI()
                elif enemy.getEnemyName() == 'slayer':
                    enemy.slayerAI()
                elif enemy.getEnemyName() == 'sorcerer' and isBoss:
                    enemy.sorcererAI()
                elif enemy.getEnemyName() == 'nightBorn' and isBoss:
                    enemy.nightBornAI()

        if enemy.deadStatus != 0:
            startTime = time.time()
            if time.time() < startTime + 2:
                res.textSetting(screen, (480, 40), res.pixelFont, res.green, f'Exp: +{enemy.loot.getLoot(0)}'
                                                                             f' Gold: +{enemy.loot.getLoot(1)}'
                                                                             f' Souls: +{enemy.loot.getLoot(2)}')
            if nextButton.drawButton():
                if isBoss:
                    isBoss = False
                    save.makeSave()
                    gameMap.reset()
                    victory()
                else:
                    save.makeSave()
                    gameMap.nextStage()
                    run = False

        if hero.currHP <= 0:
            defeat()

        if equipmentButton.drawButton():
            if isEquipmentOn:
                isEquipmentOn = False
            else:
                isEquipmentOn = True

        if isEquipmentOn:
            eq.equipment(screen)
        else:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        pygame.display.update()
        gameClock.tick(60)

### Map ###

def spawnMap():
    global isBoss
    run = True
    stages = gameMap.getStages()

    stage1 = cui.Button(screen, 100, 300, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                             str(stages[0]))
    stage2 = cui.Button(screen, 350, 300, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                        str(stages[1]))
    stage3 = cui.Button(screen, 600, 300, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                        str(stages[2]))
    stage4 = cui.Button(screen, 850, 300, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                        str(stages[3]))
    stage5 = cui.Button(screen, 1100, 300, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                        str(stages[4]))
    stage6 = cui.Button(screen, 1100, 600, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                        str(stages[5]))
    stage7 = cui.Button(screen, 850, 600, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                        str(stages[6]))
    stage8 = cui.Button(screen, 600, 600, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                        str(stages[7]))
    stage9 = cui.Button(screen, 350, 600, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                        str(stages[8]))
    stage10 = cui.Button(screen, 100, 600, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                        str(stages[9]))

    isEquipmentOn = False

    equipmentButton = cui.Button(screen, 10, 10, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                                 'EQ')

    while run:
        screen.blit(res.mapBackground, (0, 0))
        res.textSetting(screen, (600, 50), res.pixelTitleFont, res.menuTextColour, 'MAP')
        res.mapLines(screen)
        res.arrowMap(screen, gameMap.getStage())

        heroPos = gameMap.getPos()

        if stage1.drawButton() and gameMap.getStage() == 0:
            mapPosition(heroPos)
        if stage2.drawButton() and gameMap.getStage() == 1:
            mapPosition(heroPos)
        if stage3.drawButton() and gameMap.getStage() == 2:
            mapPosition(heroPos)
        if stage4.drawButton() and gameMap.getStage() == 3:
            mapPosition(heroPos)
        if stage5.drawButton() and gameMap.getStage() == 4:
            mapPosition(heroPos)
        if stage6.drawButton() and gameMap.getStage() == 5:
            mapPosition(heroPos)
        if stage7.drawButton() and gameMap.getStage() == 6:
            mapPosition(heroPos)
        if stage8.drawButton() and gameMap.getStage() == 7:
            mapPosition(heroPos)
        if stage9.drawButton() and gameMap.getStage() == 8:
            mapPosition(heroPos)
        if stage10.drawButton() and gameMap.getStage() == 9:
            isBoss = True
            mapPosition(heroPos)

        if equipmentButton.drawButton():
            if isEquipmentOn:
                isEquipmentOn = False
            else:
                isEquipmentOn = True

        if isEquipmentOn:
            eq.equipment(screen)
        else:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save.makeSave()
                pygame.quit()
                sys.exit()

        pygame.display.update()
        gameClock.tick(60)

### Bonfire ###

def bonfireMap():
    global timeStart
    heal = 0
    run = True
    bonfire = True
    isEquipmentOn = False

    nextButton = cui.Button(screen, 1100, 350, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                             'Next')
    bonfireButton = cui.Button(screen, 550, 650, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            'Use')
    equipmentButton = cui.Button(screen, 10, 10, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                                 'EQ')

    while run:
        screen.blit(res.bonfireImg, (0, 0))
        res.textSetting(screen, (550, 50), res.pixelTitleFont, res.menuTextColour, 'BONFIRE')

        if nextButton.drawButton():
            save.makeSave()
            gameMap.nextStage()
            run = False
        if bonfire:
            if bonfireButton.drawButton():
                timeStart = time.time()
                heal = hero.bonfireHeal()
                bonfire = False

        if time.time() < timeStart + 2:
            res.textSetting(screen, (50, 50), res.notificationFont, res.green, f'Healed: {heal}')

        if equipmentButton.drawButton():
            if isEquipmentOn:
                isEquipmentOn = False
            else:
                isEquipmentOn = True

        if isEquipmentOn:
            eq.equipment(screen)
        else:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save.makeSave()
                pygame.quit()
                sys.exit()

        pygame.display.update()
        gameClock.tick(60)

### Try Your Luck ###

def luckTestMap():
    run = True
    addReward = True

    nextButton = cui.Button(screen, 1100, 350, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                             'Next')

    oneButton = cui.Button(screen, 395, 520, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            '1')
    twoButton = cui.Button(screen, 582, 520, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            '2')
    threeButton = cui.Button(screen, 768, 520, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            '3')
    fourButton = cui.Button(screen, 395, 600, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            '4')
    fiveButton = cui.Button(screen, 582, 600, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            '5')
    sixButton = cui.Button(screen, 768, 600, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            '6')
    sevenButton = cui.Button(screen, 395, 680, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            '7')
    eightButton = cui.Button(screen, 582, 680, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            '8')
    nineButton = cui.Button(screen, 768, 680, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            '9')

    luckGame = tlg.LuckTest()
    gameTurn = turns.Turn()

    while run:
        screen.blit(res.testLuckImg, (0, 0))
        res.textSetting(screen, (200, 25), res.notificationFont, res.menuTextColour, 'Pick 3 of 9 tiles, if You get higher result than Magic Wizard - You win!')
        luckGame.displayTiles()

        res.textSetting(screen, (20, 140), res.notificationFont, res.green,
                        f'Your Score: {luckGame.sumPlayerResult()}')
        res.textSetting(screen, (20, 180), res.notificationFont, res.red,
                        f'Wizard Score: {luckGame.sumComResult()}')

        if len(luckGame.playerResult) < 3:
            if gameTurn.getTurn() == 1:
                if luckGame.getClickedTile(0) == 0:
                    if oneButton.drawButton():
                        luckGame.playerTurnAction(0)
                        gameTurn.endTurn()
                if luckGame.getClickedTile(1) == 0:
                    if twoButton.drawButton():
                        luckGame.playerTurnAction(1)
                        gameTurn.endTurn()
                if luckGame.getClickedTile(2) == 0:
                    if threeButton.drawButton():
                        luckGame.playerTurnAction(2)
                        gameTurn.endTurn()
                if luckGame.getClickedTile(3) == 0:
                    if fourButton.drawButton():
                        luckGame.playerTurnAction(3)
                        gameTurn.endTurn()
                if luckGame.getClickedTile(4) == 0:
                    if fiveButton.drawButton():
                        luckGame.playerTurnAction(4)
                        gameTurn.endTurn()
                if luckGame.getClickedTile(5) == 0:
                    if sixButton.drawButton():
                        luckGame.playerTurnAction(5)
                        gameTurn.endTurn()
                if luckGame.getClickedTile(6) == 0:
                    if sevenButton.drawButton():
                        luckGame.playerTurnAction(6)
                        gameTurn.endTurn()
                if luckGame.getClickedTile(7) == 0:
                    if eightButton.drawButton():
                        luckGame.playerTurnAction(7)
                        gameTurn.endTurn()
                if luckGame.getClickedTile(8) == 0:
                    if nineButton.drawButton():
                        luckGame.playerTurnAction(8)
                        gameTurn.endTurn()

        if len(luckGame.comResult) < 3:
            if gameTurn.getTurn() == 2:
                res.textSetting(screen, (20, 140), res.notificationFont, res.green,
                                f'Your Score: {luckGame.sumPlayerResult()}')
                res.textSetting(screen, (20, 180), res.notificationFont, res.red,
                                f'Wizard Score: {luckGame.sumComResult()}')
                luckGame.comTurnAction()
                gameTurn.endTurn()

        if len(luckGame.playerResult) == 3 and len(luckGame.comResult) == 3:
            res.textSetting(screen, (540, 550), res.pixelTitleFont, res.menuTextColour,
                            f'{luckGame.finalResult()}')
            if luckGame.finalResult() == 'You won!':
                res.textSetting(screen, (560, 620), res.pixelFont, res.menuTextColour,
                                f'Reward: {luckGame.gameReward()}G')
            elif luckGame.finalResult() == 'You lose!':
                res.textSetting(screen, (540, 620), res.pixelFont, res.menuTextColour,
                                f'Wizard takes 15G')

            if addReward:
                if luckGame.finalResult() == 'You won!':
                    hero.gold += luckGame.gameReward()
                    addReward = False
                elif luckGame.finalResult() == 'You lose!':
                    if hero.gold < 15:
                        hero.gold = 0
                        addReward = False
                    else:
                        hero.gold -= 15
                        addReward = False
                else:
                    pass

            if nextButton.drawButton():
                save.makeSave()
                gameMap.nextStage()
                run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save.makeSave()
                pygame.quit()
                sys.exit()

        pygame.display.update()
        gameClock.tick(60)

### Treasure ###

def treasureMap():
    global timeStart
    run = True
    isTaken = True
    isEquipmentOn = False

    treasure.__init__()

    nextButton = cui.Button(screen, 1150, 350, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                             'Next')
    treasureButton = cui.Button(screen, 550, 650, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                                   'Open')
    equipmentButton = cui.Button(screen, 10, 10, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                                   'EQ')

    while run:
        screen.blit(res.treasureRoom, (0, 0))

        if nextButton.drawButton():
            save.makeSave()
            gameMap.nextStage()
            run = False

        if isTaken:
            screen.blit(res.closedChest, (570, 280))
            if treasureButton.drawButton():
                timeStart = time.time()
                treasure.openTreasure()
                treasure.addStats()
                isTaken = False
        else:
            screen.blit(res.openedChest, (570, 280))

        if time.time() < timeStart + 2:
            tempItem = treasure.lootGet()
            if len(tempItem) == 1:
                res.textSetting(screen, (50, 50), res.notificationFont, res.green, f'Item get: {tempItem[0]}')
            elif len(tempItem) == 2:
                res.textSetting(screen, (50, 50), res.notificationFont, res.green, f'Item get: {tempItem[0]}, {tempItem[1]}')
            elif len(tempItem) == 3:
                res.textSetting(screen, (50, 50), res.notificationFont, res.green, f'Item get: {tempItem[0]}, {tempItem[1]}, {tempItem[2]}')

        if equipmentButton.drawButton():
            if isEquipmentOn:
                isEquipmentOn = False
            else:
                isEquipmentOn = True

        if isEquipmentOn:
            eq.equipment(screen)
        else:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save.makeSave()
                pygame.quit()
                sys.exit()

        pygame.display.update()
        gameClock.tick(60)

### City Buffs ###

def cityBuffs():
    global timeStart
    run = True
    buff = True
    noGold = False

    exitButton = cui.Button(screen, 1120, 660, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            'Exit')
    optionOneButton = cui.Button(screen, 300, 670, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            'Take')
    optionTwoButton = cui.Button(screen, 580, 670, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                                 'Take')
    optionThreeButton = cui.Button(screen, 860, 670, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                                 'Take')

    options = cityBuff.Buffs()

    while run:
        screen.blit(res.buffShop, (0, 0))
        res.balance(screen)

        if exitButton.drawButton():
            save.makeSave()
            run = False

        if buff:
            res.threeOptions(screen)
            res.textSetting(screen, (290, 510), res.pixelBuffFont, res.menuTextColour, options.result(0))
            res.textSetting(screen, (350, 570), res.pixelBuffFont, res.menuTextColour, f'Cost: {options.cost}G')
            res.textSetting(screen, (575, 510), res.pixelBuffFont, res.menuTextColour, options.result(1))
            res.textSetting(screen, (635, 570), res.pixelBuffFont, res.menuTextColour, f'Cost: {options.cost}G')
            res.textSetting(screen, (850, 510), res.pixelBuffFont, res.menuTextColour, options.result(2))
            res.textSetting(screen, (920, 570), res.pixelBuffFont, res.menuTextColour, f'Cost: {options.cost}G')

            if optionOneButton.drawButton():
                timeStart = time.time()
                if hero.gold >= options.cost:
                    options.whatPicked(options.result(0))
                    buff = False
                else:
                    noGold = True
            if optionTwoButton.drawButton():
                timeStart = time.time()
                if hero.gold >= options.cost:
                    options.whatPicked(options.result(1))
                    buff = False
                else:
                    noGold = True
            if optionThreeButton.drawButton():
                timeStart = time.time()
                if hero.gold >= options.cost:
                    options.whatPicked(options.result(2))
                    buff = False
                else:
                    noGold = True
        else:
            res.textSetting(screen, (450, 500), res.pixelFont, res.menuTextColour, 'Good luck and see you soon!')

        if noGold:
            if time.time() < timeStart + 2:
                res.textSetting(screen, (10, 10), res.pixelBuffFont, res.red, 'Not enough Gold!')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save.makeSave()
                pygame.quit()
                sys.exit()

        pygame.display.update()
        gameClock.tick(60)

### Healing Centre ###

def healingCentre():
    global timeStart
    run = True
    noGold = False
    healed = 0

    low = (10, 5)
    medium = (25 ,10)
    high = (hero.maxHP, 25)

    exitButton = cui.Button(screen, 1120, 660, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            'Exit')

    optionOneButton = cui.Button(screen, 300, 670, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                                 'Heal')
    optionTwoButton = cui.Button(screen, 580, 670, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                                 'Heal')
    optionThreeButton = cui.Button(screen, 860, 670, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                                   'Heal')

    while run:
        screen.blit(res.healingCentre, (0, 0))
        res.balance(screen)
        res.threeOptions(screen)
        cui.healingCentreText(screen, low, medium, high)

        if exitButton.drawButton():
            save.makeSave()
            run = False

        if optionOneButton.drawButton():
            timeStart = time.time()
            if hero.gold >= low[1]:
                hero.currHP += low[0]
                healed = low[0]
                hero.gold -= low[1]
            else:
                noGold = True
        if optionTwoButton.drawButton():
            timeStart = time.time()
            if hero.gold >= medium[1]:
                hero.currHP += medium[0]
                healed = medium[0]
                hero.gold -= medium[1]
            else:
                noGold = True
        if optionThreeButton.drawButton():
            timeStart = time.time()
            if hero.gold >= high[1]:
                hero.currHP = high[0]
                healed = high[0]
                hero.gold -= high[1]
            else:
                noGold = True

        if noGold:
            if time.time() < timeStart + 2:
                res.textSetting(screen, (10, 10), res.pixelBuffFont, res.red, 'Not enough Gold!')
        else:
            if time.time() < timeStart + 2:
                res.textSetting(screen, (10, 10), res.pixelBuffFont, res.green, f'Healed: {healed}HP')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save.makeSave()
                pygame.quit()
                sys.exit()

        pygame.display.update()
        gameClock.tick(60)

### Home ###

def homeScreen():
    global timeStart
    run = True
    exitButton = cui.Button(screen, 1120, 660, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            'Exit')

    feedButton = cui.Button(screen, 580, 600, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            'Feed')

    while run:
        screen.blit(res.home, (0, 0))
        res.balance(screen)

        cactus.info()

        if exitButton.drawButton():
            save.makeSave()
            save.makeCactusSave()
            run = False

        if cactus.lvlGet() <= 7:
            res.textSetting(screen, (230, 500), res.notificationFont, res.menuTextColour,
                            'Feeding Your cactus with souls grants You in game bonuses!')
            if feedButton.drawButton():
                timeStart = time.time()
                cactus.leveling(cactus.lvlGet())
        else:
            res.textSetting(screen, (350, 500), res.notificationFont, res.menuTextColour,
                            'Your cactus grants You all possible bonuses!')

        if hero.souls < cactus.lvlReq[cactus.lvlGet()]:
            if time.time() < timeStart + 2:
                res.textSetting(screen, (10, 10), res.pixelBuffFont, res.red, 'Not enough Souls!')


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save.makeSave()
                save.makeCactusSave()
                pygame.quit()
                sys.exit()

        pygame.display.update()
        gameClock.tick(60)

### Hunting Hut ###

def huntHut():
    run = True

    exitButton = cui.Button(screen, 1100, 650, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            'Exit')
    sacrificeButton = cui.Button(screen, 580, 660, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            'Sacrifice')

    while run:
        screen.blit(res.huntingHut, (0, 0))
        res.textSetting(screen, (250, 50), res.pixelFont, res.menuTextColour, 'Sacrifice killed monsters to rang up and buff Your hero!')
        res.textSetting(screen, (50, 600), res.pixelFont, res.menuTextColour, f'Killed monsters: {hero.monsterKilled}')
        res.oneOption(screen)

        cui.heroRangText(screen, hero.rang)

        if exitButton.drawButton():
            save.makeSave()
            run = False

        if hero.rang < 10:
            if sacrificeButton.drawButton():
                if hero.rang == 0 and pl.heroStats.get('monsterCounter') >= hunt.rangAmount.get("rang1"):
                    hunt.update()
                elif hero.rang == 1 and pl.heroStats.get('monsterCounter') >= hunt.rangAmount.get("rang2"):
                    hunt.update()
                elif hero.rang == 2 and pl.heroStats.get('monsterCounter') >= hunt.rangAmount.get("rang3"):
                    hunt.update()
                elif hero.rang == 3 and pl.heroStats.get('monsterCounter') >= hunt.rangAmount.get("rang4"):
                    hunt.update()
                elif hero.rang == 4 and pl.heroStats.get('monsterCounter') >= hunt.rangAmount.get("rang5"):
                    hunt.update()
                elif hero.rang == 5 and pl.heroStats.get('monsterCounter') >= hunt.rangAmount.get("rang6"):
                    hunt.update()
                elif hero.rang == 6 and pl.heroStats.get('monsterCounter') >= hunt.rangAmount.get("rang7"):
                    hunt.update()
                elif hero.rang == 7 and pl.heroStats.get('monsterCounter') >= hunt.rangAmount.get("rang8"):
                    hunt.update()
                elif hero.rang == 8 and pl.heroStats.get('monsterCounter') >= hunt.rangAmount.get("rang9"):
                    hunt.update()
                elif hero.rang == 9 and pl.heroStats.get('monsterCounter') >= hunt.rangAmount.get("rang10"):
                    hunt.update()
                elif hero.rang == 10:
                    pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save.makeSave()
                pygame.quit()
                sys.exit()

        pygame.display.update()
        gameClock.tick(60)

### Glory Hall ###

def glory():
    run = True
    exitButton = cui.Button(screen, 1100, 350, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                                 'Exit')

    while run:
        screen.fill((0, 0, 0))
        screen.blit(res.paper, (0, 0))
        res.textSetting(screen, (480, 50), res.pixelTitleFont, res.menuTextColour, 'HALL OF GLORY')
        score.gloryHallTable(screen)

        if exitButton.drawButton():
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save.makeSave()
                pygame.quit()
                sys.exit()

        pygame.display.update()
        gameClock.tick(60)

### Defeat Screen ###

def defeat():
    run = True
    exitButton = cui.Button(screen, 560, 650, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            'Exit')
    currScore = hero.countScore()
    score.updateScoreList(currScore)

    hero.reset()
    cactus.reset()
    gameMap.reset()
    treasure.lootClear()
    gameMap.__init__()
    save.makeSave()
    save.makeCactusSave()
    save.makeGlorySave()

    while run:
        screen.fill((0, 0, 0))
        screen.blit(res.lose, (350, 100))
        cui.scoreText(screen, currScore)

        if exitButton.drawButton():
            gameScreen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        gameClock.tick(60)

### Victory Screen ###

def victory():
    run = True
    exitButton = cui.Button(screen, 560, 650, res.menuTextColour, res.menuTextColourClicked, res.pixelFont, True,
                            'Exit')
    currScore = hero.countScore()
    score.updateScoreList(currScore)

    hero.reset()
    cactus.reset()
    gameMap.reset()
    treasure.lootClear()
    gameMap.__init__()
    save.makeSave()
    save.makeCactusSave()
    save.makeGlorySave()

    while run:
        screen.fill((0, 0, 0))
        screen.blit(res.win, (380, 100))
        cui.scoreText(screen, currScore)


        if exitButton.drawButton():
            gameScreen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        gameClock.tick(60)

### Minigame Screen ###

def miniGameScreen():
    screen.fill(res.black)
    screen.blit(res.goblin, (800, 300))
    res.textSetting(screen, (720, 50), res.pixelFont, res.menuTextColour,
                    'Connect 4 pieces and win some gold!')
    gameOver = False

    board = miniGame.createGameBoard()
    miniGame.drawBoard(board)
    pygame.display.update()

    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, res.black, (0, 0, miniGame.width, miniGame.sizeOfSquare))
                posX = event.pos[0]
                if miniGame.turn == miniGame.player:
                    if posX < 700 - miniGame.radius:
                        pygame.draw.circle(screen, res.red, (posX, int(miniGame.sizeOfSquare / 2)), miniGame.radius)
                    else:
                        pygame.draw.circle(screen, res.red, (int(700 - miniGame.radius), int(miniGame.sizeOfSquare / 2)), miniGame.radius)

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, res.black, (0, 0, miniGame.width, miniGame.sizeOfSquare))
                # Ask for Player 1 Input
                if miniGame.turn == miniGame.player:
                    posX = event.pos[0]
                    col = int(math.floor(posX / miniGame.sizeOfSquare))

                    if miniGame.validPlace(board, col):
                        row = miniGame.nextRow(board, col)
                        miniGame.pieceDrop(board, row, col, miniGame.playerPiece)

                        if miniGame.winMove(board, miniGame.playerPiece):
                            label = res.pixelTitleFont.render("You win!", 1, RED)
                            screen.blit(label, (40, 10))
                            label = res.pixelFont.render("You'll be taken back in 3 seconds!", 1,
                                                              res.menuTextColour)
                            screen.blit(label, (720, 100))
                            hero.gold += 10
                            save.makeSave()
                            gameOver = True

                        miniGame.turn += 1
                        miniGame.turn = miniGame.turn % 2

                        miniGame.drawBoard(board)

        # # Ask for Player 2 Input
        if miniGame.turn == miniGame.computer and not gameOver:

            col, minimaxScore = miniGame.minimax(board, 5, -math.inf, math.inf, True)

            if miniGame.validPlace(board, col):
                row = miniGame.nextRow(board, col)
                miniGame.pieceDrop(board, row, col, miniGame.comPiece)

                if miniGame.winMove(board, miniGame.comPiece):
                    label = res.pixelTitleFont.render("You lose!", 1, res.yellow)
                    screen.blit(label, (40, 10))
                    label = res.pixelFont.render("You'll be taken home in 3 seconds!", 1, res.menuTextColour)
                    screen.blit(label, (720, 100))
                    gameOver = True

                miniGame.drawBoard(board)

                miniGame.turn += 1
                miniGame.turn = miniGame.turn % 2

        if gameOver:
            save.makeSave()
            gameMap.nextStage()
            pygame.time.wait(3000)