import pygame
import game
import resources as res

def equipment(display):
    if len(game.treasure.loot) == 0:
        pygame.draw.rect(display, res.black, (1100, 10, 250, 190))
        pygame.draw.line(display, res.white, (1100, 10), (1350, 10), 2)
        pygame.draw.line(display, res.white, (1350, 10), (1350, 200), 2)
        pygame.draw.line(display, res.white, (1350, 200), (1100, 200), 2)
        pygame.draw.line(display, res.white, (1100, 200), (1100, 10), 2)
        res.imageSetting(display, (1110, 165), (30, 30), res.goldImg)
        res.textSetting(display, (1150, 170), res.statsCategoryFont, res.white, str(game.hero.gold))
        res.imageSetting(display, (1110, 135), (30, 30), res.soulImg)
        res.textSetting(display, (1150, 140), res.statsCategoryFont, res.white, str(game.hero.souls))

    else:
        pygame.draw.rect(display, res.black, (1100, 10, 250, 190))
        pygame.draw.line(display, res.white, (1100, 10), (1350, 10), 2)
        pygame.draw.line(display, res.white, (1350, 10), (1350, 200), 2)
        pygame.draw.line(display, res.white, (1350, 200), (1100, 200), 2)
        pygame.draw.line(display, res.white, (1100, 200), (1100, 10), 2)

        for i in range(len(game.treasure.loot)):
            if 'Sword' in game.treasure.loot[i]:
                res.imageSetting(display, (1110, 15 + i * 30), (30, 30), res.sword)
                res.textSetting(display, (1150, 25 + i * 30), res.statsCategoryFont, res.white, str(game.treasure.loot[i]))
            elif 'Wand' in game.treasure.loot[i]:
                res.imageSetting(display, (1110, 15 + i * 30), (30, 30), res.staff)
                res.textSetting(display, (1150, 25 + i * 30), res.statsCategoryFont, res.white, str(game.treasure.loot[i]))
            else:
                res.imageSetting(display, (1110, 15 + i * 30), (30, 30), res.hearth)
                res.textSetting(display, (1150, 25 + i * 30), res.statsCategoryFont, res.white, str(game.treasure.loot[i]))

        res.imageSetting(display, (1110, 165), (30, 30), res.goldImg)
        res.textSetting(display, (1150, 170), res.statsCategoryFont, res.white, str(game.hero.gold))
        res.imageSetting(display, (1110, 135), (30, 30), res.soulImg)
        res.textSetting(display, (1150, 140), res.statsCategoryFont, res.white, str(game.hero.souls))
