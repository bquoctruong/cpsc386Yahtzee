from pygame import *
import pygame

from BlockBase import BlockBase
from Scene import Scene
from BlockImage import BlockImage

class BlockScoreboard(BlockImage):
    
    def __init__(self, name, imageFile, scene, x, y, p1, p2):

        # Call the parent class (Sprite) constructor
        super().__init__(name, imageFile, scene, x, y)

        self.p1 = p1
        self.p2 = p2
        self.gameFont = pygame.font.SysFont('arial', 16)
        self.offset = (127, 46)
        self.interOffset = (43, 20)

    def outputValue(self, val):
        text = " "
        if val[0] or val[1] != 0:
            text = str(val[1])
        return text
    
    def outputValue1(self, val):
        text = " "
        if val != 0:
            text = str(val)
        return text

    
    def draw(self):

        super().draw()

        sceneCoord = self.scene.virtualToSceneCoord(self.x, self.y)
        totalOffset = (sceneCoord[0] + self.offset[0], sceneCoord[1] + self.offset[1])

        p1f1 = self.gameFont.render(self.outputValue(self.p1.acesScore), False, (0, 0, 0))
        p1f2 = self.gameFont.render(self.outputValue(self.p1.twosScore), False, (0, 0, 0))
        #print(self.p1.threesScore)
        p1f3 = self.gameFont.render(self.outputValue(self.p1.threesScore), False, (0, 0, 0))
        p1f4 = self.gameFont.render(self.outputValue(self.p1.foursScore), False, (0, 0, 0))
        p1f5 = self.gameFont.render(self.outputValue(self.p1.fivesScore), False, (0, 0, 0))
        p1f6 = self.gameFont.render(self.outputValue(self.p1.sixesScore), False, (0, 0, 0))
        p1tu = self.gameFont.render(self.outputValue1(self.p1.totalUpper()), False, (0, 0, 0))
        
        p1f7 = self.gameFont.render(self.outputValue(self.p1.threeOfAKindScore), False, (0, 0, 0))
        p1f8 = self.gameFont.render(self.outputValue(self.p1.fourOfAKindScore), False, (0, 0, 0))
        p1f9 = self.gameFont.render(self.outputValue(self.p1.fullHouseScore), False, (0, 0, 0))
        p1f10 = self.gameFont.render(self.outputValue(self.p1.smallStraightScore), False, (0, 0, 0))
        p1f11 = self.gameFont.render(self.outputValue(self.p1.largeStraightScore), False, (0, 0, 0))
        p1f12 = self.gameFont.render(self.outputValue(self.p1.yahtzeeScore), False, (0, 0, 0))
        p1f13 = self.gameFont.render(self.outputValue(self.p1.chanceScore), False, (0, 0, 0))
        p1t = self.gameFont.render(self.outputValue1(self.p1.totalScore()), False, (0, 0, 0))
        
        p2f1 = self.gameFont.render(self.outputValue(self.p2.acesScore), False, (0, 0, 0))
        p2f2 = self.gameFont.render(self.outputValue(self.p2.twosScore), False, (0, 0, 0))
        p2f3 = self.gameFont.render(self.outputValue(self.p2.threesScore), False, (0, 0, 0))
        p2f4 = self.gameFont.render(self.outputValue(self.p2.foursScore), False, (0, 0, 0))
        p2f5 = self.gameFont.render(self.outputValue(self.p2.fivesScore), False, (0, 0, 0))
        p2f6 = self.gameFont.render(self.outputValue(self.p2.sixesScore), False, (0, 0, 0))
        p2tu = self.gameFont.render(self.outputValue1(self.p2.totalUpper()), False, (0, 0, 0))
        
        p2f7 = self.gameFont.render(self.outputValue(self.p2.threeOfAKindScore), False, (0, 0, 0))
        p2f8 = self.gameFont.render(self.outputValue(self.p2.fourOfAKindScore), False, (0, 0, 0))
        p2f9 = self.gameFont.render(self.outputValue(self.p2.fullHouseScore), False, (0, 0, 0))
        p2f10 = self.gameFont.render(self.outputValue(self.p2.smallStraightScore), False, (0, 0, 0))
        p2f11 = self.gameFont.render(self.outputValue(self.p2.largeStraightScore), False, (0, 0, 0))
        p2f12 = self.gameFont.render(self.outputValue(self.p2.yahtzeeScore), False, (0, 0, 0))
        p2f13 = self.gameFont.render(self.outputValue(self.p2.chanceScore), False, (0, 0, 0))
        p2t = self.gameFont.render(self.outputValue1(self.p2.totalScore()), False, (0, 0, 0))
        
        self.screenPtr.blit(p1f1, [totalOffset[0] + self.interOffset[0]*0, totalOffset[1] + self.interOffset[1]*0 ])        
        self.screenPtr.blit(p1f2, [totalOffset[0] + self.interOffset[0]*0, totalOffset[1] + self.interOffset[1]*1 ])        
        self.screenPtr.blit(p1f3, [totalOffset[0] + self.interOffset[0]*0, totalOffset[1] + self.interOffset[1]*2 ])        
        self.screenPtr.blit(p1f4, [totalOffset[0] + self.interOffset[0]*0, totalOffset[1] + self.interOffset[1]*3 ])        
        self.screenPtr.blit(p1f5, [totalOffset[0] + self.interOffset[0]*0, totalOffset[1] + self.interOffset[1]*4 ])        
        self.screenPtr.blit(p1f6, [totalOffset[0] + self.interOffset[0]*0, totalOffset[1] + self.interOffset[1]*5 ])        
        self.screenPtr.blit(p1tu, [totalOffset[0] + self.interOffset[0]*0, totalOffset[1] + self.interOffset[1]*6 ])
       
        self.screenPtr.blit(p1f7, [totalOffset[0] + self.interOffset[0]*0, totalOffset[1] + self.interOffset[1]*9 ])
        self.screenPtr.blit(p1f8, [totalOffset[0] + self.interOffset[0]*0, totalOffset[1] + self.interOffset[1]*10 ])
        self.screenPtr.blit(p1f9, [totalOffset[0] + self.interOffset[0]*0, totalOffset[1] + self.interOffset[1]*11 ])
        self.screenPtr.blit(p1f10, [totalOffset[0] + self.interOffset[0]*0, totalOffset[1] + self.interOffset[1]*12 ])
        self.screenPtr.blit(p1f11, [totalOffset[0] + self.interOffset[0]*0, totalOffset[1] + self.interOffset[1]*13 ])
        self.screenPtr.blit(p1f12, [totalOffset[0] + self.interOffset[0]*0, totalOffset[1] + self.interOffset[1]*14 ])
        self.screenPtr.blit(p1f13, [totalOffset[0] + self.interOffset[0]*0, totalOffset[1] + self.interOffset[1]*15 ])
        self.screenPtr.blit(p1t, [totalOffset[0] + self.interOffset[0]*0, totalOffset[1] + self.interOffset[1]*16 ])

        self.screenPtr.blit(p2f1, [totalOffset[0] + self.interOffset[0]*1, totalOffset[1] + self.interOffset[1]*0 ])        
        self.screenPtr.blit(p2f2, [totalOffset[0] + self.interOffset[0]*1, totalOffset[1] + self.interOffset[1]*1 ])        
        self.screenPtr.blit(p2f3, [totalOffset[0] + self.interOffset[0]*1, totalOffset[1] + self.interOffset[1]*2 ])        
        self.screenPtr.blit(p2f4, [totalOffset[0] + self.interOffset[0]*1, totalOffset[1] + self.interOffset[1]*3 ])        
        self.screenPtr.blit(p2f5, [totalOffset[0] + self.interOffset[0]*1, totalOffset[1] + self.interOffset[1]*4 ])        
        self.screenPtr.blit(p2f6, [totalOffset[0] + self.interOffset[0]*1, totalOffset[1] + self.interOffset[1]*5 ])        
        self.screenPtr.blit(p2tu, [totalOffset[0] + self.interOffset[0]*1, totalOffset[1] + self.interOffset[1]*6 ])
       
        self.screenPtr.blit(p2f7, [totalOffset[0] + self.interOffset[0]*1, totalOffset[1] + self.interOffset[1]*9 ])
        self.screenPtr.blit(p2f8, [totalOffset[0] + self.interOffset[0]*1, totalOffset[1] + self.interOffset[1]*10 ])
        self.screenPtr.blit(p2f9, [totalOffset[0] + self.interOffset[0]*1, totalOffset[1] + self.interOffset[1]*11 ])
        self.screenPtr.blit(p2f10, [totalOffset[0] + self.interOffset[0]*1, totalOffset[1] + self.interOffset[1]*12 ])
        self.screenPtr.blit(p2f11, [totalOffset[0] + self.interOffset[0]*1, totalOffset[1] + self.interOffset[1]*13 ])
        self.screenPtr.blit(p2f12, [totalOffset[0] + self.interOffset[0]*1, totalOffset[1] + self.interOffset[1]*14 ])
        self.screenPtr.blit(p2f13, [totalOffset[0] + self.interOffset[0]*1, totalOffset[1] + self.interOffset[1]*15 ])
        self.screenPtr.blit(p2t, [totalOffset[0] + self.interOffset[0]*1, totalOffset[1] + self.interOffset[1]*16 ])

