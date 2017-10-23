from pygame import *
import pygame
from BlockBase import BlockBase
from Scene import Scene

class BlockRectangle(BlockBase):
    
    def __init__(self, name, scene, x, y, width, height, color):

        # Call the parent class (Sprite) constructor
        super().__init__(name, scene, x, y)

        self.color = color
        self.width = width
        self.height = height

        sceneCoord = self.scene.virtualToSceneCoord(self.x, self.y)
        self.itemPtr = pygame.Rect(sceneCoord[0], sceneCoord[1], self.width, self.height)
        self.rect = self.itemPtr
        #self.image.set_colorkey(BLACK)

    def draw(self):

        sceneCoord = self.scene.virtualToSceneCoord(self.x, self.y)

        pygame.draw.rect(self.screenPtr, self.color, self.itemPtr)
