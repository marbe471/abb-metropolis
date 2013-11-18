import pygame

class tree(pygame.sprite.Sprite):
	
	def __init__(self,url):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(url)
		self.x = 0
		self.y = 0

	def setPos(self,x,y):
		self.x = x
		self.y = y

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getTree(self):
		return self.image