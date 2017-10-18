# Class: Rules
# Date of code (Last updated): 10/6/2017
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
    sixes = False
    threeOfAKind = False
    fourOfAKind = False
    largeStraight = False
    smallStraight = False
    fullHouse = False
    smallStraight = False
    largeStraight = False
    yahtzee = False
    chance = False
    isAI = False

    acesSum = 0
    twosSum = 0
    threesSum = 0
    foursSum = 0
    fivesSum = 0
    sixesSum = 0
    threeOfAKindSum = 0
    fourOfAKindSum = 0
    fullHouseSum = 0
    smallStraightSum = 0
    largeStraightSum = 0
    yahtzeeSum = 0
    chanceSum = 0

    

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
    # Date of code (Last updated): 10/6/2017
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
                Rules.aces = True
                Rules.acesSum = sum
                print("You have Aces! Sum: ", sum)

    # Function: isTwos
    # Date of code (Last updated): 10/6/2017
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
                Rules.twos = True
                Rules.twosSum = sum
                print("You have Twos! Sum: ", sum)

    # Function: isThrees
    # Date of code (Last updated): 10/6/2017
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
                Rules.threes = True
                Rules.threesSum = sum
                print("You have Threes! Sum: ", sum)

    # Function: isFours
    # Date of code (Last updated): 10/6/2017
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
            Rules.fours = True
            Rules.foursSum = sum
            print("You have Fours! Sum: ", sum)

    # Function: isFives
    # Date of code (Last updated): 10/6/2017
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
                Rules.fives = True
                Rules.fivesSum = sum
                print("You have Fives! Sum: ", sum)

    # Function: isSixes
    # Date of code (Last updated): 10/6/2017
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
                Rules.sixes = True
                Rules.sixesSum = sum
                print("You have Sixes! Sum: ", sum)
    
    # Function: isThreeOfAKind
    # Date of code (Last updated): 10/6/2017
    # Programmer: Brian Truong
    # Description: Checks if player has Three of a Kind
    # Input: list(dice)
    # Output: Boolean threeOfAKind
    def isThreeOfAKind(dice):
        sum = 0
        if (dice[2] == dice[3] == dice[4]):
            sum = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
            print("You have Three of a Kind! Sum: ", sum)
            Rules.threeOfAKind = True
            Rules.threeOfAKindSum = sum
            
        elif(dice[1] == dice[2] == dice[3]):
            sum = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
            print("You have Three of a Kind! Sum: ", sum)
            Rules.threeOfAKind = True
            Rules.threeOfAKindSum = sum
            
        elif(dice[0] == dice[1] == dice[2]):
            sum = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
            print("You have Three of a Kind! Sum: ", sum)
            Rules.threeOfAKind = True
            Rules.threeOfAKindSum = sum
           

    # Function: isFourOfAKind
    # Date of code (Last updated): 10/6/2017
    # Programmer: Brian Truong
    # Description: Checks if player has Four of a Kind
    # Input: list(dice)
    # Output: Boolean fourOfAKind
    def isFourOfAKind(dice):
        sum = 0
        if (dice[1]== dice[2] == dice[3] == dice[4]):
            sum = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
            print("You have Four of a Kind! Sum: ", sum)
            Rules.fourOfAKind = True
            Rules.fourOfAKindSum = sum
            
        elif(dice[0] == dice[1] == dice[2] == dice[3]):
            sum = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
            print("You have Four of a Kind! Sum: ", sum)
            Rules.fourOfAKind = True
            Rules.fourOfAKindSum = sum
            
        
    # Function: isFullHouse
    # Date of code (Last updated): 10/6/2017
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
            Rules.fullHouse = True
            Rules.fullHouseSum = sum
           
        elif(dice[0] == dice[1] == dice[2] and dice[3] == dice[4]):
            sum = 25
            print("You have a Full House! Sum: ", sum)
            Rules.fullHouse = True
            Rules.fullHouseSum = sum
           

    # Function: isSmallStraight
    # Date of code (Last updated): 10/6/2017
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
            Rules.smallStraight = True
            Rules.smallStraightSum = sum
            
        elif(list[1] == 2 and list[2] == 3 and list[3] == 4 and list[4] == 5):
            sum = 30
            print("You have a Small Straight! Sum: ", sum)
            Rules.smallStraight = True
            Rules.smallStraightSum = sum
           
        elif(list[0] == 1 and list[1] == 2 and list[2] == 3 and list[3] == 4):
            sum = 30
            print("You have a Small Straight! Sum: ", sum)
            Rules.smallStraight = True
            Rules.smallStraightSum = sum
           

    # Function: isLargeStraight
    # Date of code (Last updated): 10/6/2017
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
            Rules.largeStraight = True
            Rules.largeStraightSum = sum
            
        elif(list[0] == 1 and list[1] == 2 and list[2] == 3 and list[3] == 4 and list[4] == 5):
            sum = 40
            print("You have a Large Straight! Sum: ", sum)
            Rules.largeStraight = True
            Rules.largeStraightSum = sum
           

    # Function: isYahtzee
    # Date of code (Last updated): 10/6/2017
    # Programmer: Brian Truong
    # Description: Checks if the player has Yahtzee
    # Input: dice
    # Output: Boolean yahtzee
    def isYahtzee(dice):
        sum = 0
        if (dice[0] == dice[1] == dice[2] == dice[3] == dice[4]):
            sum = 50
            print("You have Yahtzee! Sum: ", sum)
            Rules.yahtzee = True
            Rules.yahtzeeSum = sum
            

    # Function: isChance
    # Date of code (Last updated): 10/6/2017
    # Programmer: Brian Truong
    # Description: Checks if the player has Chance
    # Input: dice
    # Output: Boolean chance
    def isChance(dice):
        sum = 0
        sum = dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
        print("You have Chance! Sum: ", sum)
        Rules.chance = True
        Rules.chanceSum = sum
        return Rules.chance

    # Function: runLowerSection
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: Runs all categories under the "Lower Section" rules of Yahtzee
    # Input: list(dice)
    # Output: N/A
    def runLowerSection(dice):
        Rules.isYahtzee(dice)
        Rules.isLargeStraight(dice)
        Rules.isSmallStraight(dice)
        Rules.isFullHouse(dice)
        Rules.isFourOfAKind(dice)
        Rules.isThreeOfAKind(dice)
        Rules.isChance(dice)

    # Function: passAces
    # Date of code (Last updated): 10/6/2017
    # Programmer: Brian Truong
    # Description: Passes value related to Ace category from Rule class to player class
    # Input: player(player)
    # Output: N/A
    def passAces(player):
        player.aceAvailable = Rules.aces
        player.acesScore = Rules.acesSum

    # Function: passTwos
    # Date of code (Last updated): 10/6/2017
    # Programmer: Brian Truong
    # Description: Passes value related to Twos category from Rule class to player class
    # Input: player(player)
    # Output: N/A
    def passTwos(player):
        player.twosAvailable = Rules.twos
        player.twosScore = Rules.twosSum

    # Function: passThrees
    # Date of code (Last updated): 10/6/2017
    # Programmer: Brian Truong
    # Description: Passes value related to Threes category from Rule class to player class
    # Input: player(player)
    # Output: N/A
    def passThrees(player):
        player.threesAvailable = Rules.threes
        player.threesScore = Rules.threesSum

    # Function: passFours
    # Date of code (Last updated): 10/6/2017
    # Programmer: Brian Truong
    # Description: Passes value related to Fours category from Rule class to player class
    # Input: player(player)
    # Output: N/A
    def passFours(player):
        player.foursAvailable = Rules.fours
        player.foursScore = Rules.foursSum

    # Function: passFives
    # Date of code (Last updated): 10/6/2017
    # Programmer: Brian Truong
    # Description: Passes value related to Fives category from Rule class to player class
    # Input: player(player)
    # Output: N/A
    def passFives(player):
        player.fivesAvailable = Rules.fives
        player.fivesScore = Rules.fivesSum

    # Function: passSixes
    # Date of code (Last updated): 10/6/2017
    # Programmer: Brian Truong
    # Description: Passes value related to Sixes category from Rule class to player class
    # Input: player(player)
    # Output: N/A
    def passSixes(player):
        player.sixesAvailable = Rules.sixes
        player.sixesScore = Rules.sixesSum

    # Function: passThreeOfAKind
    # Date of code (Last updated): 10/6/2017
    # Programmer: Brian Truong
    # Description: Passes value related to Three-Of-A-Kind category from Rule class to player class
    # Input: player(player)
    # Output: N/A
    def passThreeOfAKind(player):
        player.threeOfAKindAvailable = Rules.threeOfAKind
        player.threeOfAKindScore = Rules.threeOfAKindSum

    # Function: passFourOfAKind
    # Date of code (Last updated): 10/6/2017
    # Programmer: Brian Truong
    # Description: Passes value related to Four-Of-A-Kind category from Rule class to player class
    # Input: player(player)
    # Output: N/A
    def passFourOfAKind(player):
        player.fourOfAKindAvailable = Rules.fourOfAKind
        player.fourOfAKindScore = Rules.fourOfAKindSum

    # Function: passSmallStraight
    # Date of code (Last updated): 10/6/2017
    # Programmer: Brian Truong
    # Description: Passes value related to Small Straight category from Rule class to player class
    # Input: player(player)
    # Output: N/A
    def passSmallStraight(player):
        player.smallStraightAvailable = Rules.smallStraight
        player.smallStraightScore = Rules.smallStraightSum

    # Function: passLargeStraight
    # Date of code (Last updated): 10/6/2017
    # Programmer: Brian Truong
    # Description: Passes value related to LargeStraight category from Rule class to player class
    # Input: player(player)
    # Output: N/A
    def passLargeStraight(player):
        player.largeStraightAvailable = Rules.largeStraight
        player.largeStraightScore = Rules.largeStraightSum

    # Function: passFullHouse
    # Date of code (Last updated): 10/6/2017
    # Programmer: Brian Truong
    # Description: Passes value related to Full House category from Rule class to player class
    # Input: player(player)
    # Output: N/A
    def passFullHouse(player):
        player.fullHouseAvailable = Rules.fullHouse
        player.fullHouseScore = Rules.fullHouseSum

    # Function: passYahtzee
    # Date of code (Last updated): 10/6/2017
    # Programmer: Brian Truong
    # Description: Passes value related to Yahtzee category from Rule class to player class
    # Input: player(player)
    # Output: N/A
    def passYahtzee(player):
        player.yahtzeeAvailable = Rules.yahtzee
        player.yahtzeeScore = Rules.yahtzeeSum

    # Function: passChance
    # Date of code (Last updated): 10/6/2017
    # Programmer: Brian Truong
    # Description: Passes value related to Chance category from Rule class to player class
    # Input: player(player)
    # Output: N/A
    def passChance(player):
        player.chanceAvailable = Rules.chance
        player.chanceScore = Rules.chanceSum

    # Function: passAIFromPlayer
    # Date of code (Last updated): 10/17/2017
    # Programmer: Brian Truong
    # Description: Runs all methods related to passing variables from class Rule to class Player
    # Input: player(player)
    # Output: N/A
    def passAIFromPlayer(player):
        Rules.isAI = player.isAI;

    # Function: passChoices
    # Date of code (Last updated): 10/6/2017
    # Programmer: Brian Truong
    # Description: Runs all methods related to passing variables from class Rule to class Player
    # Input: player(player)
    # Output: N/A
    def passChoices(player):
        Rules.passYahtzee(player)
        Rules.passLargeStraight(player)
        Rules.passSmallStraight(player)
        Rules.passFullHouse(player)
        Rules.passFourOfAKind(player)
        Rules.passThreeOfAKind(player)
        Rules.passSixes(player)
        Rules.passFives(player)
        Rules.passFours(player)
        Rules.passThrees(player)
        Rules.passTwos(player)
        Rules.passAces(player)
        Rules.passChance(player)

