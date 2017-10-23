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
        sum = 0
        for x in range(len(self.dices)):
            if (self.dices[x] == 1):
                sum += 1
        if (sum > 0):
            self.aces = (True, sum)
            print("You have Aces! Sum: ", sum)

    # Function: isTwos
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: Given a set of dice, determines if the dices have twos and sums up all "twos"
    # Input: dice
    # Output:
    def isTwos(self):
        sum = 0
        for x in range(len(self.dices)):
            if (self.dices[x] == 2):
                sum += 2
        if (sum > 0):
            self.twos = (True, sum)
            print("You have Twos! Sum: ", sum)

    # Function: isThrees
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: Given a set of dice, determines if the dices have threes and sums up all "threes"
    # Input: dice
    # Output:
    def isThrees(self):
        sum = 0
        for x in range(len(self.dices)):
            if (self.dices[x] == 3):
                sum += 3
        if (sum > 0):
            self.threes = (True, sum)
            print("You have Threes! Sum: ", sum)

    # Function: isFours
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: Given a set of dice, determines if the dices have fours and sums up all "fours"
    # Input: dice
    # Output:
    def isFours(self):
        sum = 0
        for x in range(len(self.dices)):
            if (self.dices[x] == 4):
                sum += 4
        if (sum > 0):
            self.fours = (True, sum)
            print("You have Fours! Sum: ", sum)

    # Function: isFives
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: Given a set of dice, determines if the dices have fives and sums up all "fives"
    # Input: dice
    # Output:
    def isFives(self):
        sum = 0
        for x in range(len(self.dices)):
            if (self.dices[x] == 5):
                sum += 5
        if (sum > 0):
            self.fives = (True, sum)
            print("You have Fives! Sum: ", sum)

    # Function: isSixes
    # Date of code (Last updated): 9/25/2017
    # Programmer: Brian Truong
    # Description: Given a set of dice, determines if the dices have sixes and sums up all "sixes"
    # Input: dice
    # Output:
    def isSixes(self):
        sum = 0
        for x in range(len(self.dices)):
            if (self.dices[x] == 6):
                sum += 6
        if (sum > 0):
            self.sixes = (True, sum)
            print("You have Sixes! Sum: ", sum)

    # Function: isThreeOfAKind
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: Checks if player has Three of a Kind
    # Input: list(dice)
    # Output: Boolean threeOfAKind
    def isThreeOfAKind(self):
        sum = 0
        if self.dices[2] > 0 and (self.dices[2] == self.dices[3] == self.dices[4]):
            sum = self.dices[0] + self.dices[1] + self.dices[2] + self.dices[3] + self.dices[4]
            print("You have Three of a Kind! Sum: ", sum)
            self.threeOfAKind = (True, sum)
        elif self.dices[1] > 0 and (self.dices[1] == self.dices[2] == self.dices[3]):
            sum = self.dices[0] + self.dices[1] + self.dices[2] + self.dices[3] + self.dices[4]
            print("You have Three of a Kind! Sum: ", sum)
            self.threeOfAKind = (True, sum)
        elif self.dices[0] > 0 and (self.dices[0] == self.dices[1] == self.dices[2]):
            sum = self.dices[0] + self.dices[1] + self.dices[2] + self.dices[3] + self.dices[4]
            print("You have Three of a Kind! Sum: ", sum)
            self.threeOfAKind = (True, sum)

        return self.threeOfAKind

    # Function: isFourOfAKind
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: Checks if player has Four of a Kind
    # Input: list(dice)
    # Output: Boolean fourOfAKind
    def isFourOfAKind(self):
        sum = 0
        if self.dices[1] > 0 and (self.dices[1] == self.dices[2] == self.dices[3] == self.dices[4]):
            sum = self.dices[0] + self.dices[1] + self.dices[2] + self.dices[3] + self.dices[4]
            print("You have Four of a Kind! Sum: ", sum)
            self.fourOfAKind = (True, sum)
        elif self.dices[0] > 0 and (self.dices[0] == self.dices[1] == self.dices[2] == self.dices[3]):
            sum = self.dices[0] + self.dices[1] + self.dices[2] + self.dices[3] + self.dices[4]
            print("You have Four of a Kind! Sum: ", sum)
            self.fourOfAKind = (True, sum)

        return self.fourOfAKind

    # Function: isFullHouse
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: checks if the player kept a Full House
    # Input: dice
    # Output: Boolean fullHouse
    def isFullHouse(self):
        sum = 0
        if self.dices[0] > 0 and (self.dices[0] == self.dices[1] and self.dices[2] > 0 and self.dices[2] == self.dices[3] == self.dices[4]):
            sum = 25
            print("You have a Full House! Sum: ", sum)
            self.fullHouse = (True, sum)
        elif self.dices[0] > 0 and (self.dices[0] == self.dices[1] == self.dices[2] and self.dices[3] > 0 and self.dices[3] == self.dices[4]):
            sum = 25
            print("You have a Full House! Sum: ", sum)
            self.fullHouse = (True, sum)

        return self.fullHouse

    # Function: isSmallStraight
    # Date of code (Last updated): 9/28/2017
    # Programmer: Brian Truong
    # Description: Detects if the kept dice have a Small Straight
    # Input: list(dice)
    # Output: Boolean smallStraight
    def isSmallStraight(self):
        sum = 0
        list = [0, 0, 0, 0, 0, 0]

        # detects dice number and assigns them a slot in list
        # does not store duplicates
        # print("Checking dices")
        for x in range(len(self.dices)):
            if (self.dices[x] == 1):
                list[0] = 1
            if (self.dices[x] == 2):
                list[1] = 2
            if (self.dices[x] == 3):
                list[2] = 3
            if (self.dices[x] == 4):
                list[3] = 4
            if (self.dices[x] == 5):
                list[4] = 5
            if (self.dices[x] == 6):
                list[5] = 6

        # print("detecting three of a kind")
        # print(list)
        # detects three of a kind, going by possible triplet
        if (list[2] == 3 and list[3] == 4 and list[4] == 5 and list[5] == 6):
            sum = 30
            print("You have a Small Straight! Sum: ", sum)
            self.smallStraight = (True, sum)
        elif (list[1] == 2 and list[2] == 3 and list[3] == 4 and list[4] == 5):
            sum = 30
            print("You have a Small Straight! Sum: ", sum)
            self.smallStraight = (True, sum)
        elif (list[0] == 1 and list[1] == 2 and list[2] == 3 and list[3] == 4):
            sum = 30
            print("You have a Small Straight! Sum: ", sum)
            self.smallStraight = (True, sum)

        return self.smallStraight

    # Function: isLargeStraight
    # Date of code (Last updated): 9/27/2017
    # Programmer: Brian Truong
    # Description: To determine if the player rolled a Large Straight
    # Input: list(self.dices)
    # Output: Boolean largeStraight
    def isLargeStraight(self):
        sum = 0
        # print("Begin sorting")
        list = [0, 0, 0, 0, 0, 0]

        # detects dice number and assigns them a slot in list
        # does not store duplicates
        # print("Checking dices")
        for x in range(len(self.dices)):
            if (self.dices[x] == 1):
                list[0] = 1
            if (self.dices[x] == 2):
                list[1] = 2
            if (self.dices[x] == 3):
                list[2] = 3
            if (self.dices[x] == 4):
                list[3] = 4
            if (self.dices[x] == 5):
                list[4] = 5
            if (self.dices[x] == 6):
                list[5] = 6

        # print("detecting three of a kind")
        # print(list)
        # detects three of a kind, going by possible triplet
        if (list[1] == 2 and list[2] == 3 and list[3] == 4 and list[4] == 5 and list[5] == 6):
            sum = 40
            print("You have a Large Straight! Sum: ", sum)
            self.largeStraight = (True, sum)
        elif (list[0] == 1 and list[1] == 2 and list[2] == 3 and list[3] == 4 and list[4] == 5):
            sum = 40
            print("You have a Large Straight! Sum: ", sum)
            self.largeStraight = (True, sum)

        return self.largeStraight

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
        sum = self.dices[0] + self.dices[1] + self.dices[2] + self.dices[3] + self.dices[4]
        if sum > 0:
            print("You have Chance! Sum: ", sum)
            self.chance = (True, sum)
        else:
            self.chance = (False, sum)

        return self.chance

    def runSections(self):
        self.runUpperSection()
        self.runLowerSection()
