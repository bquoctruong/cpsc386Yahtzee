
import time
import pygame

from Rules import Rules
from Player import Player
from Block import Block

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def buildDicesPlacementBlockList(dicesPlacement, screen, xPositionList, yPositionList, valueMap):
    dicesPlacementBlockList = []

    for j in range(len(dicesPlacement)):
        for i in range(len(dicesPlacement[j])):
            print(str(i) + ", " + str(j) + ", "+str(xPositionList[i])+str(yPositionList[j]))
            placementInfo = dicesPlacement[j][i];

            if (placementInfo[0] == True):
                val = placementInfo[1];
                if (val < 1):
                    val = 1
                print(str(i) + ", " + str(j) + ", "+str(val)+valueMap[val]+str(xPositionList[i])+str(yPositionList[j]))
                dicesPlacementBlockList.append(Block(screen, valueMap[val], xPositionList[i], yPositionList[j]))
            
    return dicesPlacementBlockList
    
pygame.init()

screenWidth = 1024
screenHeight = 768

size = ([screenWidth, screenHeight])
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Yahtzee")

done = False

clock = pygame.time.Clock()

# Game logic initialization
backgroundColor = WHITE

btnRollDice = pygame.Rect(10, 510, 200, 75) # creates a rect object

#refactor to build (diff=155)
xPositionList = [125, 280, 435, 590, 745]
yPositionList = [10, 300]
valueMap = ["", "dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"];

#(row, col) = (hasDie, value)
dicesPlacement = [[(True, 0), (True, 0), (True, 0), (True, 0), (True, 0)], [(False, 0), (False, 0), (False, 0), (False, 0), (False, 0)] ]

shake = pygame.mixer.Sound("shake.wav")
roll = pygame.mixer.Sound("roll.wav")

dicesPlacementBlockList = buildDicesPlacementBlockList(dicesPlacement, screen, xPositionList, yPositionList, valueMap)

while not done:
    mouse_pos = pygame.mouse.get_pos() # gets mouse position
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if btnRollDice.collidepoint(mouse_pos):
                roll.play()
            
            """elif dice2.rect.collidepoint(mouse_pos):
                if dice2.y == 10:
                    dice2.updatePosition(dice2.x, 300)
                else:
                    dice2.updatePosition(dice2.x, 10)"""

         # --- Game logic should go here
 
        # -- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(backgroundColor)

        # Copy image to screen:
        for i in dicesPlacementBlockList:
            i.draw();
          
        pygame.draw.rect(screen, RED, btnRollDice) # draw objects down here


        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

# Close the window and quit.
pygame.quit()
            
