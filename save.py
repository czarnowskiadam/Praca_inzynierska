import json
import os
import game
import player as pl
import cactus
import score

def makeSave():
    game.hero.updateStats()
    with open('save/save.txt', 'w') as heroSave:
        json.dump(pl.heroStats, heroSave)

def readSave():
    try:
        with open('save/save.txt') as heroSave:
            pl.heroStats = json.load(heroSave)
    except:
        print('No such a file or directory yet.')


def makeCactusSave():
    game.cactus.update()
    with open('save/saveCactus.txt', 'w') as cactusSave:
        json.dump(cactus.cactusLvl, cactusSave)

def readCactusSave():
    try:
        with open('save/saveCactus.txt') as cactusSave:
            cactus.cactusLvl = json.load(cactusSave)
    except:
        print('No such a file or directory yet.')

def makeGlorySave():
    game.hero.updateStats()
    with open('save/saveGlory.txt', 'w') as glorySave:
        json.dump(score.allScores, glorySave)

def readGlorySave():
    try:
        with open('save/saveGlory.txt') as glorySave:
            score.allScores = json.load(glorySave)
    except:
        print('No such a file or directory yet.')