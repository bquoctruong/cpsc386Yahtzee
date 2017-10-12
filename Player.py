from random import *

# class: player
# Date of code (Last updated): 9/26
# Programmer: Brian Truong
# Description: class that tracks dices rolled, kept, and other such variables
#               for the player when playing Yahtzee
# Input: N/A
# Output: N/A
class Player:

    def __init__(self):
        # variables
        self.numberOfRolls = 0
        self.score = 0
        self.rolledDices = [-1, -1, -1, -1, -1]
        self.keptDices = [0, 0, 0, 0, 0]

        self.acesScore = 0
        self.twosScore = 0
        self.threesScore = 0
        self.foursScore = 0
        self.fivesScore = 0
        self.sixesScore = 0
        self.threeOfAKindScore = 0
        self.fourOfAKindScore = 0
        self.fullHouseScore = 0
        self.smallStraightScore = 0
        self.largeStraightScore = 0
        self.yahtzeeScore = 0
        self.chanceScore = 0

    # Function: rollDices
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: uses randint to "roll" available dices
    # Input: list(dices)
    # Output: N/A
    def rollDices(self):
        #refactor
        #roll_sound.play()
        for x in range(len(self.rolledDices)):
            if (self.rolledDices[x] != 0):
                self.rolledDices[x] = randint(1, 6)
        self.numberOfRolls += 1
        print("Roll number:" + str(self.numberOfRolls))

    # Function:printDices
    # Date of code (Last updated): 9/25
    # Programmer: Brian Truong
    # Description: prints chosen dices' values
    # Input: list(dice), String
    # Output: N/A
    def printDices(self, dices, message):
        print(message)
        for x in range(len(dices)):
            if (dices[x] != 0):
                print("Dice", x + 1, ":", dices[x])
                #refactor
                #displayRollingDice(dice[x], x)

    # Function: keepDices
    # Date of code (Last updated): 9/26/2017
    # Programmer: Brian Truong
    # Description: Allows player to keep dices for the purpose of Yahtzee
    # Input: rolledDices, keptDice
    # Output: N/A
    def keepDices(self, keepMask):
        self.printDices(self.rolledDices, "Rolled dices")
        for i in range(len(keepMask)):
            if keepMask[i] != 0:
                self.keptDices[i] = self.rolledDices[i]
                self.rolledDices[i] = 0
