
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Yahtzee")

done = False

clock = pygame.time.Clock()

# Game logic initialization
backgroundColor = WHITE

btnRun = pygame.Rect(10, 410, 200, 75) # creates a rect object

dice1 = pygame.image.load("dice1.png").convert()
dice1.set_colorkey(WHITE)
x1 = 10
y1 = 10

dice2 = pygame.image.load("dice2.png").convert()
dice2.set_colorkey(WHITE)
x2 = 210
y2 = 10

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

while not done:
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos() # gets mouse position
        
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
 
            if btnRun.collidepoint(mouse_pos):
                #shake.play()
                roll.play()
            elif dice1.get_rect().collidepoint(mouse_pos):
                if y1 == 10:
                    y1 = 210
                else:
                    y1 = 10
            elif dice2.get_rect().collidepoint(mouse_pos):
                if y2 == 10:
                    y2 = 210
                else:
                    y2 = 10
        
         # --- Game logic should go here
 
        # -- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(backgroundColor)

        # Copy image to screen:
        screen.blit(dice1, [x1, y1])
        screen.blit(dice2, [x2, y2])
        
        #screen.blit(dice3, [10, 210])
        #screen.blit(dice4, [210, 210])

        pygame.draw.rect(screen, RED, btnRun) # draw objects down here


        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

# Close the window and quit.
pygame.quit()
            
