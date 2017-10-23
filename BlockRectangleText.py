from pygame import *
import pygame
from BlockBase import BlockBase
from BlockRectangle import BlockRectangle
from Scene import Scene

class BlockRectangleText(BlockRectangle):
    
    def __init__(self, name, scene, x, y, width, height, color, text):

        # Call the parent class (Sprite) constructor
        super().__init__(name, scene, x, y, width, height, color)

        self.gameFont = pygame.font.SysFont('arial', 16)
        self.offset = (3, 3)
        self.setText(text)
        
    def setText(self, text):
        self.text = text
        self.textg = self.gameFont.render(str(self.text), False, (0, 0, 0))
        
    def draw(self):

        super().draw()
        
        sceneCoord = self.scene.virtualToSceneCoord(self.x, self.y)
        totalOffset = (sceneCoord[0] + self.offset[0], sceneCoord[1] + self.offset[1])

        self.screenPtr.blit(self.textg, [totalOffset[0], totalOffset[1]])        
