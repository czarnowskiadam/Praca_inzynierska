import pygame
from pygame import *
import resources as res
import game

pygame.init()

clicked = False
class Button:
	width = 180
	height = 70

	def __init__(self, displayScreen, x, y, colour, clickedColour, whichFont, isFramed, text):
		self.display = displayScreen
		self.x = x
		self.y = y
		self.colour = colour
		self.clickedColour = clickedColour
		self.whichFont = whichFont
		self.isFramed = isFramed
		self.text = text

	def drawButton(self):
		global clicked
		action = False

		pos = pygame.mouse.get_pos()

		buttonRect = Rect(self.x, self.y, self.width, self.height)

		if self.isFramed:
			pygame.draw.line(self.display, self.colour, (self.x, self.y), (self.x + self.width, self.y), 2)
			pygame.draw.line(self.display, self.colour, (self.x, self.y), (self.x, self.y + self.height), 2)
			pygame.draw.line(self.display, self.colour, (self.x, self.y + self.height),
							 (self.x + self.width, self.y + self.height), 2)
			pygame.draw.line(self.display, self.colour, (self.x + self.width, self.y),
							 (self.x + self.width, self.y + self.height), 2)

		if buttonRect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				if self.isFramed:
					pygame.draw.line(self.display, self.clickedColour, (self.x, self.y), (self.x + self.width, self.y), 2)
					pygame.draw.line(self.display, self.clickedColour, (self.x, self.y), (self.x, self.y + self.height), 2)
					pygame.draw.line(self.display, self.clickedColour, (self.x, self.y + self.height),
									 (self.x + self.width, self.y + self.height), 2)
					pygame.draw.line(self.display, self.clickedColour, (self.x + self.width, self.y),
									 (self.x + self.width, self.y + self.height), 2)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True

		textImg = self.whichFont.render(self.text, True, self.colour)
		textLen = textImg.get_width()
		self.display.blit(textImg, (self.x + int(self.width / 2) - int(textLen / 2), self.y + 25))
		return action
	
def heroStatistics(displayScreen, currentHP, maxHealthPoints, minDamage, maxDamage, minMagicDamage, maxMagicDamage):
	res.textSetting(displayScreen, (20, 640), res.statsCategoryFont, res.menuTextColour, 'HP')
	res.textSetting(displayScreen, (120, 640), res.statsCategoryFont, res.menuTextColour, f'{currentHP}/{maxHealthPoints}')
	res.textSetting(displayScreen, (20, 680), res.statsCategoryFont, res.menuTextColour, 'Attack')
	res.textSetting(displayScreen, (120, 680), res.statsCategoryFont, res.menuTextColour, f'{minDamage}-{maxDamage}')
	res.textSetting(displayScreen, (20, 720), res.statsCategoryFont, res.menuTextColour, 'Magic')
	res.textSetting(displayScreen, (120, 720), res.statsCategoryFont, res.menuTextColour, f'{minMagicDamage}-{maxMagicDamage}')


def heroInfo(displayScreen, lvl, exp, expUP, rang):
	res.textSetting(displayScreen, (90, 482), res.statsCategoryFont, res.menuTextColour, 'Hero')
	res.textSetting(displayScreen, (20, 520), res.statsCategoryFont, res.menuTextColour, 'LVL')
	res.textSetting(displayScreen, (120, 520), res.statsCategoryFont, res.menuTextColour, f'{lvl}')
	res.textSetting(displayScreen, (20, 560), res.statsCategoryFont, res.menuTextColour, 'EXP')
	res.textSetting(displayScreen, (120, 560), res.statsCategoryFont, res.menuTextColour, f'{exp}/{expUP}')
	res.textSetting(displayScreen, (20, 600), res.statsCategoryFont, res.menuTextColour, 'Rang')
	res.textSetting(displayScreen, (120, 600), res.statsCategoryFont, res.menuTextColour, f'{rang}')

def enemyInfo(displayScreen, name, currHP, maxHP, minDmg, maxDmg):
	res.textSetting(displayScreen, (930, 530), res.statsCategoryFont, res.menuTextColour, f'{name.upper()}')
	res.textSetting(displayScreen, (930, 570), res.statsCategoryFont, res.menuTextColour, 'HP:')
	res.textSetting(displayScreen, (930, 610), res.statsCategoryFont, res.menuTextColour, f'{currHP}/{maxHP}')
	res.textSetting(displayScreen, (930, 650), res.statsCategoryFont, res.menuTextColour, 'Damage:')
	res.textSetting(displayScreen, (930, 690), res.statsCategoryFont, res.menuTextColour, f'{minDmg}-{maxDmg}')
	res.imageSetting(displayScreen, (1100, 500), (250, 250), res.swords)

def expeditionEnemy(displayScreen):
	res.textSetting(displayScreen, (1080, 482), res.statsCategoryFont, res.menuTextColour, 'Enemy')

def expeditionActions(displayScreen):
	res.textSetting(displayScreen, (500, 482), res.statsCategoryFont, res.menuTextColour, 'Actions')

def fightTurn(displayScreen, turn, pos):
	if turn == 1:
		res.textSetting(displayScreen, pos, res.statsCategoryFont, res.menuTextColour, 'Your turn!')
	elif turn == 2:
		res.textSetting(displayScreen, pos, res.statsCategoryFont, res.menuTextColour, 'Enemy turn!')
	else:
		pass

def healingCentreText(displayScreen, low, medium, high):
	res.textSetting(displayScreen, (290, 510), res.pixelBuffFont, res.menuTextColour, f'Heal {low[0]} HP')
	res.textSetting(displayScreen, (350, 570), res.pixelBuffFont, res.menuTextColour, f'Cost: {low[1]}G')
	res.textSetting(displayScreen, (575, 510), res.pixelBuffFont, res.menuTextColour, f'Heal {medium[0]} HP')
	res.textSetting(displayScreen, (625, 570), res.pixelBuffFont, res.menuTextColour, f'Cost: {medium[1]}G')
	res.textSetting(displayScreen, (850, 510), res.pixelBuffFont, res.menuTextColour, 'Heal to max HP')
	res.textSetting(displayScreen, (900, 570), res.pixelBuffFont, res.menuTextColour, f'Cost: {high[1]}G')
	
def heroRangText(displayScreen, num):
	if num == 0:
		res.textSetting(displayScreen, (575, 510), res.pixelBuffFont, res.menuTextColour, f'Rang 1')
		res.textSetting(displayScreen, (625, 570), res.pixelBuffFont, res.menuTextColour,
						f'Cost: {game.hunt.rangAmount.get("rang1")}')
	elif num == 1:
		res.textSetting(displayScreen, (575, 510), res.pixelBuffFont, res.menuTextColour, f'Rang 2')
		res.textSetting(displayScreen, (625, 570), res.pixelBuffFont, res.menuTextColour,
						f'Cost: {game.hunt.rangAmount.get("rang2")}')
	elif num == 2:
		res.textSetting(displayScreen, (575, 510), res.pixelBuffFont, res.menuTextColour, f'Rang 3')
		res.textSetting(displayScreen, (625, 570), res.pixelBuffFont, res.menuTextColour,
						f'Cost: {game.hunt.rangAmount.get("rang3")}')
	elif num == 3:
		res.textSetting(displayScreen, (575, 510), res.pixelBuffFont, res.menuTextColour, f'Rang 4')
		res.textSetting(displayScreen, (625, 570), res.pixelBuffFont, res.menuTextColour,
						f'Cost: {game.hunt.rangAmount.get("rang4")}')
	elif num == 4:
		res.textSetting(displayScreen, (575, 510), res.pixelBuffFont, res.menuTextColour, f'Rang 5')
		res.textSetting(displayScreen, (625, 570), res.pixelBuffFont, res.menuTextColour,
						f'Cost: {game.hunt.rangAmount.get("rang5")}')
	elif num == 5:
		res.textSetting(displayScreen, (575, 510), res.pixelBuffFont, res.menuTextColour, f'Rang 6')
		res.textSetting(displayScreen, (625, 570), res.pixelBuffFont, res.menuTextColour,
						f'Cost: {game.hunt.rangAmount.get("rang6")}')
	elif num == 6:
		res.textSetting(displayScreen, (575, 510), res.pixelBuffFont, res.menuTextColour, f'Rang 7')
		res.textSetting(displayScreen, (625, 570), res.pixelBuffFont, res.menuTextColour,
						f'Cost: {game.hunt.rangAmount.get("rang7")}')
	elif num == 7:
		res.textSetting(displayScreen, (575, 510), res.pixelBuffFont, res.menuTextColour, f'Rang 8')
		res.textSetting(displayScreen, (625, 570), res.pixelBuffFont, res.menuTextColour,
						f'Cost: {game.hunt.rangAmount.get("rang8")}')
	elif num == 8:
		res.textSetting(displayScreen, (575, 510), res.pixelBuffFont, res.menuTextColour, f'Rang 9')
		res.textSetting(displayScreen, (625, 570), res.pixelBuffFont, res.menuTextColour,
						f'Cost: {game.hunt.rangAmount.get("rang9")}')
	elif num == 9:
		res.textSetting(displayScreen, (575, 510), res.pixelBuffFont, res.menuTextColour, f'Rang 10')
		res.textSetting(displayScreen, (625, 570), res.pixelBuffFont, res.menuTextColour,
						f'Cost: {game.hunt.rangAmount.get("rang10")}')
	elif num == 10:
		res.textSetting(displayScreen, (575, 510), res.pixelBuffFont, res.menuTextColour, f'Rang 10')
		res.textSetting(displayScreen, (625, 570), res.pixelBuffFont, res.menuTextColour,
						f'Rang MAX')

def scoreText(displayScreen, score):
	res.textSetting(displayScreen, (480, 500), res.pixelTitleFont, res.white, 'Your score:')
	res.textSetting(displayScreen, (580, 580), res.pixelTitleFont, res.white, f'{score}')