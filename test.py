# Name: Brian Truong
# Date: 9/25/2017
# File Name: CPSC386Project2Yahtze.py
# File Description: py file that contains the necessary code to play a game of Yahtzee

import time
import random
import pygame

from Player import Player
from Rules import Rules

# Function: mainScreen
# Date of code (Last updated): 9/28
# Programmer: Andy Nguyen
# Description: Prints the game screen
#
# Input: N/A
# Output: N/A
def mainScreen():
    init()
    display.set_caption('Yahtzee')
    display.set_icon(image.load('icon.png'))
    screen_width = 1024
    screen_height = 768
    screen = display.set_mode([screen_width, screen_height])
    screenColor = (0, 170, 0)
    screen.fill(screenColor)
    display.flip()

    return screen


# Function: playerAvatars
# Date of code (Last updated): 9/28
# Programmer: Andy Nguyen
# Description: Representation of the player(s) or computer
#
# Input: Main game screen
# Output: Two circles representing the player(s) or computer

def playerAvatars(screen):
    # May change definition to accept (screen,color) to change color & indicate turns
    P1color = (0, 119, 255)  # blue
    P2color = (255, 0, 25)  # red
    avatarP1 = draw.circle(screen, P1color, (500, 650), 50)
    avatarP2 = draw.circle(screen, P2color, (500, 80), 50)
    display.update()


# Function: displayRollingDice
# Date of code (Last updated): 9/29
# Programmer: Andy Nguyen
# Description: Prints images of dice not kept by player(s) or computer
#
# Input: Takes in an array and its iteration
# Output: Outputs dice images in selected coordinates
def displayRollingDice(array, iteration):
    if array == 1:
        diceNumber = dice1
    elif array == 2:
        diceNumber = dice2
    elif array == 3:
        diceNumber = dice3
    elif array == 4:
        diceNumber = dice4
    elif array == 5:
        diceNumber = dice5
    elif array == 6:
        diceNumber = dice6

    # displays dices in selected coordinates
    if iteration == 0:
        display.get_surface().blit(diceNumber, (125, 300))
    if iteration == 1:
        display.get_surface().blit(diceNumber, (280, 300))
    if iteration == 2:
        display.get_surface().blit(diceNumber, (435, 300))
    if iteration == 3:
        display.get_surface().blit(diceNumber, (590, 300))
    if iteration == 4:
        display.get_surface().blit(diceNumber, (745, 300))

    display.update()


# Function: displayKeptDice
# Date of code (Last updated): 9/29
# Programmer: Andy Nguyen
# Description: Moves player kept dice down
#
# Input: Takes in an array and its iteration
# Output: Outputs dice images in selected coordinates

def displayKeptDice(array, iteration):
    eraseColor = (0, 170, 0)
    eraseSize = 150
    moveDicePosition = 100

    if array == 1:
        diceNumber = dice1
    elif array == 2:
        diceNumber = dice2
    elif array == 3:
        diceNumber = dice3
    elif array == 4:
        diceNumber = dice4
    elif array == 5:
        diceNumber = dice5
    elif array == 6:
        diceNumber = dice6

    # Erases previous dice image with a color square and draws new
    if iteration == 0:
        draw.rect(display.get_surface(), eraseColor, (125, 300, eraseSize, eraseSize))
        display.get_surface().blit(diceNumber, (125, 300 + moveDicePosition))
    if iteration == 1:
        draw.rect(display.get_surface(), eraseColor, (280, 300, eraseSize, eraseSize))
        display.get_surface().blit(diceNumber, (280, 300 + moveDicePosition))
    if iteration == 2:
        draw.rect(display.get_surface(), eraseColor, (435, 300, eraseSize, eraseSize))
        display.get_surface().blit(diceNumber, (435, 300 + moveDicePosition))
    if iteration == 3:
        draw.rect(display.get_surface(), eraseColor, (590, 300, eraseSize, eraseSize))
        display.get_surface().blit(diceNumber, (590, 300 + moveDicePosition))
    if iteration == 4:
        draw.rect(display.get_surface(), eraseColor, (745, 300, eraseSize, eraseSize))
        display.get_surface().blit(diceNumber, (745, 300 + moveDicePosition))

    display.update()


# Function: load_sound
# Date of code (Last updated): 9/28
# Programmer: Andy Nguyen
# Description: Representation of the player(s) or computer
#
# Input: A string of the sound file name
# Output: Loads the sound file into a variable
def load_sound(soundfile):
    # These are the available sounds
    # roll_sound = lay_sound('roll.wav')
    # reroll_sound = play_sound('reroll.wav')

    sound = mixer.Sound(soundfile)
    return sound



# initializes assets
clock = pygame.time.Clock()
currentScreen = mainScreen()
playerAvatars(currentScreen)
dice1 = image.load("dice1.png").convert()
dice2 = image.load("dice2.png").convert()
dice3 = image.load("dice3.png").convert()
dice4 = image.load("dice4.png").convert()
dice5 = image.load("dice5.png").convert()
dice6 = image.load("dice6.png").convert()
roll_sound = load_sound('roll.wav')
display.update()  # random display update to hopefully fix a bug

p1 = player
gameRules = Rules
time.delay(20)
# I am assuming the main issue with the image bugs is because screen focus.
# The input() command is causing major lag. Delay should give you a few more seconds before it breaks the program

while (p1.numberOfRolls < 3 and p1.rollingDices != [0, 0, 0, 0, 0, 0]):
    p1.rollDices(p1.rollingDices)
    p1.keepDices(p1.rollingDices, p1.keptDice)
    display.flip()
    clock.tick(60)

print("These are the final dice: ", p1.keptDice)  # used to check images
p1.keptDice.sort()
# p1.printDices(p1.keptDice, "Kept Dice")
gameRules.runUpperSection(p1.keptDice)
gameRules.runLowerSection(p1.keptDice)

time.delay(5)  # Pause to check if last dice correct
quit()

# Resources:
# https://en.wikipedia.org/wiki/Yahtzee#Rules
# http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
# https://wiki.python.org/moin/HowTo/Sorting
