import pygame
import time
import random

# Setuping the Pygame - the overall display

#Init pygame
pygame.init()

# Defining the colors
white = (255, 255, 255)
orange = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

width, height = 600, 400

gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")

# Setting the clock - it will keep the whole thing running
clock = pygame.time.Clock()

# Setting the snake's size and speed
snakeSize = 10
snakeSpeed = 15

# Setting the font
messageFont = pygame.font.SysFont('ubuntu', 30)
scoreFont = pygame.font.SysFont('ubuntu', 25)

# Defining the functions - updating/drawing the score and the snake wrt the position
def printScore(score):
    text = scoreFont.render("Score: "+str(score), True, orange)
    gameDisplay.blit(text, [0,0])

def drawSnake(snakeSize,snakeList):
    for pixel in snakeList:
        pygame.draw.rect(gameDisplay, white, [pixel[0], pixel[1], snakeSize, snakeSize])

def message(msg, color):
    gameMessage = messageFont.render(msg,True,color)
    gameDisplay(gameMessage, [width/6, height/3])

# Defining the functions - run function
def runGame():
    gameOver = False
    gameClose = False

    # define the starting postn
    x = width/2
    y = height/2

    #setting the default speed - before starting the speed
    xSpeed = 0
    ySpeed = 0

    # defining the snake as a list since the snake is going to grow in size
    snakeList = []
    snakeLength = 1

    #spawn a random target for food
    xTarget = round(random.randrange(0,width-snakeSize)/10.0) * 10.0
    yTarget = round(random.randrange(0,height-snakeSize)/10.0) * 10.0

    # the main game loop
    while not gameOver:

        # game close
        while gameClose == True:
            gameDisplay.fill(black)
            gameOverMessage = messageFont.render("Game Over", True, red)
            gameOver.blit(gameOverMessage, [width/2,height/2])
            printScore(snakeLength-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_c:
                        runGame()
                # if event.type == pygame.QUIT:
                #     gameOver = True
                #     gameClose = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True

                # Which key we actually press
                if event.type == pygame.KEYDOWN:
                    # left key
                    if event.key == pygame.K_LEFT:
                        xSpeed = -snakeSize # negative becoz = the more we move right the x coordinate will inc so in order to go left we need to dec the x coordinate
                        ySpeed = 0 # becoz we dont need the snake move diagonally
                    if event.key == pygame.K_RIGHT:
                        xSpeed = snakeSize # no movement  in X dir
                        ySpeed = 0
                    if event.key == pygame.K_UP:
                        xSpeed = 0 
                        ySpeed = -snakeSize # negative becoz = the more we move down the y coordinate will inc so in order to go up we need to dec the y coordinate
                    if event.key == pygame.K_DOWN:
                        xSpeed = 0
                        ySpeed = snakeSize 

        # if we hit the boundary or go out it => close the game

        if x >= width or x < 0 or y >= height or y < 0:
            gameClose = True
        
        # if we do nothing - speed inc

        x += xSpeed
        y += ySpeed

        # setting the pygame window
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, orange, [xTarget,yTarget,snakeSize,snakeSize])

        # movement of the snake wrt head and tail
        snakeHead = []
        snakeHead.append([x,y])
        if len(snakeList) > snakeLength:
            del snakeList[0]

        #collision - close
        for pixel in snakeList[:-1]:
            if pixel == snakeHead: 
                gameClose = True
        
        drawSnake(snakeSize, snakeList)
        printScore(snakeLength-1)

        pygame.display.update()

        if x == xTarget and y == yTarget:
            xTarget = round(random.randrange(0,width-snakeSize)/10.0) * 10.0
            yTarget = round(random.randrange(0,height-snakeSize)/10.0) * 10.0
            snakeLength +=1
        
        clock.tick(snakeSpeed)

    pygame.quit()
    quit()

runGame()