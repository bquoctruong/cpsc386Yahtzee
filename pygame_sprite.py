
#http://programarcadegames.com/index.php?lang=en&chapter=introduction_to_graphics
#base template
import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

screen_width = 700
screen_height = 400
size = (screen_width, screen_width)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Yahtzee Sprite")

done = False

clock = pygame.time.Clock()

# Game logic initialization
backgroundColor = WHITE

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        """ Constructor.  Pass in the color of the block,
        and its x and y position. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image.
        # Update the position of this object by setting the values
        # of rec.x and rect.y
        self.rect = self.image.get_rect()

    def update(self):
        """ Called each frame. """

        # Move block down one pixel
        self.rect.y += 1
        if self.rect.y > 410:
            self.reset_pos()
 
    def reset_pos(self):
        """ Reset position to the top of the screen, at a random x location.
        Called by update() or the main program loop if there is a collision.
        """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)

# This is a list of 'sprites.'  Each block in the program is
# added to this list.
# The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()

# This is a list of every sprites.
# All blocks and player blocks as well.
all_sprite_list = pygame.sprite.Group()

for i in range(50):
    # This represents a block
    block = Block(BLACK, 20, 15)

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    block_list.add(block)
    all_sprite_list.add(block)

# Create a RED player block
player = Block(RED, 20, 15)
all_sprite_list.add(player)

score = 0

# Hide the mouse cursor
#pygame.mouse.set_visible(0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Get the current mouse position.  This returns
        # a list of two numbers.
        pos = pygame.mouse.get_pos()

        # Fetch the x and y out of the list,
        # just like we fetch letters out of a string.
        # Set the players object to the mouse location.
        player.rect.x = pos[0]
        player.rect.y = pos[1]
        
        # --- Game logic should go here

       # See if the player block has collided with anything
        blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

        # Check the list of collisions
        for block in blocks_hit_list:
            score += 1
            print(score)

            # Reset block to the top of the screen to fall again.
            block.reset_pos()

        # -- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(backgroundColor)

        # Call the update() method for all blocks in the block_list
        block_list.update()
        
        # Draw all the sprites
        all_sprite_list.draw(screen)

        # --- Limit to 60 frames per second
        clock.tick(60)

         # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

# Close the window and quit.
pygame.quit()

