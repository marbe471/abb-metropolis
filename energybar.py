import pygame, sys, math ,pygame.gfxdraw

energyColor = (255,255,0)
criticalColor = (255,0,0)

class Energybar():
	"""docstring for Energybar"""
	def __init__(self, arg):
		self.image = pygame.Surface([arg,10])
		self.image.fill(energyColor)
		self.arg = arg
	def update(self,arg):
		if arg <= 0:
			self.image = pygame.Surface([1,10])
		elif arg >=100:
			self.image = pygame.Surface([100,10])
		else:
			self.image = pygame.Surface([arg,10])

		if arg >=40:
			self.image.fill(energyColor)
		else:
			self.image.fill(criticalColor)
			

		return self.image		
		