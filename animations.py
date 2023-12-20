import pygame
import resources as res
import game

class SpriteSheet:
	def __init__(self, image):
		self.sheet = image

	def getImage(self, frame, width, height, scale, colour):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))
		image.set_colorkey(colour)

		return image

class PlayerAnimations:
	def __init__(self):
		self.state = 0
		self.heroIdleAnimation = res.idlePlayerAnimation
		self.idleAnimationList = []
		self.idleAnimationSteps = 15
		self.heroAttackAnimation = res.attackPlayerAnimation
		self.attackAnimationList = []
		self.attackAnimationSteps = 22
		self.heroDefAnimation = res.defPlayerAnimation
		self.defAnimationList = []
		self.defAnimationSteps = 7
		self.heroDeathAnimation = res.deathPlayerAnimation
		self.deathAnimationList = []
		self.deathAnimationSteps = 15

		self.idleSpriteSheet = SpriteSheet(self.heroIdleAnimation)
		self.attackSpriteSheet = SpriteSheet(self.heroAttackAnimation)
		self.defSpriteSheet = SpriteSheet(self.heroDefAnimation)
		self.deathSpriteSheet = SpriteSheet(self.heroDeathAnimation)

		self.lastUpdate = pygame.time.get_ticks()
		self.animationCooldown = 100

		self.idleFrame = 0
		self.attackFrame = 0
		self.defFrame = 0
		self.deathFrame = 0

		for x in range(self.idleAnimationSteps):
			self.idleAnimationList.append(self.idleSpriteSheet.getImage(x, 64, 64, 3, (0, 0, 0)))

		for x in range(self.attackAnimationSteps):
			self.attackAnimationList.append(self.attackSpriteSheet.getImage(x, 144, 64, 3, (0, 0, 0)))

		for x in range(self.defAnimationSteps):
			self.defAnimationList.append(self.defSpriteSheet.getImage(x, 96, 64, 3, (0, 0, 0)))

		for x in range(self.deathAnimationSteps):
			self.deathAnimationList.append(self.deathSpriteSheet.getImage(x, 96, 64, 3, (0, 0, 0)))

	def updateIdleAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.animationCooldown:
			self.idleFrame += 1
			self.lastUpdate = currentTime
			if self.idleFrame >= len(self.idleAnimationList):
				self.idleFrame = 0

	def displayIdleAnimation(self):
		game.screen.blit(self.idleAnimationList[self.idleFrame], (200, 270))

	def updateAttackAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.animationCooldown:
			self.attackFrame += 1
			self.lastUpdate = currentTime
			if self.attackFrame >= len(self.attackAnimationList):
				self.attackFrame = 0
				self.state = 0
				game.fightTurn.endTurn()

	def displayAttackAnimation(self):
		game.screen.blit(self.attackAnimationList[self.attackFrame], (200, 270))

	def updateDefAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.animationCooldown:
			self.defFrame += 1
			self.lastUpdate = currentTime
			if self.defFrame >= len(self.defAnimationList):
				self.defFrame = 0
				self.state = 0
				game.fightTurn.endTurn()

	def displayDefAnimation(self):
		game.screen.blit(self.defAnimationList[self.defFrame], (200, 270))

	def updateDeathAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.animationCooldown:
			self.deathFrame += 1
			self.lastUpdate = currentTime
			if self.deathFrame >= len(self.deathAnimationList):
				self.deathFrame = 0
				self.state = 0
				game.fightTurn.endTurn()

	def displayDeathAnimation(self):
		game.screen.blit(self.deathAnimationList[self.deathFrame], (200, 270))

class EnemyAnimations:
	def __init__(self):
		self.state = 0

		### Skeleton animation preparation ###
		self.idleSkeletonAnimation = res.idleSkeletonAnimation
		self.idleSkeletonAnimationList = []
		self.idleSkeletonAnimationSteps = 4
		self.reviveSkeletonAnimation = res.reviveSkeletonAnimation
		self.reviveSkeletonAnimationList = []
		self.reviveSkeletonAnimationSteps = 3
		self.attackSkeletonAnimation = res.attackSkeletonAnimation
		self.attackSkeletonAnimationList = []
		self.attackSkeletonAnimationSteps = 13
		self.deathSkeletonAnimation = res.deathSkeletonAnimation
		self.deathSkeletonAnimationList = []
		self.deathSkeletonAnimationSteps = 13

		self.idleSkeletonSpriteSheet = SpriteSheet(self.idleSkeletonAnimation)
		self.reviveSkeletonSpriteSheet = SpriteSheet(self.reviveSkeletonAnimation)
		self.attackSkeletonSpriteSheet = SpriteSheet(self.attackSkeletonAnimation)
		self.deathSkeletonSpriteSheet = SpriteSheet(self.deathSkeletonAnimation)

		self.lastUpdate = pygame.time.get_ticks()
		self.idleSkeletonAnimationCooldown = 200
		self.reviveSkeletonAnimationCooldown = 400
		self.attackSkeletonAnimationCooldown = 200
		self.deathSkeletonAnimationCooldown = 200

		self.idleSkeletonFrame = 0
		self.reviveSkeletonFrame = 0
		self.attackSkeletonFrame = 0
		self.deathSkeletonFrame = 0

		for x in range(self.idleSkeletonAnimationSteps):
			self.idleSkeletonAnimationList.append(self.idleSkeletonSpriteSheet.getImage(x, 64, 64, 3, (0, 0, 0)))

		for x in range(self.reviveSkeletonAnimationSteps):
			self.reviveSkeletonAnimationList.append(self.reviveSkeletonSpriteSheet.getImage(x, 64, 64, 3, (0, 0, 0)))

		for x in range(self.attackSkeletonAnimationSteps):
			self.attackSkeletonAnimationList.append(self.attackSkeletonSpriteSheet.getImage(x, 64, 64, 3, (0, 0, 0)))

		for x in range(self.deathSkeletonAnimationSteps):
			self.deathSkeletonAnimationList.append(self.deathSkeletonSpriteSheet.getImage(x, 64, 64, 3, (0, 0, 0)))

		### Minotaur animation preparation ###
		self.idleMinotaurAnimation = res.idleMinotaurAnimation
		self.idleMinotaurAnimationList = []
		self.idleMinotaurAnimationSteps = 5
		self.attackMinotaurAnimation = res.attackMinotaurAnimation
		self.attackMinotaurAnimationList = []
		self.attackMinotaurAnimationSteps = 9
		self.deathMinotaurAnimation = res.deathMinotaurAnimation
		self.deathMinotaurAnimationList = []
		self.deathMinotaurAnimationSteps = 6
		self.stunMinotaurAnimation = res.stunMinotaurAnimation
		self.stunMinotaurAnimationList = []
		self.stunMinotaurAnimationSteps = 6
		self.healMinotaurAnimation = res.healMinotaurAnimation
		self.healMinotaurAnimationList = []
		self.healMinotaurAnimationSteps = 3

		self.idleMinotaurSpriteSheet = SpriteSheet(self.idleMinotaurAnimation)
		self.stunMinotaurSpriteSheet = SpriteSheet(self.stunMinotaurAnimation)
		self.attackMinotaurSpriteSheet = SpriteSheet(self.attackMinotaurAnimation)
		self.deathMinotaurSpriteSheet = SpriteSheet(self.deathMinotaurAnimation)
		self.healMinotaurSpriteSheet = SpriteSheet(self.healMinotaurAnimation)

		self.idleMinotaurAnimationCooldown = 200
		self.stunMinotaurAnimationCooldown = 200
		self.attackMinotaurAnimationCooldown = 200
		self.deathMinotaurAnimationCooldown = 200
		self.healMinotaurAnimationCooldown = 400

		self.idleMinotaurFrame = 0
		self.stunMinotaurFrame = 0
		self.attackMinotaurFrame = 0
		self.deathMinotaurFrame = 0
		self.healMinotaurFrame = 0

		for x in range(self.idleMinotaurAnimationSteps):
			self.idleMinotaurAnimationList.append(self.idleMinotaurSpriteSheet.getImage(x, 100, 80, 2, (0, 0, 0)))

		for x in range(self.attackMinotaurAnimationSteps):
			self.attackMinotaurAnimationList.append(self.attackMinotaurSpriteSheet.getImage(x, 97, 74, 2, (0, 0, 0)))

		for x in range(self.stunMinotaurAnimationSteps):
			self.stunMinotaurAnimationList.append(self.stunMinotaurSpriteSheet.getImage(x, 95, 64, 2, (0, 0, 0)))

		for x in range(self.healMinotaurAnimationSteps):
			self.healMinotaurAnimationList.append(self.healMinotaurSpriteSheet.getImage(x, 98, 64, 2, (0, 0, 0)))

		for x in range(self.deathMinotaurAnimationSteps):
			self.deathMinotaurAnimationList.append(self.deathMinotaurSpriteSheet.getImage(x, 95, 64, 2, (0, 0, 0)))

		### Witch animation preparation ###
		self.idleWitchAnimation = res.idleWitchAnimation
		self.idleWitchAnimationList = []
		self.idleWitchAnimationSteps = 8
		self.attackWitchAnimation = res.attackWitchAnimation
		self.attackWitchAnimationList = []
		self.attackWitchAnimationSteps = 8
		self.deathWitchAnimation = res.deathWitchAnimation
		self.deathWitchAnimationList = []
		self.deathWitchAnimationSteps = 7
		self.healWitchAnimation = res.healWitchAnimation
		self.healWitchAnimationList = []
		self.healWitchAnimationSteps = 3

		self.idleWitchSpriteSheet = SpriteSheet(self.idleWitchAnimation)
		self.attackWitchSpriteSheet = SpriteSheet(self.attackWitchAnimation)
		self.deathWitchSpriteSheet = SpriteSheet(self.deathWitchAnimation)
		self.healWitchSpriteSheet = SpriteSheet(self.healWitchAnimation)

		self.idleWitchAnimationCooldown = 200
		self.attackWitchAnimationCooldown = 180
		self.deathWitchAnimationCooldown = 200
		self.healWitchAnimationCooldown = 400

		self.idleWitchFrame = 0
		self.attackWitchFrame = 0
		self.deathWitchFrame = 0
		self.healWitchFrame = 0

		for x in range(self.idleWitchAnimationSteps):
			self.idleWitchAnimationList.append(self.idleWitchSpriteSheet.getImage(x, 250, 250, 2, (0, 0, 0)))

		for x in range(self.attackWitchAnimationSteps):
			self.attackWitchAnimationList.append(self.attackWitchSpriteSheet.getImage(x, 250, 250, 2, (0, 0, 0)))

		for x in range(self.healWitchAnimationSteps):
			self.healWitchAnimationList.append(self.healWitchSpriteSheet.getImage(x, 250, 250, 2, (0, 0, 0)))

		for x in range(self.deathWitchAnimationSteps):
			self.deathWitchAnimationList.append(self.deathWitchSpriteSheet.getImage(x, 250, 250, 2, (0, 0, 0)))

		### Golem animation preparation ###
		self.idleGolemAnimation = res.idleGolemAnimation
		self.idleGolemAnimationList = []
		self.idleGolemAnimationSteps = 8
		self.attackGolemAnimation = res.attackGolemAnimation
		self.attackGolemAnimationList = []
		self.attackGolemAnimationSteps = 9
		self.deathGolemAnimation = res.deathGolemAnimation
		self.deathGolemAnimationList = []
		self.deathGolemAnimationSteps = 10
		self.defenceGolemAnimation = res.defenceGolemAnimation
		self.defenceGolemAnimationList = []
		self.defenceGolemAnimationSteps = 8

		self.idleGolemSpriteSheet = SpriteSheet(self.idleGolemAnimation)
		self.attackGolemSpriteSheet = SpriteSheet(self.attackGolemAnimation)
		self.deathGolemSpriteSheet = SpriteSheet(self.deathGolemAnimation)
		self.defenceGolemSpriteSheet = SpriteSheet(self.defenceGolemAnimation)

		self.idleGolemAnimationCooldown = 200
		self.attackGolemAnimationCooldown = 100
		self.deathGolemAnimationCooldown = 200
		self.defenceGolemAnimationCooldown = 100

		self.idleGolemFrame = 0
		self.attackGolemFrame = 0
		self.deathGolemFrame = 0
		self.defenceGolemFrame = 0

		for x in range(self.idleGolemAnimationSteps):
			self.idleGolemAnimationList.append(self.idleGolemSpriteSheet.getImage(x, 100, 100, 2, (0, 0, 0)))

		for x in range(self.attackGolemAnimationSteps):
			self.attackGolemAnimationList.append(self.attackGolemSpriteSheet.getImage(x, 100, 100, 2, (0, 0, 0)))

		for x in range(self.defenceGolemAnimationSteps):
			self.defenceGolemAnimationList.append(self.defenceGolemSpriteSheet.getImage(x, 100, 100, 2, (0, 0, 0)))

		for x in range(self.deathGolemAnimationSteps):
			self.deathGolemAnimationList.append(self.deathGolemSpriteSheet.getImage(x, 100, 100, 2, (0, 0, 0)))

		### Slayer animation preparation ###
		self.idleSlayerAnimation = res.idleSlayerAnimation
		self.idleSlayerAnimationList = []
		self.idleSlayerAnimationSteps = 8
		self.attackSlayerAnimation = res.attackSlayerAnimation
		self.attackSlayerAnimationList = []
		self.attackSlayerAnimationSteps = 8
		self.deathSlayerAnimation = res.deathSlayerAnimation
		self.deathSlayerAnimationList = []
		self.deathSlayerAnimationSteps = 8
		self.drainSlayerAnimation = res.drainSlayerAnimation
		self.drainSlayerAnimationList = []
		self.drainSlayerAnimationSteps = 8
		self.toxicSlayerAnimation = res.toxicSlayerAnimation
		self.toxicSlayerAnimationList = []
		self.toxicSlayerAnimationSteps = 8

		self.idleSlayerSpriteSheet = SpriteSheet(self.idleSlayerAnimation)
		self.attackSlayerSpriteSheet = SpriteSheet(self.attackSlayerAnimation)
		self.deathSlayerSpriteSheet = SpriteSheet(self.deathSlayerAnimation)
		self.drainSlayerSpriteSheet = SpriteSheet(self.drainSlayerAnimation)
		self.toxicSlayerSpriteSheet = SpriteSheet(self.toxicSlayerAnimation)

		self.idleSlayerAnimationCooldown = 100
		self.attackSlayerAnimationCooldown = 100
		self.deathSlayerAnimationCooldown = 100
		self.drainSlayerAnimationCooldown = 100
		self.toxicSlayerAnimationCooldown = 100

		self.idleSlayerFrame = 0
		self.attackSlayerFrame = 0
		self.deathSlayerFrame = 0
		self.drainSlayerFrame = 0
		self.toxicSlayerFrame = 0

		for x in range(self.idleSlayerAnimationSteps):
			self.idleSlayerAnimationList.append(self.idleSlayerSpriteSheet.getImage(x, 140, 100, 2, (0, 0, 0)))

		for x in range(self.attackSlayerAnimationSteps):
			self.attackSlayerAnimationList.append(self.attackSlayerSpriteSheet.getImage(x, 140, 100, 2, (0, 0, 0)))

		for x in range(self.drainSlayerAnimationSteps):
			self.drainSlayerAnimationList.append(self.drainSlayerSpriteSheet.getImage(x, 140, 100, 2, (0, 0, 0)))

		for x in range(self.deathSlayerAnimationSteps):
			self.deathSlayerAnimationList.append(self.deathSlayerSpriteSheet.getImage(x, 140, 100, 2, (0, 0, 0)))

		for x in range(self.toxicSlayerAnimationSteps):
			self.toxicSlayerAnimationList.append(self.toxicSlayerSpriteSheet.getImage(x, 140, 100, 2, (0, 0, 0)))

		### Sorcerer animation preparation ###
		self.idleSorcererAnimation = res.idleSorcererAnimation
		self.idleSorcererAnimationList = []
		self.idleSorcererAnimationSteps = 8
		self.attackSorcererAnimation = res.attackSorcererAnimation
		self.attackSorcererAnimationList = []
		self.attackSorcererAnimationSteps = 8
		self.deathSorcererAnimation = res.deathSorcererAnimation
		self.deathSorcererAnimationList = []
		self.deathSorcererAnimationSteps = 5
		self.curseSorcererAnimation = res.curseSorcererAnimation
		self.curseSorcererAnimationList = []
		self.curseSorcererAnimationSteps = 4

		self.idleSorcererSpriteSheet = SpriteSheet(self.idleSorcererAnimation)
		self.attackSorcererSpriteSheet = SpriteSheet(self.attackSorcererAnimation)
		self.deathSorcererSpriteSheet = SpriteSheet(self.deathSorcererAnimation)
		self.curseSorcererSpriteSheet = SpriteSheet(self.curseSorcererAnimation)

		self.idleSorcererAnimationCooldown = 100
		self.attackSorcererAnimationCooldown = 100
		self.deathSorcererAnimationCooldown = 150
		self.curseSorcererAnimationCooldown = 200

		self.idleSorcererFrame = 0
		self.attackSorcererFrame = 0
		self.deathSorcererFrame = 0
		self.curseSorcererFrame = 0

		for x in range(self.idleSorcererAnimationSteps):
			self.idleSorcererAnimationList.append(self.idleSorcererSpriteSheet.getImage(x, 150, 150, 2, (0, 0, 0)))

		for x in range(self.attackSorcererAnimationSteps):
			self.attackSorcererAnimationList.append(self.attackSorcererSpriteSheet.getImage(x, 150, 150, 2, (0, 0, 0)))

		for x in range(self.curseSorcererAnimationSteps):
			self.curseSorcererAnimationList.append(self.curseSorcererSpriteSheet.getImage(x, 150, 150, 2, (0, 0, 0)))

		for x in range(self.deathSorcererAnimationSteps):
			self.deathSorcererAnimationList.append(self.deathSorcererSpriteSheet.getImage(x, 150, 150, 2, (0, 0, 0)))

		### Nightborn animation preparation ###
		self.idleNightbornAnimation = res.idleNightbornAnimation
		self.idleNightbornAnimationList = []
		self.idleNightbornAnimationSteps = 9
		self.attackNightbornAnimation = res.attackNightbornAnimation
		self.attackNightbornAnimationList = []
		self.attackNightbornAnimationSteps = 12
		self.deathNightbornAnimation = res.deathNightbornAnimation
		self.deathNightbornAnimationList = []
		self.deathNightbornAnimationSteps = 11
		self.stunNightbornAnimation = res.stunNightbornAnimation
		self.stunNightbornAnimationList = []
		self.stunNightbornAnimationSteps = 4

		self.idleNightbornSpriteSheet = SpriteSheet(self.idleNightbornAnimation)
		self.attackNightbornSpriteSheet = SpriteSheet(self.attackNightbornAnimation)
		self.deathNightbornSpriteSheet = SpriteSheet(self.deathNightbornAnimation)
		self.stunNightbornSpriteSheet = SpriteSheet(self.stunNightbornAnimation)

		self.idleNightbornAnimationCooldown = 100
		self.attackNightbornAnimationCooldown = 100
		self.deathNightbornAnimationCooldown = 150
		self.stunNightbornAnimationCooldown = 200

		self.idleNightbornFrame = 0
		self.attackNightbornFrame = 0
		self.deathNightbornFrame = 0
		self.stunNightbornFrame = 0

		for x in range(self.idleNightbornAnimationSteps):
			self.idleNightbornAnimationList.append(self.idleNightbornSpriteSheet.getImage(x, 80, 80, 3, (0, 0, 0)))

		for x in range(self.attackNightbornAnimationSteps):
			self.attackNightbornAnimationList.append(self.attackNightbornSpriteSheet.getImage(x, 80, 80, 3, (0, 0, 0)))

		for x in range(self.stunNightbornAnimationSteps):
			self.stunNightbornAnimationList.append(self.stunNightbornSpriteSheet.getImage(x, 80, 80, 3, (0, 0, 0)))

		for x in range(self.deathNightbornAnimationSteps):
			self.deathNightbornAnimationList.append(self.deathNightbornSpriteSheet.getImage(x, 80, 80, 3, (0, 0, 0)))

	### Skeleton animation methods ###

	def updateIdleSkeletonAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.idleSkeletonAnimationCooldown:
			self.idleSkeletonFrame += 1
			self.lastUpdate = currentTime
			if self.idleSkeletonFrame >= len(self.idleSkeletonAnimationList):
				self.idleSkeletonFrame = 0

	def displayIdleSkeletonAnimation(self):
		game.screen.blit(self.idleSkeletonAnimationList[self.idleSkeletonFrame], (950, 270))

	def updateReviveSkeletonAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.reviveSkeletonAnimationCooldown:
			self.reviveSkeletonFrame += 1
			self.lastUpdate = currentTime
			if self.reviveSkeletonFrame >= len(self.reviveSkeletonAnimationList):
				self.reviveSkeletonFrame = 0
				self.state = 0

	def displayReviveSkeletonAnimation(self):
		game.screen.blit(self.reviveSkeletonAnimationList[self.reviveSkeletonFrame], (950, 270))

	def updateAttackSkeletonAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.attackSkeletonAnimationCooldown:
			self.attackSkeletonFrame += 1
			self.lastUpdate = currentTime
			if self.attackSkeletonFrame >= len(self.attackSkeletonAnimationList):
				self.attackSkeletonFrame = 0
				self.state = 0

	def displayAttackSkeletonAnimation(self):
		game.screen.blit(self.attackSkeletonAnimationList[self.attackSkeletonFrame], (950, 270))

	def updateDeathSkeletonAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.deathSkeletonAnimationCooldown:
			self.deathSkeletonFrame += 1
			self.lastUpdate = currentTime
			if self.deathSkeletonFrame >= len(self.deathSkeletonAnimationList):
				self.deathSkeletonFrame = 0
				self.state = 0

	def displayDeathSkeletonAnimation(self):
		game.screen.blit(self.deathSkeletonAnimationList[self.deathSkeletonFrame], (950, 270))

	### Minotaur animation methods ###

	def updateIdleMinotaurAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.idleMinotaurAnimationCooldown:
			self.idleMinotaurFrame += 1
			self.lastUpdate = currentTime
			if self.idleMinotaurFrame >= len(self.idleMinotaurAnimationList):
				self.idleMinotaurFrame = 0

	def displayIdleMinotaurAnimation(self):
		game.screen.blit(self.idleMinotaurAnimationList[self.idleMinotaurFrame], (950, 270))

	def updateAttackMinotaurAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.attackMinotaurAnimationCooldown:
			self.attackMinotaurFrame += 1
			self.lastUpdate = currentTime
			if self.attackMinotaurFrame >= len(self.attackMinotaurAnimationList):
				self.attackMinotaurFrame = 0
				self.state = 0

	def displayAttackMinotaurAnimation(self):
		game.screen.blit(self.attackMinotaurAnimationList[self.attackMinotaurFrame], (950, 270))

	def updateStunMinotaurAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.stunMinotaurAnimationCooldown:
			self.stunMinotaurFrame += 1
			self.lastUpdate = currentTime
			if self.stunMinotaurFrame >= len(self.stunMinotaurAnimationList):
				self.stunMinotaurFrame = 0
				self.state = 0

	def displayStunMinotaurAnimation(self):
		game.screen.blit(self.stunMinotaurAnimationList[self.stunMinotaurFrame], (950, 270))

	def updateHealMinotaurAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.healMinotaurAnimationCooldown:
			self.healMinotaurFrame += 1
			self.lastUpdate = currentTime
			if self.healMinotaurFrame >= len(self.healMinotaurAnimationList):
				self.healMinotaurFrame = 0
				self.state = 0

	def displayHealMinotaurAnimation(self):
		game.screen.blit(self.healMinotaurAnimationList[self.healMinotaurFrame], (950, 290))

	def updateDeathMinotaurAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.deathMinotaurAnimationCooldown:
			self.deathMinotaurFrame += 1
			self.lastUpdate = currentTime
			if self.deathMinotaurFrame >= len(self.deathMinotaurAnimationList):
				self.deathMinotaurFrame = 0
				self.state = 0

	def displayDeathMinotaurAnimation(self):
		game.screen.blit(self.deathMinotaurAnimationList[self.deathMinotaurFrame], (950, 270))

	### Witch animation methods ###

	def updateIdleWitchAnimation(self):
			currentTime = pygame.time.get_ticks()
			if currentTime - self.lastUpdate >= self.idleWitchAnimationCooldown:
				self.idleWitchFrame += 1
				self.lastUpdate = currentTime
				if self.idleWitchFrame >= len(self.idleWitchAnimationList):
					self.idleWitchFrame = 0

	def displayIdleWitchAnimation(self):
			game.screen.blit(self.idleWitchAnimationList[self.idleWitchFrame], (820, 70))

	def updateAttackWitchAnimation(self):
			currentTime = pygame.time.get_ticks()
			if currentTime - self.lastUpdate >= self.attackWitchAnimationCooldown:
				self.attackWitchFrame += 1
				self.lastUpdate = currentTime
				if self.attackWitchFrame >= len(self.attackWitchAnimationList):
					self.attackWitchFrame = 0
					self.state = 0

	def displayAttackWitchAnimation(self):
			game.screen.blit(self.attackWitchAnimationList[self.attackWitchFrame], (820, 70))

	def updateHealWitchAnimation(self):
			currentTime = pygame.time.get_ticks()
			if currentTime - self.lastUpdate >= self.healWitchAnimationCooldown:
				self.healWitchFrame += 1
				self.lastUpdate = currentTime
				if self.healWitchFrame >= len(self.healWitchAnimationList):
					self.healWitchFrame = 0
					self.state = 0

	def displayHealWitchAnimation(self):
			game.screen.blit(self.healWitchAnimationList[self.healWitchFrame], (820, 70))

	def updateDeathWitchAnimation(self):
			currentTime = pygame.time.get_ticks()
			if currentTime - self.lastUpdate >= self.deathWitchAnimationCooldown:
				self.deathWitchFrame += 1
				self.lastUpdate = currentTime
				if self.deathWitchFrame >= len(self.deathWitchAnimationList):
					self.deathWitchFrame = 0
					self.state = 0

	def displayDeathWitchAnimation(self):
			game.screen.blit(self.deathWitchAnimationList[self.deathWitchFrame], (820, 70))

	### Golem animation methods ###

	def updateIdleGolemAnimation(self):
			currentTime = pygame.time.get_ticks()
			if currentTime - self.lastUpdate >= self.idleGolemAnimationCooldown:
				self.idleGolemFrame += 1
				self.lastUpdate = currentTime
				if self.idleGolemFrame >= len(self.idleGolemAnimationList):
					self.idleGolemFrame = 0

	def displayIdleGolemAnimation(self):
			game.screen.blit(self.idleGolemAnimationList[self.idleGolemFrame], (950, 180))

	def updateAttackGolemAnimation(self):
			currentTime = pygame.time.get_ticks()
			if currentTime - self.lastUpdate >= self.attackGolemAnimationCooldown:
				self.attackGolemFrame += 1
				self.lastUpdate = currentTime
				if self.attackGolemFrame >= len(self.attackGolemAnimationList):
					self.attackGolemFrame = 0
					self.state = 0

	def displayAttackGolemAnimation(self):
			game.screen.blit(self.attackGolemAnimationList[self.attackGolemFrame], (950, 180))

	def updateDefenceGolemAnimation(self):
			currentTime = pygame.time.get_ticks()
			if currentTime - self.lastUpdate >= self.defenceGolemAnimationCooldown:
				self.defenceGolemFrame += 1
				self.lastUpdate = currentTime
				if self.defenceGolemFrame >= len(self.defenceGolemAnimationList):
					self.defenceGolemFrame = 0
					self.state = 0

	def displayDefenceGolemAnimation(self):
			game.screen.blit(self.defenceGolemAnimationList[self.defenceGolemFrame], (950, 180))

	def updateDeathGolemAnimation(self):
			currentTime = pygame.time.get_ticks()
			if currentTime - self.lastUpdate >= self.deathGolemAnimationCooldown:
				self.deathGolemFrame += 1
				self.lastUpdate = currentTime
				if self.deathGolemFrame >= len(self.deathGolemAnimationList):
					self.deathGolemFrame = 0
					self.state = 0

	def displayDeathGolemAnimation(self):
			game.screen.blit(self.deathGolemAnimationList[self.deathGolemFrame], (950, 220))

	### Slayer animation methods ###

	def updateIdleSlayerAnimation(self):
			currentTime = pygame.time.get_ticks()
			if currentTime - self.lastUpdate >= self.idleSlayerAnimationCooldown:
				self.idleSlayerFrame += 1
				self.lastUpdate = currentTime
				if self.idleSlayerFrame >= len(self.idleSlayerAnimationList):
					self.idleSlayerFrame = 0

	def displayIdleSlayerAnimation(self):
			game.screen.blit(self.idleSlayerAnimationList[self.idleSlayerFrame], (950, 180))

	def updateAttackSlayerAnimation(self):
			currentTime = pygame.time.get_ticks()
			if currentTime - self.lastUpdate >= self.attackSlayerAnimationCooldown:
				self.attackSlayerFrame += 1
				self.lastUpdate = currentTime
				if self.attackSlayerFrame >= len(self.attackSlayerAnimationList):
					self.attackSlayerFrame = 0
					self.state = 0

	def displayAttackSlayerAnimation(self):
			game.screen.blit(self.attackSlayerAnimationList[self.attackSlayerFrame], (950, 180))

	def updateDrainSlayerAnimation(self):
			currentTime = pygame.time.get_ticks()
			if currentTime - self.lastUpdate >= self.drainSlayerAnimationCooldown:
				self.drainSlayerFrame += 1
				self.lastUpdate = currentTime
				if self.drainSlayerFrame >= len(self.drainSlayerAnimationList):
					self.drainSlayerFrame = 0
					self.state = 0

	def displayDrainSlayerAnimation(self):
			game.screen.blit(self.drainSlayerAnimationList[self.drainSlayerFrame], (950, 180))

	def updateDeathSlayerAnimation(self):
			currentTime = pygame.time.get_ticks()
			if currentTime - self.lastUpdate >= self.deathSlayerAnimationCooldown:
				self.deathSlayerFrame += 1
				self.lastUpdate = currentTime
				if self.deathSlayerFrame >= len(self.deathSlayerAnimationList):
					self.deathSlayerFrame = 0
					self.state = 0

	def displayDeathSlayerAnimation(self):
			game.screen.blit(self.deathSlayerAnimationList[self.deathSlayerFrame], (950, 220))

	def updateToxicSlayerAnimation(self):
			currentTime = pygame.time.get_ticks()
			if currentTime - self.lastUpdate >= self.toxicSlayerAnimationCooldown:
				self.toxicSlayerFrame += 1
				self.lastUpdate = currentTime
				if self.toxicSlayerFrame >= len(self.toxicSlayerAnimationList):
					self.toxicSlayerFrame = 0
					self.state = 0

	def displayToxicSlayerAnimation(self):
			game.screen.blit(self.toxicSlayerAnimationList[self.toxicSlayerFrame], (950, 220))

	### Sorcerer animation methods ###

	def updateIdleSorcererAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.idleSorcererAnimationCooldown:
			self.idleSorcererFrame += 1
			self.lastUpdate = currentTime
			if self.idleSorcererFrame >= len(self.idleSorcererAnimationList):
				self.idleSorcererFrame = 0

	def displayIdleSorcererAnimation(self):
		game.screen.blit(self.idleSorcererAnimationList[self.idleSorcererFrame], (950, 180))

	def updateAttackSorcererAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.attackSorcererAnimationCooldown:
			self.attackSorcererFrame += 1
			self.lastUpdate = currentTime
			if self.attackSorcererFrame >= len(self.attackSorcererAnimationList):
				self.attackSorcererFrame = 0
				self.state = 0

	def displayAttackSorcererAnimation(self):
		game.screen.blit(self.attackSorcererAnimationList[self.attackSorcererFrame], (950, 180))

	def updateCurseSorcererAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.curseSorcererAnimationCooldown:
			self.curseSorcererFrame += 1
			self.lastUpdate = currentTime
			if self.curseSorcererFrame >= len(self.curseSorcererAnimationList):
				self.curseSorcererFrame = 0
				self.state = 0

	def displayCurseSorcererAnimation(self):
		game.screen.blit(self.curseSorcererAnimationList[self.curseSorcererFrame], (950, 180))

	def updateDeathSorcererAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.deathSorcererAnimationCooldown:
			self.deathSorcererFrame += 1
			self.lastUpdate = currentTime
			if self.deathSorcererFrame >= len(self.deathSorcererAnimationList):
				self.deathSorcererFrame = 0
				self.state = 0

	def displayDeathSorcererAnimation(self):
		game.screen.blit(self.deathSorcererAnimationList[self.deathSorcererFrame], (950, 220))

	### Sorcerer animation methods ###

	def updateIdleNightbornAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.idleNightbornAnimationCooldown:
			self.idleNightbornFrame += 1
			self.lastUpdate = currentTime
			if self.idleNightbornFrame >= len(self.idleNightbornAnimationList):
				self.idleNightbornFrame = 0

	def displayIdleNightbornAnimation(self):
		game.screen.blit(self.idleNightbornAnimationList[self.idleNightbornFrame], (950, 180))

	def updateAttackNightbornAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.attackNightbornAnimationCooldown:
			self.attackNightbornFrame += 1
			self.lastUpdate = currentTime
			if self.attackNightbornFrame >= len(self.attackNightbornAnimationList):
				self.attackNightbornFrame = 0
				self.state = 0

	def displayAttackNightbornAnimation(self):
		game.screen.blit(self.attackNightbornAnimationList[self.attackNightbornFrame], (950, 180))

	def updateStunNightbornAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.stunNightbornAnimationCooldown:
			self.stunNightbornFrame += 1
			self.lastUpdate = currentTime
			if self.stunNightbornFrame >= len(self.stunNightbornAnimationList):
				self.stunNightbornFrame = 0
				self.state = 0

	def displayStunNightbornAnimation(self):
		game.screen.blit(self.stunNightbornAnimationList[self.stunNightbornFrame], (950, 180))

	def updateDeathNightbornAnimation(self):
		currentTime = pygame.time.get_ticks()
		if currentTime - self.lastUpdate >= self.deathNightbornAnimationCooldown:
			self.deathNightbornFrame += 1
			self.lastUpdate = currentTime
			if self.deathNightbornFrame >= len(self.deathNightbornAnimationList):
				self.deathNightbornFrame = 0
				self.state = 0

	def displayDeathNightbornAnimation(self):
		game.screen.blit(self.deathNightbornAnimationList[self.deathNightbornFrame], (950, 220))

	### Display defined by enemy name ###

	def currentDisplayAnimation(self, enemy):
		if enemy.getEnemyName() == 'skeleton':
			if self.state == 0 and enemy.deadStatus == 0:
				self.updateIdleSkeletonAnimation()
				self.displayIdleSkeletonAnimation()
			elif self.state == 1:
				self.updateReviveSkeletonAnimation()
				self.displayReviveSkeletonAnimation()
			elif self.state == 2:
				self.updateAttackSkeletonAnimation()
				self.displayAttackSkeletonAnimation()
			elif self.state == 3:
				self.updateDeathSkeletonAnimation()
				self.displayDeathSkeletonAnimation()
		elif enemy.getEnemyName() == 'minotaur':
			if self.state == 0 and enemy.deadStatus == 0:
				self.updateIdleMinotaurAnimation()
				self.displayIdleMinotaurAnimation()
			elif self.state == 1:
				self.updateAttackMinotaurAnimation()
				self.displayAttackMinotaurAnimation()
			elif self.state == 2:
				self.updateStunMinotaurAnimation()
				self.displayStunMinotaurAnimation()
			elif self.state == 3:
				self.updateHealMinotaurAnimation()
				self.displayHealMinotaurAnimation()
			elif self.state == 4:
				self.updateDeathMinotaurAnimation()
				self.displayDeathMinotaurAnimation()
		elif enemy.getEnemyName() == 'witch':
			if self.state == 0 and enemy.deadStatus == 0:
				self.updateIdleWitchAnimation()
				self.displayIdleWitchAnimation()
			elif self.state == 1:
				self.updateAttackWitchAnimation()
				self.displayAttackWitchAnimation()
			elif self.state == 2:
				self.updateHealWitchAnimation()
				self.displayHealWitchAnimation()
			elif self.state == 3:
				self.updateDeathWitchAnimation()
				self.displayDeathWitchAnimation()
		elif enemy.getEnemyName() == 'golem':
			if self.state == 0 and enemy.deadStatus == 0:
				self.updateIdleGolemAnimation()
				self.displayIdleGolemAnimation()
			elif self.state == 1:
				self.updateAttackGolemAnimation()
				self.displayAttackGolemAnimation()
			elif self.state == 2:
				self.updateDefenceGolemAnimation()
				self.displayDefenceGolemAnimation()
			elif self.state == 3:
				self.updateDeathGolemAnimation()
				self.displayDeathGolemAnimation()
		elif enemy.getEnemyName() == 'slayer':
			if self.state == 0 and enemy.deadStatus == 0:
				self.updateIdleSlayerAnimation()
				self.displayIdleSlayerAnimation()
			elif self.state == 1:
				self.updateAttackSlayerAnimation()
				self.displayAttackSlayerAnimation()
			elif self.state == 2:
				self.updateDrainSlayerAnimation()
				self.displayDrainSlayerAnimation()
			elif self.state == 3:
				self.updateToxicSlayerAnimation()
				self.displayToxicSlayerAnimation()
			elif self.state == 4:
				self.updateDeathSlayerAnimation()
				self.displayDeathSlayerAnimation()
		elif enemy.getEnemyName() == 'sorcerer':
			if self.state == 0 and enemy.deadStatus == 0:
				self.updateIdleSorcererAnimation()
				self.displayIdleSorcererAnimation()
			elif self.state == 1:
				self.updateAttackSorcererAnimation()
				self.displayAttackSorcererAnimation()
			elif self.state == 2:
				self.updateCurseSorcererAnimation()
				self.displayCurseSorcererAnimation()
			elif self.state == 3:
				self.updateDeathSorcererAnimation()
				self.displayDeathSorcererAnimation()
		elif enemy.getEnemyName() == 'nightBorn':
			if self.state == 0 and enemy.deadStatus == 0:
				self.updateIdleNightbornAnimation()
				self.displayIdleNightbornAnimation()
			elif self.state == 1:
				self.updateAttackNightbornAnimation()
				self.displayAttackNightbornAnimation()
			elif self.state == 2:
				self.updateStunNightbornAnimation()
				self.displayStunNightbornAnimation()
			elif self.state == 3:
				self.updateDeathNightbornAnimation()
				self.displayDeathNightbornAnimation()