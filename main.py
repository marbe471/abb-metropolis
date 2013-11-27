import sys, pygame, glob, pygame.mixer, math, random, button,tree,obj,energybar
from pygame import *
from button import ImageButton
from button import Button
from tree import tree
from obj import obj
from obj import House
from energybar import Energybar
def paintScene():
	screen.fill((18,152,248))
	if startScreen:
		screen.blit(logoText,(384,400))
	else:
		screen.blit(ground.getImage(),(groundXpos,groundYpos))
		screen.blit(houseBtn.getButton(),(houseXpos,houseYpos))
		if movingHouse:
			screen.blit(house1.getImage(),(house1.getX(),house1.getY()))
		screen.blit(buildingObj.getImage(),(buildingObj.getX(),buildingObj.getY()))
		for currentHouse in houseList:
			screen.blit(currentHouse.getImage(),(currentHouse.getX(),currentHouse.getY()))
			if currentHouse.getShowInfo():
				info = currentHouse.getInfo();
				infoText = fontScore.render(" $TEST " + info, True, (240,240,240))	
				screen.blit(infoText,(100,10))
		for currentBuilding in buildingList:
			screen.blit(currentBuilding.getImage(),(currentBuilding.getX(),currentBuilding.getY()))
			if currentBuilding.getShowInfo():
				screen.blit(knapp.getButton(),(10,10))

		scoreText = fontScore.render(" $ " + str(CASH), True, (240,240,240))	
		screen.blit(scoreText,[220,20])
		screen.blit(energyBar.update(ENERGY),(350,20))

#Init pygame
pygame.init()
SCREEN_HEIGHT=768
SCREEN_WIDTH=1280
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("ABB metropolis")
fontScore = pygame.font.SysFont('8-bit Limit BRK', 16)
clock = pygame.time.Clock()
startScreen = True
houseXpos = 40
houseYpos = 40
groundXpos = 50
groundYpos = 50
buildingXpos = 40
buildingYpos = 200
knapp = Button("Information om byggnad",500,500)


# GAME VARIABLES
CASH = 10000;
ENERGY = 100;
energyBar = Energybar(ENERGY)

#Load gfx sprites
logoText = pygame.image.load("gfx/x-ABB Metropolis.png")
ground = obj("gfx/ground.png")
ground.rect.x = groundXpos
ground.rect.y = groundYpos
house1 = obj("gfx/houses/02.png")
house1.setPos(houseXpos,houseYpos)
houseBtn = Button("Hus",64,100)
houseBtn.rect.x = houseXpos
houseBtn.rect.y = houseYpos
buildingObj = obj("gfx/building.png")
buildingObj.setPos(buildingXpos,buildingYpos)
buildingBtn = ImageButton("gfx/building.png")
buildingBtn.rect.x = buildingXpos
buildingBtn.rect.y = buildingYpos


#All sprites
houseList = []
buildingList = []

# The main loop for the game
mouseX,mouseY = pygame.mouse.get_pos()
mouseX=0
mouseY=0
ypos=0
xpos=0
mousePos = [0,0]
movingHouse = False
movingBuilding = False

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
			else:	
				mouseX,mouseY = pygame.mouse.get_pos()
				if houseBtn.rect.collidepoint(mouseX,mouseY):
					movingHouse = True
				elif buildingBtn.rect.collidepoint(mouseX,mouseY):
					movingBuilding = True
				else:
					for currentBuilding in buildingList:
						if currentBuilding.rect.collidepoint(mouseX,mouseY):
							currentBuilding.setShowInfo(True)
						else:
							currentBuilding.setShowInfo(False)
					for currentHouse in houseList:
						if currentHouse.rect.collidepoint(mouseX,mouseY):
							currentHouse.setShowInfo(True)
						else:
							currentHouse.setShowInfo(False)
						
				
					
		elif event.type == MOUSEBUTTONUP:
			mouseX,mouseY = pygame.mouse.get_pos()
			if movingHouse:
				if ground.rect.collidepoint(mouseX,mouseY):
					houseNew = House()
					houseNew.setPos(mouseX-10,mouseY-10)
					houseList.append(houseNew)
					CASH= CASH - houseNew.cost
					ENERGY = ENERGY + houseNew.energy
				house1.setPos(houseXpos,houseYpos)
				movingHouse = False	
			if movingBuilding:
				if ground.rect.collidepoint(mouseX,mouseY):
					buildingNew = obj("gfx/building.png")
					buildingNew.setPos(mouseX-10,mouseY-10)
					buildingList.append(buildingNew)
				buildingObj.setPos(buildingXpos,buildingYpos)
				movingBuilding = False

	
	if movingHouse:
		mouseX,mouseY = pygame.mouse.get_pos()
		house1.setPos(mouseX-10,mouseY-10)

	if movingBuilding:
		mouseX,mouseY = pygame.mouse.get_pos()
		buildingObj.setPos(mouseX-10,mouseY-10)

	paintScene()
	pygame.display.update()