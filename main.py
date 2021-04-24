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