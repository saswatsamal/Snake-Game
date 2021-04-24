import pygame
import time
import random

# Setuping the Pygame - the overall display

#Init pygame
pygame.init()

# Defining the colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
orange = (255,165,0)

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

def drawSnake(snakeSize,snakePixels):
    for pixel in snakePixels:
        pygame.draw.rect(gameDisplay, white, [pixel[0], pixel[1], snakeSize, snakeSize])

