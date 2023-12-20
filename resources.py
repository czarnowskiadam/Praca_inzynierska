import pygame
import game

pygame.font.init()

### Colours ###
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
menuTextColour = (227, 226, 244)
menuTextColourClicked = (111, 117, 196)
cityTextColour = (149, 0, 4)
cityTextColourClicked = (255, 81, 85)

### Images ###
bgMenu = pygame.image.load('img/bgMenu.png')
bgCity = pygame.image.load('img/cityBg.png')
soulImg = pygame.image.load('img/soul.png')
goldImg = pygame.image.load('img/gold.png')
explorationHUD = pygame.image.load('img/explorationHUD.png')
bonfireImg = pygame.image.load('img/bonfire.png')
testLuckImg = pygame.image.load('img/testLuck.png')
buffShop = pygame.image.load('img/buffshop.png')
healingCentre = pygame.image.load('img/healingCentre.png')
home = pygame.image.load('img/home.png')
mapBackground = pygame.image.load('img/mapBackground.png')
treasureRoom = pygame.image.load('img/treasureRoom.png')
closedChest = pygame.image.load('img/closedChest.png')
openedChest = pygame.image.load('img/openedChest.png')
huntingHut = pygame.image.load('img/hunterHut.png')
swords = pygame.image.load('img/swords.png')
paper = pygame.image.load('img/paper.png')
goblin = pygame.image.load('img/goblin.png')
sword = pygame.image.load('img/sword.png')
staff = pygame.image.load('img/staff.png')
hearth = pygame.image.load('img/hearth.png')
lose = pygame.image.load('img/lose.png')
win = pygame.image.load('img/win.png')

### Player Animation Sheets ###
idlePlayerAnimation = pygame.image.load('sprites/hero/heroIdle.png')
attackPlayerAnimation = pygame.image.load('sprites/hero/heroAttack.png')
defPlayerAnimation = pygame.image.load('sprites/hero/heroDef.png')
deathPlayerAnimation = pygame.image.load('sprites/hero/heroDeath.png')
### Skeleton Animation Sheets ###
attackSkeletonAnimation = pygame.image.load('sprites/skeleton/attack.png')
deathSkeletonAnimation = pygame.image.load('sprites/skeleton/death.png')
idleSkeletonAnimation = pygame.image.load('sprites/skeleton/idle.png')
reviveSkeletonAnimation = pygame.image.load('sprites/skeleton/revive.png')
### Minotaur Animation Sheets ###
idleMinotaurAnimation = pygame.image.load('sprites/minotaur/idle.png')
attackMinotaurAnimation = pygame.image.load('sprites/minotaur/attack.png')
deathMinotaurAnimation = pygame.image.load('sprites/minotaur/death.png')
stunMinotaurAnimation = pygame.image.load('sprites/minotaur/stun.png')
healMinotaurAnimation = pygame.image.load('sprites/minotaur/heal.png')
### Witch Animation Sheets ###
idleWitchAnimation = pygame.image.load('sprites/witch/idle.png')
attackWitchAnimation = pygame.image.load('sprites/witch/attack.png')
deathWitchAnimation = pygame.image.load('sprites/witch/death.png')
healWitchAnimation = pygame.image.load('sprites/witch/heal.png')
### Golem Animation Sheets ###
idleGolemAnimation = pygame.image.load('sprites/golem/idle.png')
attackGolemAnimation = pygame.image.load('sprites/golem/attack.png')
deathGolemAnimation = pygame.image.load('sprites/golem/death.png')
defenceGolemAnimation = pygame.image.load('sprites/golem/defence.png')
### Slayer Animation Sheets ###
idleSlayerAnimation = pygame.image.load('sprites/slayer/idle.png')
attackSlayerAnimation = pygame.image.load('sprites/slayer/attack.png')
deathSlayerAnimation = pygame.image.load('sprites/slayer/death.png')
drainSlayerAnimation = pygame.image.load('sprites/slayer/drain.png')
toxicSlayerAnimation = pygame.image.load('sprites/slayer/toxic.png')
### Sorcerer Animation Sheets ###
idleSorcererAnimation = pygame.image.load('sprites/sorcerer/idle.png')
attackSorcererAnimation = pygame.image.load('sprites/sorcerer/attack.png')
deathSorcererAnimation = pygame.image.load('sprites/sorcerer/death.png')
curseSorcererAnimation = pygame.image.load('sprites/sorcerer/curse.png')
### Nightborn Animation Sheets ###
idleNightbornAnimation = pygame.image.load('sprites/nightborn/idle.png')
attackNightbornAnimation = pygame.image.load('sprites/nightborn/attack.png')
deathNightbornAnimation = pygame.image.load('sprites/nightborn/death.png')
stunNightbornAnimation = pygame.image.load('sprites/nightborn/stun.png')


### Fonts ###
pixelFont = pygame.font.Font('fonts/pixelFont.ttf', 40)
pixelTitleFont = pygame.font.Font('fonts/pixelFont.ttf', 70)
pixelCityFont = pygame.font.Font('fonts/pixelFont.ttf', 20)
explorationFont = pygame.font.Font('fonts/pixelFont.ttf', 22)
statsCategoryFont = pygame.font.Font('fonts/pixelFont.ttf', 30)
notificationFont = pygame.font.Font('fonts/pixelFont.ttf', 35)
pixelBuffFont = pygame.font.Font('fonts/pixelFont.ttf', 25)

def textSetting(display, pos, font, colour,text):
    img = font.render(text, True, colour)
    display.blit(img, pos)

def imageSetting(display, pos, size, img):
    tempImg = img
    tempImg = pygame.transform.scale(tempImg, size)
    display.blit(tempImg, pos)

def mapLines(display):
    pygame.draw.line(display, red, (280, 335), (350, 335), 2)
    pygame.draw.line(display, red, (530, 335), (600, 335), 2)
    pygame.draw.line(display, red, (780, 335), (850, 335), 2)
    pygame.draw.line(display, red, (1030, 335), (1100, 335), 2)
    pygame.draw.line(display, red, (1190, 370), (1190, 600), 2)
    pygame.draw.line(display, red, (280, 335), (350, 335), 2)
    pygame.draw.line(display, red, (1100, 635), (1030, 635), 2)
    pygame.draw.line(display, red, (850, 635), (780, 635), 2)
    pygame.draw.line(display, red, (600, 635), (530, 635), 2)
    pygame.draw.line(display, red, (350, 635), (280, 635), 2)

def arrowMap(display, stage):
    if stage == 0:
        pygame.draw.line(display, red, (190, 200), (190, 250), 3)
        pygame.draw.line(display, red, (190, 250), (180, 240), 3)
        pygame.draw.line(display, red, (190, 250), (200, 240), 3)
    if stage == 1:
        pygame.draw.line(display, red, (440, 200), (440, 250), 3)
        pygame.draw.line(display, red, (440, 250), (430, 240), 3)
        pygame.draw.line(display, red, (440, 250), (450, 240), 3)
    if stage == 2:
        pygame.draw.line(display, red, (690, 200), (690, 250), 3)
        pygame.draw.line(display, red, (690, 250), (680, 240), 3)
        pygame.draw.line(display, red, (690, 250), (700, 240), 3)
    if stage == 3:
        pygame.draw.line(display, red, (940, 200), (940, 250), 3)
        pygame.draw.line(display, red, (940, 250), (930, 240), 3)
        pygame.draw.line(display, red, (940, 250), (950, 240), 3)
    if stage == 4:
        pygame.draw.line(display, red, (1190, 200), (1190, 250), 3)
        pygame.draw.line(display, red, (1190, 250), (1180, 240), 3)
        pygame.draw.line(display, red, (1190, 250), (1200, 240), 3)
    if stage == 5:
        pygame.draw.line(display, red, (1190, 700), (1190, 750), 3)
        pygame.draw.line(display, red, (1190, 700), (1180, 710), 3)
        pygame.draw.line(display, red, (1190, 700), (1200, 710), 3)
    if stage == 6:
        pygame.draw.line(display, red, (940, 700), (940, 750), 3)
        pygame.draw.line(display, red, (940, 700), (930, 710), 3)
        pygame.draw.line(display, red, (940, 700), (950, 710), 3)
    if stage == 7:
        pygame.draw.line(display, red, (690, 700), (690, 750), 3)
        pygame.draw.line(display, red, (690, 700), (680, 710), 3)
        pygame.draw.line(display, red, (690, 700), (700, 710), 3)
    if stage == 8:
        pygame.draw.line(display, red, (440, 700), (440, 750), 3)
        pygame.draw.line(display, red, (440, 700), (430, 710), 3)
        pygame.draw.line(display, red, (440, 700), (450, 710), 3)
    if stage == 9:
        pygame.draw.line(display, red, (190, 700), (190, 750), 3)
        pygame.draw.line(display, red, (190, 700), (180, 710), 3)
        pygame.draw.line(display, red, (190, 700), (200, 710), 3)

def threeOptions(display):
    pygame.draw.rect(display, menuTextColour, (280, 500, 220, 150), 3)
    pygame.draw.rect(display, menuTextColour, (560, 500, 220, 150), 3)
    pygame.draw.rect(display, menuTextColour, (840, 500, 220, 150), 3)

def oneOption(display):
    pygame.draw.rect(display, menuTextColour, (560, 500, 220, 150), 3)

def balance(display):
    imageSetting(display, (20, 600), (50, 50), soulImg)
    textSetting(display, (80, 615), pixelFont, menuTextColour, f'{game.hero.souls}')
    imageSetting(display, (20, 660), (50, 50), goldImg)
    textSetting(display, (80, 675), pixelFont, menuTextColour, f'{game.hero.gold}')