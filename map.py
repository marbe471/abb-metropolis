import pygame

class Map(object):
	"""docstring for Map"""
	def __init__(self, numberOfTiles):
		self.number= numberOfTiles
		grass = pygame.image.load("gfx/grass.png")
		self.ground = pygame.Surface((grass.get_rect().width*numberOfTiles+50,grass.get_rect().height*numberOfTiles), pygame.SRCALPHA, 32)
		for y in xrange(0,numberOfTiles*2):
			for x in xrange(0,numberOfTiles):
				if y % 2 == 0:
					self.ground.blit(grass,(x*100,30+25*y))
				else:
					self.ground.blit(grass,(x*100+50,25*y+30))
				
