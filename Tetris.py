import pygame, random

boardWidth = 10
boardHeight = 20
blockSize = 40

intToColor = [(0,0,0), (170, 200, 255), (0, 0, 255), (140, 90, 30), (255, 255, 0), (0, 255, 0), (140, 0, 80), (255, 0, 0)]

# This is an array of arrays each holding information about the point at that location
# Defined as cells[x][y] is an integer
cells = []
height = boardHeight

# This is an array of positions
# Defined as activeCells[i] = [x,y]
activeCells = []
activeInt = 1

# This represents how fast the game goes in frames per second
gameSpeed = 3
gameDelay = 0

running = True

window = pygame.display.set_mode((boardWidth * blockSize, boardHeight * blockSize))
clock = pygame.time.Clock()

#Create an empty array of size [boardWidth][boardHeight]
def getEmptyBoard():
    global boardWidth, boardHeight
    cells = [[0 for x in range(boardHeight)] for y in range(boardWidth)]
    return cells

# intitalize cells and activeCells to an empty board
def createBoard():
    global cells, activeCells
    cells = getEmptyBoard()
    # activeCells = []
    # count = 4
    # while count > 0:
    #     activeCells.append([random.randint(0, boardWidth - 1), random.randint(0, boardHeight - 1)])
    #     count -= 1

    # for x in activeCells:
    #     cells[x[0]][x[1]] = activeInt
        

def updateActiveCells():
    for cell in activeCells:
        cells[cell[0], cell[1]] = activeInt

# Creates a new piece
def genPiece():
    global activeInt, activeCells
    center = (boardWidth - 1) // 2
    activeCells.append([0, center])
    formation = random.randint(1, 7)
    
    # Formation 1 refers to the T shape
    if formation == 1:
        activeCells.append([0, center + 1])
        activeCells.append([0, center - 1])
        activeCells.append([1, center])
    # Formation 2 refers to the S shape flipped on its side
    elif formation == 2:
        activeCells.append([1, center])
        activeCells.append([1, center + 1])
        activeCells.append([2, center + 1])
    # Formation 3 refers to the Z shape flipped on its side
    elif formation == 3:
        activeCells.append([1, center])
        activeCells.append([1, center - 1])
        activeCells.append([2, center - 1])
    # Formation 4 refers to the O shape (even though it's clearly a square and no one can convince me otherwise)
    elif formation == 4:
        activeCells.append([0, center + 1])
        activeCells.append([1, center])
        activeCells.append([1, center + 1])
    # Formation 5 refers to the L shape
    elif formation == 5:
        activeCells.append([1, center])
        activeCells.append([2, center])
        activeCells.append([2, center + 1])
    # Formation 6 refers to the J shape
    elif formation == 6:
        activeCells.append([1, center])
        activeCells.append([2, center])
        activeCells.append([2, center - 1])
    # Formation 7 refers to the I shape (a.k.a, the best shape)
    elif formation == 7:
        for i in range(1, 3):
            activeCells.append([i, center])
    
    updateActiveCells()
    
def getActiveSquare():
    global activeCells
    activeSquare = []
    index = 0
    for x in activeCells:
        for y in activeCells:
            if not(checkPositionEmpty(x, y)):
                activeSquare.append(activeCells[index])
            index += 1
    if len(activeSquare != 4):
        raise Exception("The active square cannot contain more or less than four units!")
    else:
        return activeSquare

def rotateActive():
    global activeCells

# Check if position [x][y] is empty in the cells 2D array
def checkPositionEmpty(x, y):
    return cells[x][y] != activeInt

# Move the activeCells into the cells 2D array and gen a new piece
def snapActive():
    global activeCells
    for cell in activeCells:
        cells[cell[0], cell[1]] = 2
    genPiece()

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
