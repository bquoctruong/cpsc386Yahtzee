from copy import deepcopy

# Class: Rules
# Date of code (Last updated): 9/27/2017
# Programmer: Brian Truong
# Description: Given player dices, determines what points may be given to the player
# Input:
# Output:
class Rules:

    def __init__(self, dices):

        self.dices = dices

        self.aces = (False, 0)
        self.twos = (False, 0)
        self.threes = (False, 0)
        self.fours = (False, 0)
        self.fives = (False, 0)
        self.sixes = (False, 0)
        
        self.threeOfAKind = (False, 0)
        self.fourOfAKind = (False, 0)
        self.fullHouse = (False, 0)
        self.smallStraight = (False, 0)
        self.largeStraight = (False, 0)
        self.yahtzee = (False, 0)
        self.chance = (False, 0)

    def selectCategory(self, index):
        
        item = None
        
        if index == 1:
            item = self.aces
        elif index == 2:
            item = self.twos
        elif index == 3:
            item = self.threes
        elif index == 4:
            item = self.fours
        elif index == 5:
            item = self.fives
        elif index == 6:
            item = self.sixes

        elif index == 7:
            item = self.threeOfAKind
        elif index == 8:
            item = self.fourOfAKind
        elif index == 9:
            item = self.fullHouse
        elif index == 10:
            item = self.smallStraight
        elif index == 11:
            item = self.largeStraight
        elif index == 12:
            item = self.yahtzee
        elif index == 13:
            item = self.chance
            
        return item
       
    # Function: runLowerSection
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: Runs all categories under the "Lower Section" rules of Yahtzee
    # Input: list(dice)
    # Output: N/A
    def runLowerSection(self):
        self.isYahtzee()
        self.isLargeStraight()
        self.isSmallStraight()
        self.isFullHouse()
        self.isFourOfAKind()
        self.isThreeOfAKind()
        self.isChance()

    # Function: runUpperSection
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: runs the set of rules (as functions) belonging to the upper section of the game Yahtzee
    # Input: list(dice)
    # Output:
    def runUpperSection(self):
        self.isAces()
        self.isTwos()
        self.isThrees()
        self.isFours()
        self.isFives()
        self.isSixes()

    # Function: isAces
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: Given a set of dice, determines if the dices have aces and sums up all "aces"
    # Input: dice
    # Output:
    def isAces(self):
        self.aces = self.processN(1)

    # Function: isTwos
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: Given a set of dice, determines if the dices have twos and sums up all "twos"
    # Input: dice
    # Output:
    def isTwos(self):
        self.twos = self.processN(2)
        
    # Function: isThrees
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: Given a set of dice, determines if the dices have threes and sums up all "threes"
    # Input: dice
    # Output:
    def isThrees(self):
        self.threes = self.processN(3)

    # Function: isFours
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: Given a set of dice, determines if the dices have fours and sums up all "fours"
    # Input: dice
    # Output:
    def isFours(self):
        self.fours = self.processN(4)
        
    # Function: isFives
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: Given a set of dice, determines if the dices have fives and sums up all "fives"
    # Input: dice
    # Output:
    def isFives(self):
        self.fives = self.processN(5)

    # Function: isSixes
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: Given a set of dice, determines if the dices have sixes and sums up all "sixes"
    # Input: dice
    # Output:
    def isSixes(self):
        self.sixes = self.processN(6)

    def processN(self, n):

        sum = 0
        criteria = (False, sum)
        for i in range(len(self.dices)):
            if (self.dices[i] == n):
                sum += n
        if (sum > 0):
            criteria = (True, sum)
            print("You have " + str(n) + "! Sum: ", sum)

        return criteria

    def buildLookup(self):
        lookup = {}

        for i in self.dices:
            if i > 0:
                if i in lookup:
                    lookup[i] += 1
                else:
                    lookup[i] = 1
                    
        return lookup
       
    def isNOfAKind(self, n):

        criteria = (False, 0, 0)
        lookup = self.buildLookup()
        
        for k, v in lookup.items():
            if v >= n:
                criteria = (True, k, v)
                break

        return criteria

    def buildIsNOfAKind(self, n):

        criteria = self.isNOfAKind(n)
        ruleCriteria = None
        
        if criteria[0]:
            ruleCriteria = (True, criteria[1]*criteria[2])
        else:
            ruleCriteria = (False, 0, 0)

        return ruleCriteria

    # Function: isThreeOfAKind
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: Checks if player has Three of a Kind
    # Input: list(dice)
    # Output: Boolean threeOfAKind
    def isThreeOfAKind(self):
        self.threeOfAKind = self.buildIsNOfAKind(3)

    # Function: isFourOfAKind
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: Checks if player has Four of a Kind
    # Input: list(dice)
    # Output: Boolean fourOfAKind
    def isFourOfAKind(self):
        self.fourOfAKind = self.buildIsNOfAKind(4)

    # Function: isFullHouse
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: checks if the player kept a Full House
    # Input: dice
    # Output: Boolean fullHouse
    def isFullHouse(self):

        pairFound = (False, 0)
        threeOfAKindFound = (False, 0)

        lookup = self.buildLookup()

        for k, v in lookup.items():
            if v == 2:
                pairFound = (True, k)
            elif v == 3:
                threeOfAKindFound = (True, k)

        if pairFound[0] and threeOfAKindFound[0]:
            self.fullHouse = (True, 25)
        else:
            self.fullHouse = (False, 0)

    def buildSequentialList(self):

        sortedList = []
        tempList = sorted(deepcopy(self.dices))

        for i in range(0, len(tempList)):
            if tempList[i] > 0:
                if i == 0:
                    sortedList.append(tempList[i])
                elif i > 0 and (tempList[i]-tempList[i-1] == 1):
                    sortedList.append(tempList[i])

        return sortedList

    def processStraight(self, n, score):
        
        sortedList = self.buildSequentialList()
        if len(sortedList) >= n:
            print(sortedList)
            return (True, score)
        else:
            return (False, 0)
        
    # Function: isSmallStraight
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: Detects if the kept dice have a Small Straight
    # Input: list(dice)
    # Output: Boolean smallStraight
    def isSmallStraight(self):
        self.smallStraight = self.processStraight(4, 30)
            
    # Function: isLargeStraight
    # Date of code (Last updated): 9/27/2017
    # Programmer: Brian Truong
    # Description: To determine if the player rolled a Large Straight
    # Input: list(self.dices)
    # Output: Boolean largeStraight
    def isLargeStraight(self):
        self.largeStraight = self.processStraight(5, 40)

    # Function: isYahtzee
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: Checks if the player has Yahtzee
    # Input: dice
    # Output: Boolean yahtzee
    def isYahtzee(self):
        sum = 0
        if self.dices[0] > 0 and (self.dices[0] == self.dices[1] == self.dices[2] == self.dices[3] == self.dices[4]):
            sum = 50
            print("You have Yahtzee! Sum: ", sum)
            self.yahtzee = (True, sum)

        return self.yahtzee

    # Function: isChance
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: Checks if the player has Chance
    # Input: self.dices
    # Output: Boolean chance
    def isChance(self):
        sum = 0

        for i in self.dices:
            sum += i

        if sum > 0:
            print("You have Chance! Sum: ", sum)
            self.chance = (True, sum)
        else:
            self.chance = (False, sum)

        return self.chance

    def runSections(self):
        self.runUpperSection()
        self.runLowerSection()

