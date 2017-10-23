
from BlockBase import BlockBase

class Scene:

    def __init__(self, screenPtr, width, height, xLength, yLength, margin):

        self.screenPtr = screenPtr
        self.width = width
        self.height = height
        self.xLength = xLength
        self.yLength = yLength
        self.margin = margin

        self.cellWidth = self.width/xLength
        self.cellHeight = self.height/yLength

        self.itemList = {}

    def addItem(self, item):
        self.itemList[item.name] = item

    def removeItem(self, item):
        del self.itemList[item.name]
        
    def virtualToSceneCoord(self, x, y):
        realX = x*self.cellWidth + self.margin
        realY = y*self.cellHeight + self.margin

        return (realX, realY)

    def draw(self):
        for k, v in self.itemList.items():
            v.draw()

    def isClicked(self, itemName, mousePos):
        item = self.itemList[itemName]
        
        return item.rect.collidepoint(mousePos)

    def getItemClicked(self, mousePos):

        itemName = ""
        
        for k, v in self.itemList.items():
            if self.isClicked(k, mousePos):
                itemName = k
                break
        return itemName

    def clearWithPattern(self, pattern):
        toRemoveList = []
        
        for k, v in self.itemList.items():
            if k.startswith(pattern):
                toRemoveList.append(k)

        for i in toRemoveList:
            del self.itemList[i]

