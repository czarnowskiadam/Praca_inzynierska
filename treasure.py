import random
import game

class Treasure(object):
    def __init__(self):
        self.commonItems = ['Wooden Sword', 'Wooden Wand', 'Wooden Helmet', 'Wooden Armor', 'Wooden Boots',
                            'Wooden Pants', 'Wooden Gloves']
        self.rareItems = ['Iron Sword', 'Iron Wand', 'Iron Helmet', 'Iron Armor', 'Iron Boots',
                            'Iron Pants', 'Iron Gloves']
        self.uniqueItems = ['Golden Sword', 'Golden Wand', 'Golden Helmet', 'Golden Armor', 'Golden Boots',
                            'Golden Pants', 'Golden Gloves']
        self.legendaryItems = ['Diamond Sword', 'Diamond Wand', 'Diamond Helmet', 'Diamond Armor', 'Diamond Boots',
                            'Diamond Pants', 'Diamond Gloves']
        self.loot = []

    def openTreasure(self):
        itemAmount = random.randint(1, 3)

        for i in range(0, itemAmount):
            rarity = random.randint(1, 100)
            if 1 <= rarity <= 50:
                itemIndex = random.randint(0, 6)
                self.loot.append(self.commonItems[itemIndex])
            elif 51 <= rarity <= 80:
                itemIndex = random.randint(0, 6)
                self.loot.append(self.rareItems[itemIndex])
            elif 81 <= rarity <= 95:
                itemIndex = random.randint(0, 6)
                self.loot.append(self.uniqueItems[itemIndex])
            elif 96 <= rarity <= 100:
                itemIndex = random.randint(0, 6)
                self.loot.append(self.legendaryItems[itemIndex])

    def addStats(self):
        for item in self.loot:
            if item == 'Wooden Sword':
                game.hero.minDmg += 1
                game.hero.maxDmg += 1
            elif item == 'Wooden Wand':
                game.hero.minMDmg += 1
                game.hero.maxMDmg += 1
            elif item == 'Wooden Helmet' or item == 'Wooden Boots' or item == 'Wooden Gloves':
                game.hero.maxHP += 3
            elif item == 'Wooden Armor' or item == 'Wooden Pants':
                game.hero.maxHP += 5

            if item == 'Iron Sword':
                game.hero.minDmg += 3
                game.hero.maxDmg += 3
            elif item == 'Iron Wand':
                game.hero.minMDmg += 3
                game.hero.maxMDmg += 3
            elif item == 'Iron Helmet' or item == 'Iron Boots' or item == 'Iron Gloves':
                game.hero.maxHP += 6
            elif item == 'Iron Armor' or item == 'Iron Pants':
                game.hero.maxHP += 8

            if item == 'Golden Sword':
                game.hero.minDmg += 5
                game.hero.maxDmg += 5
            elif item == 'Golden Wand':
                game.hero.minMDmg += 5
                game.hero.maxMDmg += 5
            elif item == 'Golden Helmet' or item == 'Golden Boots' or item == 'Golden Gloves':
                game.hero.maxHP += 9
            elif item == 'Golden Armor' or item == 'Golden Pants':
                game.hero.maxHP += 11

            if item == 'Diamond Sword':
                game.hero.minDmg += 10
                game.hero.maxDmg += 10
            elif item == 'Diamond Wand':
                game.hero.minMDmg += 10
                game.hero.maxMDmg += 10
            elif item == 'Diamond Helmet' or item == 'Diamond Boots' or item == 'Diamond Gloves':
                game.hero.maxHP += 15
            elif item == 'Diamond Armor' or item == 'Diamond Pants':
                game.hero.maxHP += 25

    def lootGet(self):
        return self.loot

    def lootClear(self):
        self.loot.clear()