from random import *
from Rules import Rules

# class: player
# Date of code (Last updated): 9/26
# Programmer: Brian Truong
# Description: class that tracks dices rolled, kept, and other such variables
#               for the player when playing Yahtzee
# Input: N/A
# Output: N/A
class Player:

    def __init__(self, name):

        self.name = name
        
        # variables
        self.acesScore = (False, 0)
        self.twosScore = (False, 0)
        self.threesScore = (False, 0)
        self.foursScore = (False, 0)
        self.fivesScore = (False, 0)
        self.sixesScore = (False, 0)
        self.threeOfAKindScore = (False, 0)
        self.fourOfAKindScore = (False, 0)
        self.fullHouseScore = (False, 0)
        self.smallStraightScore = (False, 0)
        self.largeStraightScore = (False, 0)
        self.yahtzeeScore = (False, 0)
        self.chanceScore = (False, 0)

        #Warning: should not call methods in constructor
        #due to variable lifecycle and ordering of calls
        self.initializeTurn()
        
    def initializeTurn(self):
        
        self.numberOfRolls = 0
        self.rolledDices = [-1, -1, -1, -1, -1]
        self.keptDices = [0, 0, 0, 0, 0]
        self.cleanScore()

    def cleanScore(self):

        resetValue = (False, 0)
        
        if not self.acesScore[0]:
            self.acesScore = resetValue
        if not self.twosScore[0]:
            self.twosScore = resetValue
        if not self.threesScore[0]:
            self.threesScore = resetValue
        if not self.foursScore[0]:
            self.foursScore = resetValue    
        if not self.fivesScore[0]:
            self.fivesScore = resetValue    
        if not self.sixesScore[0]:
            self.sixesScore = resetValue
            
        if not self.threeOfAKindScore[0]:
            self.threeOfAKindScore = resetValue
        if not self.fourOfAKindScore[0]:
            self.fourOfAKindScore = resetValue
        if not self.fullHouseScore[0]:
            self.fullHouseScore = resetValue
        if not self.smallStraightScore[0]:
            self.smallStraightScore = resetValue
        if not self.largeStraightScore[0]:
            self.largeStraightScore = resetValue
        if not self.yahtzeeScore[0]:
            self.yahtzeeScore = resetValue
        if not self.chanceScore[0]:
            self.chanceScore = resetValue
            
    def categoryCount(self):
        return 13
    
    def selectCategory(self, index):

        item = None
        
        if index == 1:
            item = self.acesScore
        elif index == 2:
            item = self.twosScore
        elif index == 3:
            item = self.threesScore
        elif index == 4:
            item = self.foursScore
        elif index == 5:
            item = self.fivesScore
        elif index == 6:
            item = self.sixesScore

        elif index == 7:
            item = self.threeOfAKindScore
        elif index == 8:
            item = self.fourOfAKindScore
        elif index == 9:
            item = self.fullHouseScore
        elif index == 10:
            item = self.smallStraightScore
        elif index == 11:
            item = self.largeStraightScore
        elif index == 12:
            item = self.yahtzeeScore
        elif index == 13:
            item = self.chanceScore
            
        return item

    def isDone(self):

        isDoneItem = True
        
        for i in range(0, self.categoryCount()):
            if not self.selectCategory(i+1)[0]:
                isDoneItem = False
                break

        return isDoneItem
            
    
    def updateCategory(self, ruleItem, index):

        ruleCategoryValue = ruleItem.selectCategory(index)[1]
        categoryValue = (True, ruleCategoryValue)
        
        if index == 1:
            self.acesScore = categoryValue
        elif index == 2:
            self.twosScore = categoryValue
        elif index == 3:
            self.threesScore = categoryValue
        elif index == 4:
            self.foursScore = categoryValue
        elif index == 5:
            self.fivesScore = categoryValue
        elif index == 6:
            self.sixesScore = categoryValue

        elif index == 7:
            self.threeOfAKindScore = categoryValue
        elif index == 8:
            self.fourOfAKindScore = categoryValue
        elif index == 9:
            self.fullHouseScore = categoryValue
        elif index == 10:
            self.smallStraightScore = categoryValue
        elif index == 11:
            self.largeStraightScore = categoryValue
        elif index == 12:
            self.yahtzeeScore = categoryValue
        elif index == 13:
            self.chanceScore = categoryValue
       
    def updateScore(self, ruleItem):
        
        if ruleItem.aces[0]:
            self.acesScore = (self.acesScore[0] , ruleItem.aces[1])
        if ruleItem.twos[0]:
            self.twosScore = (self.twosScore[0] , ruleItem.twos[1])
        if ruleItem.threes[0]:
            self.threesScore = (self.threesScore[0] , ruleItem.threes[1])
        if ruleItem.fours[0]:
            self.foursScore = (self.foursScore[0] , ruleItem.fours[1])
        if ruleItem.fives[0]:
            self.fivesScore = (self.fivesScore[0] , ruleItem.fives[1])
        if ruleItem.sixes[0]:
            self.sixesScore = (self.sixesScore[0] , ruleItem.sixes[1])
            
        if ruleItem.threeOfAKind[0]:
            self.threeOfAKindScore = (self.threeOfAKindScore[0] , ruleItem.threeOfAKind[1])
        if ruleItem.fourOfAKind[0]:
            self.fourOfAKindScore = (self.fourOfAKindScore[0] , ruleItem.fourOfAKind[1])
        if ruleItem.fullHouse[0]:
            self.fullHouseScore = (self.fullHouseScore[0] , ruleItem.fullHouse[1])
        if ruleItem.smallStraight[0]:
            self.smallStraightScore = (self.smallStraightScore[0] , ruleItem.smallStraight[1])
        if ruleItem.largeStraight[0]:
            self.largeStraightScore = (self.largeStraightScore[0] , ruleItem.largeStraight[1])
        if ruleItem.yahtzee[0]:
            self.yahtzeeScore = (self.yahtzeeScore[0] , ruleItem.yahtzee[1])
        if ruleItem.chance[0]:
            self.chanceScore = (self.chanceScore[0] , ruleItem.chance[1])

    def totalUpper(self):
        
        sum = 0

        if self.acesScore[0]:
            sum += self.acesScore[1]
        if self.twosScore[0]:
            sum += self.twosScore[1]
        if self.threesScore[0]:
            sum += self.threesScore[1]
        if self.foursScore[0]:
            sum += self.foursScore[1]
        if self.fivesScore[0]:
            sum += self.fivesScore[1]
        if self.sixesScore[0]:
            sum += self.sixesScore[1]
        
        return sum

    def totalScore(self):
        
        sum = self.totalUpper()

        if self.threeOfAKindScore[0]:
            sum += self.threeOfAKindScore[1]
        if self.fourOfAKindScore[0]:
            sum += self.fourOfAKindScore[1]
        if self.fullHouseScore[0]:
            sum += self.fullHouseScore[1]
        if self.smallStraightScore[0]:
            sum += self.smallStraightScore[1]
        if self.largeStraightScore[0]:
            sum += self.largeStraightScore[1]
        if self.yahtzeeScore[0]:
            sum += self.yahtzeeScore[1]
        if self.chanceScore[0]:
            sum += self.chanceScore[1]        
        return sum
    
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
