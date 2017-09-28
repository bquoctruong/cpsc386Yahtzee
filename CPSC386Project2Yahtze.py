#Name: Brian Truong
#Date: 9/25/10`7
#File Name: CPSC386Project2Yahtze.py
#File Description: py file that contains the necessary code to play a game of Yahtzee
from pygame import *
from random import *

# class: player
# Date of code (Last updated): 9/26
# Programmer: Brian Truong
# Description: class that tracks dices rolled, kept, and other such variables
#               for the player when playing Yahtzee
# Input: N/A
# Output: N/A
class player:
    #variables
    numberOfRolls = 0
    score = 0
    rollingDices = [1, 2, 3, 4, 5]
    keptDice = [0, 0, 0, 0, 0]

    acesScore = 0
    twosScore = 0
    threesScore = 0
    foursScore = 0
    fivesScore = 0
    sixesScore = 0
    threeOfAKindScore = 0
    fourOfAKindScore = 0
    fullHouseScore = 0
    smallStraightScore = 0
    largeStraightScore = 0
    yahtzeeScore = 0
    chanceScore = 0
   
    # Function: rollDices
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: uses randint to "roll" available dices
    # Input: list(dices)
    # Output: N/A
    def rollDices(dices):
        for x in range(len(dices)):
            if (dices[x] != 0):
                dices[x] = randint(1,6)
        player.numberOfRolls += 1
        print("Roll number:" + str(player.numberOfRolls))

    # Function:printDices
    # Date of code (Last updated): 9/25
    # Programmer: Brian Truong
    # Description: prints chosen dices' values
    # Input: list(dice), String
    # Output: N/A
    def printDices(dice, string):
        print(string)
        for x in range(len(dice)):
            if (dice[x] != 0):
                print("Dice", x+1, ":",dice[x])

    # Function: keepDices
    # Date of code (Last updated): 9/26/2017
    # Programmer: Brian Truong
    # Description: Allows player to keep dices for the purpose of Yahtzee
    # Input: rolledDices, keptDice
    # Output: N/A
    def keepDices(rolledDices, keptDice):
        decision = str
        player.printDices(rolledDices, "Rolled dices")
        for x in range(len(rolledDices)):
            if (rolledDices[x] != 0 and keptDice[x] == 0):
                decision = input("Press Y/N to keep Dice" + str(x + 1) + ":")
                if(decision.upper() == "Y"):
                    keptDice[x] = rolledDices[x]
                    rolledDices[x] = 0
    
# Class: Rules
# Date of code (Last updated): 9/27/2017
# Programmer: Brian Truong
# Description: Given player dices, determines what points may be given to the player
# Input: 
# Output: 
class Rules:
    aces = False
    twos = False
    threes = False
    fours = False
    fives = False
    six = False
    largeStraight = False
    smallStraight = False
    fullHouse = False
    smallStraight = False
    largeStraight = False
    yahtzee = False
    chance = False

    # Function: runUpperSection
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: runs the set of rules (as functions) belonging to the upper section of the game Yahtzee
    # Input: list(dice)
    # Output: 
    def runUpperSection(dice):
        Rules.isAces(dice)
        Rules.isTwos(dice)
        Rules.isThrees(dice)
        Rules.isFours(dice)
        Rules.isFives(dice)
        Rules.isSixes(dice)

    # Function: isAces
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: Given a set of dice, determines if the dices have aces and sums up all "aces"
    # Input: dice
    # Output: 
    def isAces(dice):
        sum = 0
        for x in range(len(dice)):
            if (dice[x] == 1):
                sum += 1
        if (sum > 0):
                print("You have Aces! Sum: ", sum)

    # Function: isTwos
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: Given a set of dice, determines if the dices have twos and sums up all "twos"
    # Input: dice
    # Output: 
    def isTwos(dice):
        sum = 0
        for x in range(len(dice)):
            if (dice[x] == 2):
                sum += 2
        if (sum > 0):
                print("You have Twos! Sum: ", sum)

    # Function: isThrees
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: Given a set of dice, determines if the dices have threes and sums up all "threes"
    # Input: dice
    # Output: 
    def isThrees(dice):
        sum = 0
        for x in range(len(dice)):
            if (dice[x] == 3):
                sum += 3
        if (sum > 0):
                print("You have Threes! Sum: ", sum)

    # Function: isFours
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: Given a set of dice, determines if the dices have fours and sums up all "fours"
    # Input: dice
    # Output: 
    def isFours(dice):
        sum = 0
        for x in range(len(dice)):
            if (dice[x] == 4):
                sum += 4
        if (sum > 0):
                print("You have Fours! Sum: ", sum)

    # Function: isFives
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: Given a set of dice, determines if the dices have fives and sums up all "fives"
    # Input: dice
    # Output: 
    def isFives(dice):
        sum = 0
        for x in range(len(dice)):
            if (dice[x] == 5):
                sum += 5
        if (sum > 0):
                print("You have Fives! Sum: ", sum)

    # Function: isSixes
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: Given a set of dice, determines if the dices have sixes and sums up all "sixes"
    # Input: dice
    # Output: 
    def isSixes(dice):
        sum = 0
        for x in range(len(dice)):
            if (dice[x] == 6):
                sum += 6
        if (sum > 0):
                print("You have Sixes! Sum: ", sum)
    
    # Function: isThreeOfAKind
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: Checks if player has Three of a Kind
    # Input: list(dice)
    # Output: Boolean threeOfAKind
    def isThreeOfAKind(dice):
        sum = 0
        if (dice[2] == dice[3] == dice[4]):
            sum = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
            print("You have Three of a Kind! Sum: ", sum)
            threeOfAKind = True
            return threeOfAKind
        elif(dice[1] == dice[2] == dice[3]):
            sum = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
            print("You have Three of a Kind! Sum: ", sum)
            threeOfAKind = True
            return threeOfAKind
        elif(dice[0] == dice[1] == dice[2]):
            sum = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
            print("You have Three of a Kind! Sum: ", sum)
            threeOfAKind = True
            return threeOfAKind

    # Function: isFourOfAKind
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: Checks if player has Four of a Kind
    # Input: list(dice)
    # Output: Boolean fourOfAKind
    def isFourOfAKind(dice):
        sum = 0
        if (dice[1]== dice[2] == dice[3] == dice[4]):
            sum = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
            print("You have Four of a Kind! Sum: ", sum)
            fourOfAKind = True
            return fourOfAKind
        elif(dice[0] == dice[1] == dice[2] == dice[3]):
            sum = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
            print("You have Four of a Kind! Sum: ", sum)
            fourOfAKind = True
            return fourOfAKind
        
    # Function: isFullHouse
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: checks if the player kept a Full House
    # Input: dice
    # Output: Boolean fullHouse
    def isFullHouse(dice):
        sum = 0
        dice.sort()
        if (dice[0] == dice[1] and dice[2] == dice[3] == dice[4]):
            sum = 25
            print("You have a Full House! Sum: ", sum)
            fullHouse = True
            return fullHouse
        elif(dice[0] == dice[1] == dice[2] and dice[3] == dice[4]):
            sum = 25
            print("You have a Full House! Sum: ", sum)
            fullHouse = True
            return fullHouse

    # Function: isSmallStraight
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: Detects if the kept dice have a Small Straight
    # Input: list(dice)
    # Output: Boolean smallStraight
    def isSmallStraight(dice):
        sum = 0
        #print("Begin sorting")
        list = [0, 0, 0, 0, 0, 0]

        #detects dice number and assigns them a slot in list
        #does not store duplicates
        #print("Checking dices")
        for x in range(len(dice)):
            if (dice[x] == 1):
                list[0] = 1;
            if (dice[x] == 2):
                list[1] = 2;
            if (dice[x] == 3):
                list[2] = 3;
            if (dice[x] == 4):
                list[3] = 4;
            if (dice[x] == 5):
                list[4] = 5;
            if (dice[x] == 6):
                list[5] = 6;
        
        #print("detecting three of a kind")
        #print(list)
        #detects three of a kind, going by possible triplet
        if (list[2] == 3 and list[3] == 4 and list[4] == 5 and list[5] == 6):
            sum = 30
            print("You have a Small Straight! Sum: ", sum)
            smallStraight = True
            return smallStraight
        elif(list[1] == 2 and list[2] == 3 and list[3] == 4 and list[4] == 5):
            sum = 30
            print("You have a Small Straight! Sum: ", sum)
            smallStraight = True
            return smallStraight
        elif(list[0] == 1 and list[1] == 2 and list[2] == 3 and list[3] == 4):
            sum = 30
            print("You have a Small Straight! Sum: ", sum)
            smallStraight = True
            return smallStraight

    # Function: isLargeStraight
    # Date of code (Last updated): 9/27/2017
    # Programmer: Brian Truong
    # Description: To determine if the player rolled a Large Straight
    # Input: list(dice)
    # Output: Boolean largeStraight
    def isLargeStraight(dice):
        sum = 0
        #print("Begin sorting")
        list = [0, 0, 0, 0, 0, 0]

        #detects dice number and assigns them a slot in list
        #does not store duplicates
        #print("Checking dices")
        for x in range(len(dice)):
            if (dice[x] == 1):
                list[0] = 1;
            if (dice[x] == 2):
                list[1] = 2;
            if (dice[x] == 3):
                list[2] = 3;
            if (dice[x] == 4):
                list[3] = 4;
            if (dice[x] == 5):
                list[4] = 5;
            if (dice[x] == 6):
                list[5] = 6;
        
        #print("detecting three of a kind")
        #print(list)
        #detects three of a kind, going by possible triplet
        if (list[1] == 2 and list[2] == 3 and list[3] == 4 and list[4] == 5 and list[5] == 6):
            sum = 40
            print("You have a Large Straight! Sum: ", sum)
            largeStraight = True
            return largeStraight
        elif(list[0] == 1 and list[1] == 2 and list[2] == 3 and list[3] == 4 and list[4] == 5):
            sum = 40
            print("You have a Large Straight! Sum: ", sum)
            largeStraight = True
            return largeStraight

    # Function: isYahtzee
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: Checks if the player has Yahtzee
    # Input: dice
    # Output: Boolean yahtzee
    def isYahtzee(dice):
        sum = 0
        if (dice[0] == dice[1] == dice[2] == dice[3] == dice[4]):
            sum = 50
            print("You have Yahtzee! Sum: ", sum)
            yahtzee = True
            return yahtzee

    # Function: isChance
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: Checks if the player has Chance
    # Input: dice
    # Output: Boolean chance
    def isChance(dice):
        sum = 0
        sum = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
        print("You have Chance! Sum: ", sum)
        chance = True
        return chance

    # Function: runLowerSection
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: Runs all categories under the "Lower Section" rules of Yahtzee
    # Input: list(dice)
    # Output: N/A
    def runLowerSection(dice):
        dice.sort()
        Rules.isYahtzee(dice)
        Rules.isLargeStraight(dice)
        Rules.isSmallStraight(dice)
        Rules.isFullHouse(dice)
        Rules.isFourOfAKind(dice)
        Rules.isThreeOfAKind(dice)
        Rules.isChance(dice)


p1 = player
gameRules = Rules
while (p1.numberOfRolls < 3 and p1.rollingDices != [0, 0, 0, 0, 0, 0]):
    p1.rollDices(p1.rollingDices)
    p1.keepDices(p1.rollingDices, p1.keptDice)
p1.keptDice.sort()
p1.printDices(p1.keptDice, "Kept Dice")
gameRules.runUpperSection(p1.keptDice)
gameRules.runLowerSection(p1.keptDice)


#Resources:
#https://en.wikipedia.org/wiki/Yahtzee#Rules
#http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
#https://wiki.python.org/moin/HowTo/Sorting
