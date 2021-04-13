import pygame, random

boardWidth = 10
boardHeight = 20
blockSize = 40

intToColor = [(0,0,0), (170, 200, 255), (0, 0, 255), (140, 90, 30), (255, 255, 0), (0, 255, 0), (140, 0, 80), (255, 0, 0)]

# This is an array of arrays each holding information about the point at that location
# Defined as cells[x][y] is an integer
cells = []
height = boardHeight

# Populate cells with list of possible positions
while height > 0:
    width = boardWidth
    while width > 0:
        cells.append([width, height])
        width -= 1
    height -= 1

# for debugging purposes
for x in cells:
    print(x)

# This is an array of positions
# Defined as activeCells[i] = [x,y]
activeCells = []
activeInt = 0

# This represents how fast the game goes in frames per second
gameSpeed = 3
gameDelay = 0

running = True

window = pygame.display.set_mode((boardWidth * blockSize, boardHeight * blockSize))
clock = pygame.time.Clock()

#Create an empty array of size [boardWidth][boardHeight]
def getEmptyBoard():
    global boardWidth, boardHeight
    cells = []
    height = boardHeight

    # Populate cells with list of possible positions
    while height > 0:
        width = boardWidth
        while width > 0:
            cells.append([width, height])
            width -= 1
        height -= 1
    
    return cells

# intitalize cells and activeCells to an empty board
def createBoard():
    global cells, activeCells
    cells = getEmptyBoard()
    activeCells = []
    count = 4
    while count > 0:
        activeCells.append([random.randint(1, boardWidth), random.randint(1, boardHeight)])
        count -= 1

    for x in activeCells:
        print(x)

# Creates a new piece
def genPiece():
    global activeInt, activeCells
    
def getActiveSquare():
    global activeCells

def rotateActive():
    global activeCells

# Check if position [x][y] is empty in the cells 2D array
def checkPositionEmpty(x, y):
    return True

# Move the activeCells into the cells 2D array and gen a new piece
#def snapActive():

# Move all the activeCells down by one as long as they can all fall, if not, snapActive    
def updateFall():
    global activeCells, boardHeight

# If any rows are completed, empty the row, and move the ones above down one
def updateRows():
    global cells, gameSpeed
        

def drawGame():
    global cells, activeCells, blockSize, window, intToColor
    window.fill((0,0,0))
    for x in range(len(cells)):
        for y in range(len(cells[x])):
            pygame.draw.rect(window, intToColor[cells[x][y]], (x * blockSize + 5, y * blockSize + 5, blockSize - 10, blockSize - 10), 0)
            if activeCells[x][y] != 0:
                pygame.draw.rect(window, intToColor[activeCells[x][y]], (x * blockSize + 5, y * blockSize + 5, blockSize - 10, blockSize - 10), 0)
                
    pygame.display.update()
    

def shiftActive(s):
    global activeCells, boardWidth
    newActiveCells = getEmptyBoard()
    for x in range(len(activeCells)):
        for y in range(len(activeCells[x])):
            if activeCells[x][y] != 0:
                if x + s >= 0 and x + s < boardWidth:
                    newActiveCells[x + s][y] = activeCells[x][y]
                else:
                    return
    activeCells = newActiveCells


def handleKeys():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                shiftActive(-1)
            if event.key == pygame.K_RIGHT:
                shiftActive(1)
            if event.key == pygame.K_UP:
                rotateActive()


def update():
    global gameSpeed, gameDelay
    handleKeys()
    if gameDelay > 1000 / gameSpeed:
        updateFall()
        updateRows()
        gameDelay -= 1000 / gameSpeed
    drawGame()
    
    clock.tick(60)
    gameDelay += 16

    
def init():
    pygame.init()
    createBoard()
    genPiece()


# Starts the Game
def play():
    global running
    while running:
        update()


init()
play()
