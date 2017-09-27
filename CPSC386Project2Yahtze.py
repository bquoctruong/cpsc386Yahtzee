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
    rollingDices = [1, 2, 3, 4, 5, 6]
    keptDice = [0, 0, 0, 0, 0, 0]
   
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
    threeOfAKind = False
    fourOfAKind = False
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
        player.printDices(dice, "Kept dice")
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

    # Function: isAces
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

    # Function: isAces
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

    # Function: isAces
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
    # Date of code (Last updated): 9/27/2017
    # Programmer: Brian Truong
    # Description: To determine if the player rolled a three-of-a-kind
    # Input: list(dice)
    # Output: Boolean threeOfAKind
    #9/27 NOTE: Functions okay; not consistent
    def isThreeOfAKind(dice):
        sum = 0
        print("Begin sorting")
        dice.sort()
        list = [0, 0, 0, 0, 0, 0]
        print("Finish sorting")
        player.printDices(dice, "Sorted dice")

        #detects dice number and assigns them a slot in list
        #does not store duplicates
        print("Checking dices")
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
        
        print("detecting three of a kind")
        #detects three of a kind, going by possible triplet
        if (list[3] == 4 and list[4] == 5 and list[5] == 6):
            sum = list[3] + list[4] + list[5]
            print("You have Three of a Kind! Sum: ", sum)
            threeOfAKind = True
            return threeOfAKind
        elif(list[2] == 3 and list[3] == 4 and list[4] == 5):
            sum = list[2] + list[3] + list[4]
            print("You have Three of a Kind! Sum: ", sum)
            threeOfAKind = True
            return threeOfAKind
        elif(list[1] == 2 and list[2] == 3 and list[3] == 4):
            sum = list[1] + list[2] + list[3]
            print("You have Three of a Kind! Sum: ", sum)
            threeOfAKind = True
            return threeOfAKind
        elif(list[0] == 1 and list[1] == 2 and list[2] == 2):
            sum = list[0] + list[1] + list[2]
            print("You have Three of a Kind! Sum: ", sum)
            threeOfAKind = True
            return threeOfAKind



p1 = player
gameRules = Rules
while (p1.numberOfRolls < 3 and p1.rollingDices != [0, 0, 0, 0, 0, 0]):
    p1.rollDices(p1.rollingDices)
    p1.keepDices(p1.rollingDices, p1.keptDice)

gameRules.runUpperSection(p1.keptDice)

gameRules.isThreeOfAKind(p1.keptDice)




#Resources:
#https://en.wikipedia.org/wiki/Yahtzee#Rules
#http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
#https://wiki.python.org/moin/HowTo/Sorting
