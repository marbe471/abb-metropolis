import pygame

FontColor = (255,255,255)
FontSize = 20

class Button(pygame.sprite.Sprite):

	def __init__(self, arg,h,w):
		self.text = arg
		self.height = h
		self.width = w
		self.image = pygame.Surface([self.height,self.width],pygame.SRCALPHA, 32)
		self.image.fill((0,0,255))
		self.font = pygame.font.SysFont('Helvetica', FontSize)
		self.text = self.font.render(self.text, True, FontColor)
		self.image.blit(self.text,(0,0))
		self.rect = self.image.get_rect()

	def getButton(self):
		return self.image

class ImageButton(pygame.sprite.Sprite):

	def __init__(self, url):
		self.image = pygame.image.load(url)
		self.rect = self.image.get_rect()

	def getButton(self):
		return self.image