import sys, pygame, glob, pygame.mixer, math, random, button,tree,obj,energybar,map
from pygame import *
from button import ImageButton
from button import Button
from tree import tree
from obj import obj
from obj import House
from obj import Turbine
from energybar import Energybar
from map import Map
def paintScene():
	screen.fill((18,152,248))
	if startScreen:
		screen.blit(logoText,(384,400))
	else:
		# screen.blit(ground.getImage(),(groundXpos,groundYpos))
		screen.blit(levelMap.ground,(groundXpos,groundYpos))
		screen.blit(houseBtn.getButton(),(houseXpos,houseYpos))
		if movingHouse:
			screen.blit(house1.getImage(),(house1.getX(),house1.getY()))
		screen.blit(turbineObj.getImage(),(turbineObj.getX(),turbineObj.getY()))
		for currentHouse in houseList:
			screen.blit(currentHouse.getImage(),(currentHouse.getX(),currentHouse.getY()))
		for currentTurbine in turbineList:
			screen.blit(currentTurbine.getImage(),(currentTurbine.getX(),currentTurbine.getY()))
			
		for currentHouse in houseList:
			if currentHouse.getShowInfo() and infoScreen:
				showInfo(currentHouse)
		for currentTurbine in turbineList:
			if currentTurbine.showInfo and infoScreen:
				showInfo(currentTurbine)

		paintHUD()


def showInfo(obj):
	rect = pygame.Surface((500,300), pygame.SRCALPHA, 32)
	rect.fill((255, 255, 255, 70))
	infoText = gameFont.render(" Information " + obj.info, True, (240,240,240))	
	upgradeText = gameFont.render(" Upgrade? ", True, (0,0,0))
	rect.blit(upgradeText,(400,250))
	rect.blit(infoText,(5,5))
	screen.blit(rect, (350,200))
	
	

def paintHUD():
	rect = pygame.Surface((150,80), pygame.SRCALPHA, 32)
	rect.fill((255, 255, 255, 50))
	screen.blit(rect, (10,10))
	cashText = gameFont.render(str(CASH), True, (240,240,240))	
	screen.blit(cashSign,(20,15))
	screen.blit(cashText,[40,20])
	screen.blit(energySign,(20,60))
	screen.blit(energyBar.update(ENERGY),(40,60))

#Init pygame
pygame.init()
SCREEN_HEIGHT=768
SCREEN_WIDTH=1280
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("ABB metropolis")
gameFont = pygame.font.SysFont('Helvetica', 20)
clock = pygame.time.Clock()
startScreen = True
houseXpos = 40
houseYpos = 140
groundXpos = 200
groundYpos = 50
turbineXpos = 40
turbineYpos = 200
levelMap = Map(10);

# GAME VARIABLES
CASH = 10000;
ENERGY = 100;
energyBar = Energybar(ENERGY)

#Load gfx sprites
logoText = pygame.image.load("gfx/x-ABB Metropolis.png")
cashSign = pygame.image.load("gfx/cash.png")
energySign = pygame.image.load("gfx/bolt.png")
ground = obj("gfx/ground.png")
ground.rect.x = groundXpos
ground.rect.y = groundYpos
house1 = obj("gfx/houses/02.png")
house1.setPos(houseXpos,houseYpos)
houseBtn = Button("Hus",64,20)
houseBtn.rect.x = houseXpos
houseBtn.rect.y = houseYpos
turbineObj = Turbine()
turbineObj.setPos(turbineXpos,turbineYpos)
turbineBtn = ImageButton("gfx/placeholder.png")
turbineBtn.rect.x = turbineXpos
turbineBtn.rect.y = turbineYpos



#All sprites
houseList = []
turbineList = []

# The main loop for the game
mouseX,mouseY = pygame.mouse.get_pos()
mouseX=0
mouseY=0
ypos=0
xpos=0
mousePos = [0,0]
movingHouse = False
movingTurbine = False
infoScreen = False

while 1:
	clock.tick(60)


	#Eventhandling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
		 sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			if startScreen:
				startScreen = False
			if infoScreen:
				infoScreen = False
			else:	
				mouseX,mouseY = pygame.mouse.get_pos()
				if houseBtn.rect.collidepoint(mouseX,mouseY):
					movingHouse = True
				elif turbineBtn.rect.collidepoint(mouseX,mouseY):
					movingTurbine = True
				else:
					for currentTurbine in turbineList:
						if currentTurbine.rect.collidepoint(mouseX,mouseY):
							currentTurbine.setShowInfo(True)
							infoScreen = True
						else:
							currentTurbine.setShowInfo(False)
					for currentHouse in houseList:
						if currentHouse.rect.collidepoint(mouseX,mouseY):
							currentHouse.setShowInfo(True)
							infoScreen = True
						else:
							currentHouse.setShowInfo(False)
						
				
					
		elif event.type == MOUSEBUTTONUP:
			mouseX,mouseY = pygame.mouse.get_pos()
			if movingHouse:
				if ground.rect.collidepoint(mouseX,mouseY):
					houseNew = House()
					if CASH >= houseNew.cost:
						houseNew.setPos(mouseX-10,mouseY-10)
						houseList.append(houseNew)
						CASH= CASH - houseNew.cost
						ENERGY = ENERGY + houseNew.energy
						house1.setPos(houseXpos,houseYpos)

				movingHouse = False	
			if movingTurbine:
				if ground.rect.collidepoint(mouseX,mouseY):
					turbineNew = Turbine()
					if CASH >= turbineNew.cost:
						CASH= CASH - turbineNew.cost
						ENERGY = ENERGY + turbineNew.energy
						turbineNew.setPos(mouseX-10,mouseY-10)
						turbineList.append(turbineNew)
						turbineObj.setPos(turbineXpos,turbineYpos)

				movingTurbine = False

	
	if movingHouse:
		mouseX,mouseY = pygame.mouse.get_pos()
		house1.setPos(mouseX-10,mouseY-10)

	if movingTurbine:
		mouseX,mouseY = pygame.mouse.get_pos()
		turbineObj.setPos(mouseX-10,mouseY-10)

	paintScene()
	pygame.display.update()