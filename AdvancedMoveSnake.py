#Python Snake using pygame
import pygame, random

#Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SEGMENTSIZE = 25
WINDOWSIZE = 20	#This is measured in Segments
SPACING = 4

#Initialize the pygame library
pygame.init()

#Variables
running = True;
clock = pygame.time.Clock()
screen = pygame.display.set_mode([SEGMENTSIZE * WINDOWSIZE, SEGMENTSIZE * WINDOWSIZE])
pygame.display.set_caption('Snake')

#Position of game objects
foodPos = [10,10]
snakePos = [[1,3],
			[1,2],
			[1,1]]

#The "vector" of where the snake is moving
moving = [0, 1]

while running:
	for event in pygame.event.get():
		#This is when they press the X for the window
		if event.type == pygame.QUIT:
			running = False
			
		#If they pressed a key
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT and moving != [-1, 0]:
				moving = [1, 0]
				break
			if event.key == pygame.K_LEFT and moving != [1, 0]:
				moving = [-1, 0]
				break
			if event.key == pygame.K_UP and moving != [0, 1]:
				moving = [0, -1]
				break
			if event.key == pygame.K_DOWN and moving != [0, -1]:
				moving = [0, 1]
				break
				
	#If the head of the snake is in any other part of the snake list, you lose
	if (snakePos[0] in snakePos[1:]):
		exit()
	#If the snake head goes out of bounds, you also lose
	if (snakePos[0][0] == -1 or snakePos[0][0] == WINDOWSIZE or snakePos[0][1] == -1 or snakePos[0][1] == WINDOWSIZE):
		exit()
		
	#Update the Snake
	snakePos.insert(0, [snakePos[0][0] + moving[0], snakePos[0][1] + moving[1]])
	
	#Did the snake get the food
	if (foodPos not in snakePos):
		#If not, the tail will shrink
		snakePos.pop()
	else:
		#If snake got the food, keep generating new positions for it until it is not
		while foodPos in snakePos:
			foodPos = [random.randint(0, WINDOWSIZE - 1), random.randint(0, WINDOWSIZE - 1)]	#random.randint IS INCLUSIVE ON BOTH ENDS
	
	#Clear the screen
	screen.fill(BLACK)
	
	#Draw all the segments of the snake
	for segment in snakePos:	
		#Draw to what screen what color, what rectangle, and what thickness
		pygame.draw.rect(screen, WHITE, (
		segment[0] * SEGMENTSIZE + SPACING, 
		segment[1] * SEGMENTSIZE + SPACING, 
		SEGMENTSIZE - SPACING, 
		SEGMENTSIZE - SPACING)
		, 0)	#This is the Thickness of the Rectangle. 0 Is filled in
		
	#Draw the Food
	pygame.draw.rect(screen, RED, (
		foodPos[0] * SEGMENTSIZE + SPACING, 
		foodPos[1] * SEGMENTSIZE + SPACING, 
		SEGMENTSIZE - SPACING, 
		SEGMENTSIZE - SPACING), 0)
	
	#Update the screen
	pygame.display.update()
	
	#Pause the game for a moment
	clock.tick(10)
	