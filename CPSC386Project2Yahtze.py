#Name: Brian Truong
#Date: 9/25/10`7
#File Name: CPSC386Project2Yahtze.py
#File Description: py file that contains the necessary code to play a game of Yahtzee
from pygame import *
from random import *


class player:
    #variables
    numberOfRolls = 0
    score = 0
    rollingDices = [1, 2, 3, 4, 5, 6]
    keptDice = [0, 0, 0, 0, 0, 0]
   
    def rollDices(dices):
        for x in range(len(dices)):
            if (dices[x] != 0):
                dices[x] = randint(1,6)
        player.numberOfRolls += 1
        print("Roll number:" + str(player.numberOfRolls))

    def printDices(dice, string):
        print(string)
        for x in range(len(dice)):
            if (dice[x] != 0):
                print("Dice", x+1, ":",dice[x])

    def keepDices(rolledDices, keptDice):
        decision = str
        player.printDices(rolledDices, "Rolled dices")
        for x in range(len(rolledDices)):
            if (rolledDices[x] != 0 and keptDice[x] == 0):
                decision = input("Press Y/N to keep Dice" + str(x + 1) + ":")
                if(decision.upper() == "Y"):
                    keptDice[x] = rolledDices[x]
                    rolledDices[x] = 0
    
    





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

    def runUpperSection(dice):
        player.printDices(dice, "Kept dice")
        Rules.isAces(dice)
        Rules.isTwos(dice)
        Rules.isThrees(dice)
        Rules.isFours(dice)
        Rules.isFives(dice)
        Rules.isSixes(dice)

    def isAces(dice):
        sum = 0
        for x in range(len(dice)):
            if (dice[x] == 1):
                sum += 1
        if (sum > 0):
                print("You have Aces! Sum: ", sum)

    def isTwos(dice):
        sum = 0
        for x in range(len(dice)):
            if (dice[x] == 2):
                sum += 2
        if (sum > 0):
                print("You have Twos! Sum: ", sum)

    def isThrees(dice):
        sum = 0
        for x in range(len(dice)):
            if (dice[x] == 3):
                sum += 3
        if (sum > 0):
                print("You have Threes! Sum: ", sum)

    def isFours(dice):
        sum = 0
        for x in range(len(dice)):
            if (dice[x] == 4):
                sum += 4
        if (sum > 0):
                print("You have Fours! Sum: ", sum)

    def isFives(dice):
        sum = 0
        for x in range(len(dice)):
            if (dice[x] == 5):
                sum += 5
        if (sum > 0):
                print("You have Fives! Sum: ", sum)

    def isSixes(dice):
        sum = 0
        for x in range(len(dice)):
            if (dice[x] == 6):
                sum += 6
        if (sum > 0):
                print("You have Sixes! Sum: ", sum)
    
    #Fix, not sorting
    def isThreeOfAKind(dice):
        sum = 0
        dice.sort()
        list = [0, 0, 0]
        for x in range(len(dice)):
            while(dice[x+1] != None or dice[x+2] != None):
                if (dice[x+1] == dice[x] + 1 and dice[x+2] == dice[x] +2):
                    dice[x] = list[x]
                    dice[x+1] = list[x+1]
                    dice[x+2] = list[x+2]
                    sum = dice[x] + dice[x+1] + dice[x+2]
                    Rules.threeOfAKind = True
        if (sum > 0):
                print("You have Three of a Kind! Sum: ", sum)



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
