import pygame

class obj(pygame.sprite.Sprite):
	
	def __init__(self,url):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(url)
		self.rect = self.image.get_rect()
		self.x = 0
		self.y = 0
		self.showInfo = False

	def setPos(self,x,y):
		self.x = x
		self.y = y
		self.rect.x = x
		self.rect.y = y

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getImage(self):
		return self.image

	def setShowInfo(self,showInfo):
		self.showInfo = showInfo

	def getShowInfo(self):
		return self.showInfo

	def getInfo(self):
		return "Info about building la la la la";

class House(obj):
	"""docstring for house"""
	def __init__(self):
		super(House, self).__init__("gfx/houses/02.png")
		self.cost = 1000
		self.energy = -10
		

class Turbine(object):
	"""docstring for Turbine"""
	def __init__(self):
		super(Turbine, self).__init__()
		self.cost = 1000
		self.energy = 20