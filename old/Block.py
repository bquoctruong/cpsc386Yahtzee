
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Block(pygame.sprite.Sprite):
    def __init__(self, scr, imageFile, x, y):

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.image.load(imageFile).convert()
        self.image.set_colorkey(BLACK)

        # Fetch the rectangle object that has the dimensions of the image.
        # Update the position of this object by setting the values
        # of rec.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.scr = scr
        self.imageFile = imageFile
        self.x = x
        self.y = y

    def draw(self):
        self.scr.blit(self.image, [self.x, self.y])
    
    def updatePosition(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
