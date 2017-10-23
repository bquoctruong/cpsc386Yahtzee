# class: player
# Date of code (Last updated): 10/17/2017
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

    sumOfScore = 0

    #Determines if player is done playing
    isDone = False

    #Sets up player to be autonomous; player.isAI == isAI
    isAI = False

    #Booleans that note if player can add points under a category
    aceAvailable = False
    twosAvailable = False
    threesAvailable = False
    foursAvailable = False
    fivesAvailable = False
    sixesAvailable = False
    threeOfAKindAvailable = False
    fourOfAKindAvailable = False
    fullHouseAvailable = False
    smallStraightAvailable = False
    largeStraightAvailable = False
    yahtzeeAvailable = False
    chanceAvailable = False

    #prevents player and AI from picking same option more than once
    noAce = False
    noTwos = False
    noThrees = False
    noFours = False
    noFives = False
    noSixes = False
    noThreeOfAKind = False
    noFourOfAKind = False
    noFullHouse = False
    noSmallStraight = False
    noLargeStraight = False
    noYahtzee = False
    noChance = False


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
    # Date of code (Last updated): 10/17/2017
    # Programmer: Brian Truong
    # Description: Allows player to keep dices for the purpose of Yahtzee
    # Input: rolledDices, keptDice
    # Output: N/A
    def keepDices(rolledDices, keptDice):
        decision = str
        player.printDices(rolledDices, "Rolled dices")
        for x in range(len(rolledDices)):
            if (rolledDices[x] != 0 and keptDice[x] == 0 and player.isAI == False):
                decision = input("Press Y/N to keep Dice" + str(x + 1) + ":")
                if(decision.upper() == "Y"):
                    keptDice[x] = rolledDices[x]
                    rolledDices[x] = 0
            elif (rolledDices[x] != 0 and keptDice[x] == 0 and player.isAI == True):
                #If 0, does not keep dice; if 1, keeps dice
                robotDecision = randint(0, 1);
                if(robotDecision == 1):
                    keptDice[x] = rolledDices[x]
                    rolledDices[x] = 0

    # Function: keepScore
    # Date of code (Last updated): 10/17/2017
    # Programmer: Brian Truong
    # Description: Allows player to keep one available choice; makes AI pick best possible choice from list
    # Input:
    # Output: 
    def keepScore():
        decision = str
        if (player.yahtzeeAvailable == True and player.noYahtzee == False and player.isAI == False):
            decision = input("Keep Yahtzee (Y/N)?")
            if(decision.upper() == "Y"):
                player.noYahtzee = True
            elif(decision.upper() == "N"):
                player.yahtzeeAvailable = False
                player.yahtzeeScore = 0
        #Automatically makes AI take best possible choice
        elif(player.yahtzeeAvailable == True and player.noYahtzee == False and player.isAI == True):
           player.noYahtzee = True
        elif (player.largeStraightAvailable == True and player.noLargeStraight == False and player.isAI == False):
            decision = input("Keep Large Straight (Y/N)?")
            if(decision.upper() == "Y"):
                player.noLargeStraight = True
            elif(decision.upper() == "N"):
                player.largeStraightAvailable = False
                player.largeStraightScore = 0
        #Automatically makes AI take best possible choice
        elif(player.largeStraightAvailable == True and player.noLargeStraight == False and player.isAI == True):
           player.noLargeStraight = True
        elif (player.smallStraightAvailable == True and player.noSmallStraight == False and player.isAI == False):
            decision = input("Keep Small Straight (Y/N)?")
            if(decision.upper() == "Y"):
                player.noSmallStraight = True
            elif(decision.upper() == "N"):
                player.smallStraightAvailable = False
                player.smallStraightScore = 0
        #Automatically makes AI take best possible choice
        elif(player.smallStraightAvailable == True and player.noSmallStraight == False and player.isAI == True):
           player.noSmallStraight = True
        elif (player.fullHouseAvailable == True and player.noFullHouse == False and player.isAI == False):
            decision = input("Keep Large Straight (Y/N)?")
            if(decision.upper() == "Y"):
                player.noFullHouse = True
            elif(decision.upper() == "N"):
                player.fullHouseAvailable = False
                player.fullHouseScore = 0
        #Automatically makes AI take best possible choice
        elif(player.fullHouseAvailable == True and player.noFullHouse == False and player.isAI == True):
           player.noFullHouse = True
        elif (player.fourOfAKindAvailable == True and player.noFourOfAKind == False and player.isAI == False):
            decision = input("Keep Four of a Kind (Y/N)?")
            if(decision.upper() == "Y"):
                player.noFourOfAKind = True
            elif(decision.upper() == "N"):
                player.fourOfAKindAvailable = False
                player.fourOfAKindScore = 0
        #Automatically makes AI take best possible choice
        elif(player.fourOfAKindAvailable == True and player.noFourOfAKind == False and player.isAI == True):
           player.noFourOfAKind = True
        elif (player.threeOfAKindAvailable == True and player.noThreeOfAKind == False and player.isAI == False):
            decision = input("Keep Three of a Kind (Y/N)?")
            if(decision.upper() == "Y"):
                player.noThreeOfAKind = True
            elif(decision.upper() == "N"):
                player.threeOfAKindAvailable = False
                player.threeOfAKindScore = 0
        #Automatically makes AI take best possible choice
        elif(player.threeOfAKindAvailable == True and player.noThreeOfAKind == False and player.isAI == True):
           player.noThreeOfAKind = True
        elif (player.sixesAvailable == True and player.noSixes == False and player.isAI == False):
            decision = input("Keep Sixes (Y/N)?")
            if(decision.upper() == "Y"):
                player.noSixes = True
            elif(decision.upper() == "N"):
                player.sixesAvailable = False
                player.sixesScore = 0
        #Automatically makes AI take best possible choice
        elif(player.sixesAvailable == True and player.noSixes == False and player.isAI == True):
           player.noSixes = True
        elif (player.fivesAvailable == True and player.noFives == False and player.isAI == False):
            decision = input("Keep Fives (Y/N)?")
            if(decision.upper() == "Y"):
                player.noFives = True
            elif(decision.upper() == "N"):
                player.fivesAvailable = False
                player.fivesScore = 0
        #Automatically makes AI take best possible choice
        elif(player.fivesAvailable == True and player.noFives == False and player.isAI == True):
           player.noFives = True
        elif (player.foursAvailable == True and player.noFours == False and player.isAI == False):
            decision = input("Keep Fours (Y/N)?")
            if(decision.upper() == "Y"):
                player.noFours = True
            elif(decision.upper() == "N"):
                player.foursAvailable = False
                player.foursScore = 0
        #Automatically makes AI take best possible choice
        elif(player.foursAvailable == True and player.noFours == False and player.isAI == True):
           player.noFours = True
        elif (player.threesAvailable == True and player.noThrees == False and player.isAI == False):
            decision = input("Keep Threes (Y/N)?")
            if(decision.upper() == "Y"):
                player.noThrees = True
            elif(decision.upper() == "N"):
                player.threesAvailable = False
                player.threesScore = 0
        #Automatically makes AI take best possible choice
        elif(player.threesAvailable == True and player.noThrees == False and player.isAI == True):
           player.noThrees = True
        elif (player.twosAvailable == True and player.noTwos == False and player.isAI == False):
            decision = input("Keep Twos (Y/N)?")
            if(decision.upper() == "Y"):
                player.noTwos = True
            elif(decision.upper() == "N"):
                player.twosAvailable = False
                player.twosScore = 0
        #Automatically makes AI take best possible choice
        elif(player.twosAvailable == True and player.noTwos == False and player.isAI == True):
           player.noTwos = True
        elif (player.aceAvailable == True and player.noAce == False and player.isAI == False):
            decision = input("Keep Ace (Y/N)?")
            if(decision.upper() == "Y"):
                player.noAce = True
            elif(decision.upper() == "N"):
                player.aceAvailable = False
                player.acesScore = 0
        #Automatically makes AI take best possible choice
        elif(player.aceAvailable == True and player.noAce == False and player.isAI == True):
           player.noAce = True
        elif (player.chanceAvailable == True and player.noChance == False and player.isAI == False):
            decision = input("Keep Chance (Y/N)?")
            if(decision.upper() == "Y"):
                player.noChance = True
            elif(decision.upper() == "N"):
                player.chanceAvailable = False
                player.chanceScore = 0
        #Automatically makes AI take best possible choice
        elif(player.chanceAvailable == True and player.noChance == False and player.isAI == True):
           player.noChance = True

    # Function: isDone
    # Date of code (Last updated): 10/17/2017
    # Programmer: Brian Truong
    # Description: Determines whether or not the player is done playing
    # Input: N/A
    # Output: N/A
    def setDone():
        if (player.noAce == True and player.noTwos == True and player.noThrees == True and player.noFours == True and player.noFives == True and player.noSixes == True
            and player.noThreeOfAKind == True and player.noFourOfAKind == True and player.noSmallStraight == True and player.noLargeStraight == True and player.noFullHouse == True
            and player.yahtzeeAvailable == True and player.noChance == True):
            isDone = True

    def sum():
        player.sum = (player.acesScore + player.twosScore + player.threesScore + player.foursScore + player.fivesScore + player.sixesScore + 
        player.threeOfAKindScore + player.fourOfAKindScore + player.smallStraightScore +player.largeStraightScore +player.fullHouseScore + 
        player.yahtzeeScore + player.chanceScore)



