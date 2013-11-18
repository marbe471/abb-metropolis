import sys, pygame, glob, pygame.mixer, math, random, button,tree,obj
from pygame import *
from button import ImageButton
from tree import tree
from obj import obj
def paintScene():
	screen.fill((100,0,100))
	if startScreen:
		screen.blit(logoText,(384,400))
	else:
		screen.blit(ground.getImage(),(groundXpos,groundYpos))
		screen.blit(treeBtn.getButton(),(treeXpos,treeYpos))
		screen.blit(treeObj.getImage(),(treeObj.getX(),treeObj.getY()))
		screen.blit(buildingObj.getImage(),(buildingObj.getX(),buildingObj.getY()))
		for obj in treeList:
			screen.blit(obj.getImage(),(obj.getX(),obj.getY()))
		for obj in buildingList:
			screen.blit(obj.getImage(),(obj.getX(),obj.getY()))

#Init pygame
pygame.init()
SCREEN_HEIGHT=768
SCREEN_WIDTH=1280
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("ABB metropolis")
clock = pygame.time.Clock()
startScreen = True
treeXpos = 40
treeYpos = 40
groundXpos = 50
groundYpos = 50
buildingXpos = 40
buildingYpos = 200

#Load gfx sprites
logoText = pygame.image.load("gfx/x-ABB Metropolis.png")
ground = obj("gfx/ground.png")
ground.rect.x = groundXpos
ground.rect.y = groundYpos
treeObj = obj("gfx/tree.png")
treeObj.setPos(treeXpos,treeYpos)
treeBtn = ImageButton("gfx/tree.png")
treeBtn.rect.x = treeXpos
treeBtn.rect.y = treeYpos
buildingObj = obj("gfx/building.png")
buildingObj.setPos(buildingXpos,buildingYpos)
buildingBtn = ImageButton("gfx/building.png")
buildingBtn.rect.x = buildingXpos
buildingBtn.rect.y = buildingYpos


#All sprites
treeList = []
buildingList = []

# The main loop for the game
mouseX,mouseY = pygame.mouse.get_pos()
mouseX=0
mouseY=0
ypos=0
xpos=0
mousePos = [0,0]
movingTree = False
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
				if treeBtn.rect.collidepoint(mouseX,mouseY):
					movingTree = True
				elif buildingBtn.rect.collidepoint(mouseX,mouseY):
					movingBuilding = True
					
					
		elif event.type == MOUSEBUTTONUP:
			mouseX,mouseY = pygame.mouse.get_pos()
			if movingTree:
				if ground.rect.collidepoint(mouseX,mouseY):
					treeNew = obj("gfx/tree.png")
					treeNew.setPos(mouseX-60,mouseY-110)
					treeList.append(treeNew)
				
				treeObj.setPos(treeXpos,treeYpos)
				movingTree = False	
			if movingBuilding:
				if ground.rect.collidepoint(mouseX,mouseY):
					buildingNew = obj("gfx/building.png")
					buildingNew.setPos(mouseX-10,mouseY-10)
					buildingList.append(buildingNew)
				
				buildingObj.setPos(buildingXpos,buildingYpos)
				movingBuilding = False

	
	if movingTree:
		mouseX,mouseY = pygame.mouse.get_pos()
		treeObj.setPos(mouseX-60,mouseY-110)

	if movingBuilding:
		mouseX,mouseY = pygame.mouse.get_pos()
		buildingObj.setPos(mouseX-10,mouseY-10)

	paintScene()
	pygame.display.update()
