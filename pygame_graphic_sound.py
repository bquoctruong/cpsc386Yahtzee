
#http://programarcadegames.com/index.php?lang=en&chapter=introduction_to_graphics
#base template
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

background_image = pygame.image.load("saturn_family1.jpg").convert()

player_image = pygame.image.load("playerShip1_orange.png").convert()
player_image.set_colorkey(BLACK)

click_sound = pygame.mixer.Sound("laser5.ogg")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
        
        # Get the current mouse position.  This returns the position
        # as a list of two numbers.
        player_position = pygame.mouse.get_pos()
        x = player_position[0]
        y = player_position[1]

        # --- Game logic should go here
 
        # -- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        #screen.fill(backgroundColor)
        screen.blit(background_image, [0, 0])


        # Copy image to screen:
        screen.blit(player_image, [x, y])
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

# Close the window and quit.
pygame.quit()
            
