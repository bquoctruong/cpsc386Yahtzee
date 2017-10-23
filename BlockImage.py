from pygame import *
import pygame

from BlockBase import BlockBase
from Scene import Scene

class BlockImage(BlockBase):
    
    def __init__(self, name, imageFile, scene, x, y):

        # Call the parent class (Sprite) constructor
        super().__init__(name, scene, x, y)

        self.imageFile = imageFile
        self.itemPtr = pygame.image.load(imageFile).convert()
        self.rect = self.itemPtr.get_rect()
        #self.image.set_colorkey(BLACK)

        super().updatePosition(x, y)

    def draw(self):

        sceneCoord = self.scene.virtualToSceneCoord(self.x, self.y)

        self.screenPtr.blit(self.itemPtr, [sceneCoord[0], sceneCoord[1]])
