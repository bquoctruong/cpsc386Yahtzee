import pygame

class BlockBase(pygame.sprite.Sprite):
    
    def __init__(self, name, scene, x, y):

        # Call the parent class (Sprite) constructor
        super().__init__()

        self.name = name
        self.scene = scene
        self.screenPtr = self.scene.screenPtr
        self.x = x
        self.y = y
        #set by subclasses
        self.itemPtr = None
        self.rect = None

        self.item = None
    
    def updatePosition(self, x, y):
        self.x = x
        self.y = y
        if self.rect is not None:
            sceneCoord = self.scene.virtualToSceneCoord(self.x, self.y)
            self.rect.x = sceneCoord[0]
            self.rect.y = sceneCoord[1]

    #virtual method
    #to be overriden
    def draw(self):
        self.name = self.name
