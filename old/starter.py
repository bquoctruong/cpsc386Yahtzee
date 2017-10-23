
from time import *
from random import *
from pygame import *
import pygame

from Rules import Rules
from Player import Player
from Block import Block

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
KINDA_GREEN = (0, 170, 0)
   
pygame.init()
pygame.font.init()

screenWidth = 1024
screenHeight = 768

size = ([screenWidth, screenHeight])
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Yahtzee")
pygame.display.set_icon(pygame.image.load("icon.png"))

done = False

clock = pygame.time.Clock()

# Game logic initialization
backgroundColor = KINDA_GREEN

while not done:
    mouse_pos = pygame.mouse.get_pos() # gets mouse position
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

         # --- Game logic should go here
 
        # -- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(backgroundColor)
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

# Close the window and quit.
pygame.quit()
            
