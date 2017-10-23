
from time import *
from random import *
from pygame import *
import pygame

from Rules import Rules
from Player import Player

from BlockBase import BlockBase
from Scene import Scene

from BlockImage import BlockImage
from BlockRectangle import BlockRectangle
from BlockRectangleText import BlockRectangleText
from BlockScoreboard import BlockScoreboard

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0,255)
KINDA_GREEN = (0, 170, 0)
    
def updateDisplay(sceneItem, playerItem, doInitTurnItem):
    
    sceneItem.clearWithPattern("di-")

    updateDieDisplays(sceneItem, playerItem.rolledDices, "di-0-", 1, 0, doInitTurnItem)
    updateDieDisplays(sceneItem, playerItem.keptDices, "di-1-", 3, 1, doInitTurnItem)

    updateCategoryButtons(sceneItem, playerItem)

def updateDieDisplays(sceneItem, dices, prefix, y, relPos, doInitTurnItem):

    for i in range(0, len(dices)):

        val = dices[i]
        if doInitTurnItem and val<0:
            val = 1

        diceGap = 4    
        if val > 0:
            name = prefix + diceNameList[i]
            imageFile = valueMap[val]
            x = 1+i*diceGap
            b = BlockImage(name, imageFile, sceneItem, x, y)
            b.item = (relPos, i, val)
            sceneItem.addItem(b)

def initTurn(valueMap, diceNameList, defaultDieValue, sceneItem, playerItem, playerLabelItem, oldPlayerItem, statusLabelItem):

    oldPlayerItem.initializeTurn()
    
    sceneItem.clearWithPattern("di-")
    
    x = 1
    y = 1
    xInterval = 4
    imageFile = valueMap[defaultDieValue]
    prefix = "di-0-"
    for i in range(0, len(diceNameList)):
        name = prefix + diceNameList[i]
        b = BlockImage(name, imageFile, sceneItem, x, y)
        b.item = (0, i, defaultDieValue)
        sceneItem.addItem(b)
        x += xInterval

    playerLabelItem.setText(playerItem.name)
    statusLabelItem.setText("")
    
    updateCategoryButtons(sceneItem, playerItem)

def updateCategoryButtons(sceneItem, playerItem):
    
    sceneItem.clearWithPattern("cat-")
    
    x = 19
    y = 11.23
    yInterval = .54
    width = 50
    height = 13
    lowerGap = 3.12
    for i in range(0, playerItem.categoryCount()):

        categoryItem = playerItem.selectCategory(i+1)
        if categoryItem[0]:
            color = RED
        else:
            color = BLUE
        name = "cat-"+str(i+1)
        fontSize = 10
        b = BlockRectangleText(name, sceneItem, x, y, width, height, color, name, fontSize)
        b.item = i+1
        sceneItem.addItem(b)
        y += yInterval

        if i==5:
            y += lowerGap*yInterval
    
pygame.init()
pygame.font.init()

screenWidth = 1024
screenHeight = 768

size = ([screenWidth, screenHeight])
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Yahtzee")
pygame.display.set_icon(pygame.image.load("icon.png"))

shake = pygame.mixer.Sound("shake.wav")
roll = pygame.mixer.Sound("roll.wav")

done = False

clock = pygame.time.Clock()

# Game logic initialization
backgroundColor = KINDA_GREEN

valueMap = ["", "dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"]
diceNameList = ["0", "1", "2", "3", "4"]
defaultDie = 1

s = Scene(screen, size[0], size[1], 30, 21, 3)
    
player1 = Player("Player1")
player2 = Player("Player2")

scoreboard = BlockScoreboard("scoreboard.png", "scoreboard.png", s, 21, 10, player1, player2)
btn = BlockImage("roll.png", "roll.png", s, 1, 15);

s.addItem(scoreboard)
s.addItem(btn)

player = player1
otherPlayer = player2

x = 23
y = 1
width = 100
height = 50
text = player.name
fontSize = 20
playerLabel = BlockRectangleText("playerLabel", s, x, y, width, height, WHITE, text, fontSize)
s.addItem(playerLabel)

x = 23
y = 3
width = 225
height = 50
text = ""
fontSize = 20
statusLabel = BlockRectangleText("statusLabel", s, x, y, width, height, BLUE, text, fontSize)
s.addItem(statusLabel)

initTurn(valueMap, diceNameList, defaultDie, s, player, playerLabel, otherPlayer, statusLabel)

allowRoll = True
while not done:
    mouse_pos = pygame.mouse.get_pos() # gets mouse position
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:

            itemName = s.getItemClicked(mouse_pos)

            doInitTurn = False
            category = 0
            if itemName == "roll.png" and allowRoll:
                roll.play()
                player.rollDices()

                #debug
                #player.rolledDices = [6, 6, 6, 2, 2]
 
                if player.numberOfRolls == 3:
                    allowRoll = False
                    statusLabel.setText("You must score this roll!")
                    
            elif itemName.startswith("cat-"):
                category = s.itemList[itemName].item
                doInitTurn = True                    
                
            elif itemName.startswith("di-"):
                parentItem = s.itemList[itemName]
                item = parentItem.item

                relPos = item[0]
                diex = item[1]
                val = item[2]
                rolledNewVal = None
                keptNewVal = None
                if relPos == 0:
                    relPos = 1
                    rolledNewVal = 0
                    keptNewVal = val
                    parentItem.y = 3
                else:
                    relPos = 0
                    rolledNewVal = val
                    keptNewVal = 0
                    parentItem.y = 1

                player.rolledDices[diex] = rolledNewVal
                player.keptDices[diex] = keptNewVal
                parentItem.item = (relPos, diex, val)    
                parentItem.updatePosition(parentItem.x, parentItem.y)

            if itemName != "":               
                r = Rules(player.keptDices)
                r.runSections()

                player.updateScore(r)

                if category > 0:
                    player.updateCategory(r, category)

                if doInitTurn:
                    if player == player1 and not otherPlayer.isDone():
                        player = player2
                        otherPlayer = player1
                    else:
                        player = player1
                        otherPlayer = player2

                    initTurn(valueMap, diceNameList, defaultDie, s, player, playerLabel, otherPlayer, statusLabel)
                    allowRoll = True
                    statusLabel
                   
                updateDisplay(s, player, doInitTurn)
                doInitTurn = False
                category = 0          

                if player.isDone() and otherPlayer.isDone():
                
                    winner = None
                    winnerMessage = ""
                    if (player.totalScore() > otherPlayer.totalScore()):
                        winner = player
                    else:
                        winner = otherPlayer
                        
                    winnerMessage = winner.name + " is the winner. Bye!"
                    statusLabel.setText(winnerMessage)
                    
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
            
