
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

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
        self. rect.y = y

size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Yahtzee")

done = False

clock = pygame.time.Clock()

# Game logic initialization
backgroundColor = WHITE

btnRun = pygame.Rect(10, 410, 200, 75) # creates a rect object

dice1 = Block(screen, "dice1.png", 10, 10)

dice2 = Block(screen, "dice2.png", 210, 10)

dice3 = pygame.image.load("dice3.png").convert()
dice3.set_colorkey(WHITE)

dice4 = pygame.image.load("dice4.png").convert()
dice4.set_colorkey(WHITE)

dice5 = pygame.image.load("dice5.png").convert()
dice5.set_colorkey(WHITE)

dice6 = pygame.image.load("dice6.png").convert()
dice6.set_colorkey(WHITE)

shake = pygame.mixer.Sound("shake.wav")
roll = pygame.mixer.Sound("roll.wav")

"""elif dice1.rect.collidepoint(mouse_pos):
                if dice1.y == 10:
                    dice1.y = 210
                else:
                    dice1.y = 10
                print("dice1.y " + str(dice1.y))"""
"""            if btnRun.collidepoint(mouse_pos):
                #shake.play()
                roll.play()
"""
while not done:
    mouse_pos = pygame.mouse.get_pos() # gets mouse position
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if btnRun.collidepoint(mouse_pos):
                roll.play()
            
            elif dice1.rect.collidepoint(mouse_pos):
                if dice1.y == 10:
                    dice1.updatePosition(dice1.x, 210)
                else:
                    dice1.updatePosition(dice1.x, 10)

                print("dice1.y " + str(dice1.y))
                
            elif dice2.rect.collidepoint(mouse_pos):
                if dice2.y == 10:
                    dice2.updatePosition(dice2.x, 210)
                else:
                    dice2.updatePosition(dice2.x, 10)

                print("dice2.y " + str(dice2.y))
                
            else:
                x = 1
        else:
            x = 1
        
         # --- Game logic should go here
 
        # -- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(backgroundColor)

        # Copy image to screen:
        dice1.draw()
        dice2.draw()
         
        #screen.blit(dice3, [10, 210])
        #screen.blit(dice4, [210, 210])

        pygame.draw.rect(screen, RED, btnRun) # draw objects down here


        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

# Close the window and quit.
pygame.quit()
            
