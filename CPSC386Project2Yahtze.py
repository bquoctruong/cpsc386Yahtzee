from pygame import *
from random import *


class player1:
    rolledDices = [randint(1,6), randint(1,6), randint(1,6), 
             randint(1,6), randint(1,6), randint(1,6)]

    keptDice = [0, 0, 0, 0, 0, 0]

    def rollDices(rolledDices):
        for x in range(len(rolledDices)):
            if (rolledDices[x] != 0):
                rolledDices[x] = randint(1,6)

    def keepDices(rolledDices, keptDice):
        decision = str
        printDices(rolledDices)
        for x in range(len(rolledDices)):
            if (rolledDices[x] != 0 and keptDice[x] == 0):
                decision = input("Press Y/N to keep Dice" + str(x + 1) + ":")
                if(decision.upper() == "Y"):
                    keptDice[x] = rolledDices[x]
                    rolledDices[x] = 0





def printDices(dice):
    for x in range(len(dice)):
        print("Dice", x+1, ":",dice[x])

def runUpperSection(dices):
    isAces(dices)
    isTwos(dices)
    isThrees(dices)
    isFours(dices)
    isFives(dices)
    isSixes(dices)

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
        if (dice[x] == 1):
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

p1 = player1
printDices(p1.rolledDices)
p1.keepDices(p1.rolledDices, p1.keptDice)
printDices(p1.rolledDices)
printDices(p1.keptDice)
runUpperSection(p1.keptDice)


#Resources:
#https://en.wikipedia.org/wiki/Yahtzee#Rules
#http://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/