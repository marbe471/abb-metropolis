import pygame, sys, math ,pygame.gfxdraw

energyColor = (255,255,0)

class Energybar():
	"""docstring for Energybar"""
	def __init__(self, arg):
		self.image = pygame.Surface([arg,10])
		self.image.fill(energyColor)
		self.arg = arg
	def update(self,arg):
		self.image = pygame.Surface([arg,10])
		self.image.fill(energyColor)
		return self.image		

