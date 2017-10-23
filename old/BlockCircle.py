from BlockBase import BlockBase

class BlockCircle(BlockBase):
    
    def __init__(self, scene, screenPtr, x, y):

        # Call the parent class (Sprite) constructor
        super().__init__(self, scene, screenPtr, x, y)

        self.color = color
        self.itemPtr = pygame.image.load(imageFile).convert()
        self.rect = self.itemPtr.get_rect()
        #self.image.set_colorkey(BLACK)

    def draw(self):

        super().draw(self)

        pygame.draw.rect(self.screenPtr, self.color, btnRollDice)
