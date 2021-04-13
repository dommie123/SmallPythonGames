#Python Snake
import pygame, random

#Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SEGMENTSIZE = 25
WINDOWSIZE = 20	#This is measured in Segments
SPACING = 3

#Inits
pygame.init()

#Vars
running = True;
clock = pygame.time.Clock()
screen = pygame.display.set_mode([SEGMENTSIZE * WINDOWSIZE, SEGMENTSIZE * WINDOWSIZE])
pygame.display.set_caption('Snaaake')

foodPos = [10,10]
snakePos = [[1,3],[1,2],[1,1]]

#Directions are as follows
#   1
# 2 S 0
#   3
direction = 3;

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT and direction != 2:
				direction = 0
			if event.key == pygame.K_LEFT and direction != 0:
				direction = 2
			if event.key == pygame.K_UP and direction != 3:
				direction = 1
			if event.key == pygame.K_DOWN and direction != 1:
				direction = 3
				
	#Update the Snake
	if (direction == 0):
		snakePos.insert(0, [snakePos[0][0] + 1, snakePos[0][1]])
	elif (direction == 1):
		snakePos.insert(0, [snakePos[0][0], snakePos[0][1] - 1])
	elif (direction == 2):
		snakePos.insert(0, [snakePos[0][0] - 1, snakePos[0][1]])
	elif (direction == 3):
		snakePos.insert(0, [snakePos[0][0], snakePos[0][1] + 1])
	#Remove the tail so the snake doesn't grow forever
	if (foodPos not in snakePos):
		snakePos.pop()
	else:
		while foodPos in snakePos:
			foodPos = [random.randint(0, WINDOWSIZE - 1), random.randint(0, WINDOWSIZE - 1)]
	
	#If the head of the snake is in any other part of the snake list, you lose
	if (snakePos[0] in snakePos[1:]):
		exit()
	#If the snake head goes out of bounds, you also lose
	if (snakePos[0][0] == -1 or snakePos[0][0] == WINDOWSIZE or snakePos[0][1] == -1 or snakePos[0][1] == WINDOWSIZE):
		exit()
		
	#Draw the Game
	screen.fill(BLACK)	
	for segment in snakePos:	#Draw all the segments
	
		pygame.draw.rect(screen, WHITE, (
		segment[0] * SEGMENTSIZE + SPACING, 
		segment[1] * SEGMENTSIZE + SPACING, 
		SEGMENTSIZE - SPACING * 2, 
		SEGMENTSIZE - SPACING * 2)
		, 0)	#This is the Thickness of the Rectangle. 0 Is filled in
		
	#Draw the Food
	pygame.draw.rect(screen, RED, (foodPos[0] * 25 + 5, foodPos[1] * 25 + 5, 15, 15), 0)
	
	#Update the screen
	pygame.display.update()
	
	clock.tick(10)
	