
from time import *
from random import *
from pygame import *
import pygame

from Rules import Rules
from Player import Player
from Block import Block

from BlockBase import BlockBase
from Scene import Scene

from BlockImage import BlockImage
from BlockRectangle import BlockRectangle
from BlockScoreboard import BlockScoreboard

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

s = Scene(screen, size[0], size[1], 30, 21, 3)
b1 = BlockImage("dice1.png-1", "dice1.png", s, 1, 1)
b2 = BlockImage("dice2.png-1", "dice2.png", s, 5, 1)
b3 = BlockImage("dice3.png-1", "dice3.png", s, 9, 1)
b4 = BlockImage("dice4.png-1", "dice4.png", s, 13, 1)
b5 = BlockImage("dice5.png-1", "dice5.png", s, 17, 1)
r4 = BlockScoreboard("scoreboard.png", "scoreboard.png", s, 21, 1)

s.addItem(b1)
s.addItem(b2)
s.addItem(b3)
s.addItem(b4)
s.addItem(b5)
s.addItem(r4)

while not done:
    mouse_pos = pygame.mouse.get_pos() # gets mouse position
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:

            key = "dice2.png-1"
            if s.isClicked(key, mouse_pos):
                item = s.itemList[key]
                pos = (item.x, item.y)
                if item.y == 1:
                    item.y = 3
                else:
                    item.y = 1
                    
                item.updatePosition(item.x, item.y)
                
                print("clicked1")
                
         # --- Game logic should go here
 
        # -- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(backgroundColor)

        s.draw()
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

# Close the window and quit.
pygame.quit()
            
