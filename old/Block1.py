import pygame

class Block1(pygame.sprite.Sprite):
    def __init__(self, screenPtr, isImage, imageFile):

        # Call the parent class (Sprite) constructor
        super().__init__()

        self.screenPtr = screenPtr

        self.imageFile = imageFile
        self.image = pygame.image.load(imageFile).convert()
        self.rect = self.image.get_rect()
        #self.image.set_colorkey(BLACK)

    def draw(self):
        self.scr.blit(self.image, [self.x, self.y])
    
    def updatePosition(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
