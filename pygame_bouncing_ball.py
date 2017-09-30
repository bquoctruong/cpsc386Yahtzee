
#http://programarcadegames.com/index.php?lang=en&chapter=introduction_to_graphics
#base template
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Yahtzee")

done = False

clock = pygame.time.Clock()

# Game logic initialization
backgroundColor = WHITE
rect_x = 50
rect_y = 50

rect_change_x = 5
rect_change_y = 5

# Speed in pixels per frame
x_speed = 0
y_speed = 0

#Current position
x_coord = 10
y_coord = 10

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1+x,y,10,10], 0)
 
    # Legs
    pygame.draw.line(screen, BLACK ,[5+x,17+y], [10+x,27+y], 2)
    pygame.draw.line(screen, BLACK, [5+x,17+y], [x,27+y], 2)
 
    # Body
    pygame.draw.line(screen, RED, [5+x,17+y], [5+x,7+y], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [5+x,7+y], [9+x,17+y], 2)
    pygame.draw.line(screen, RED, [5+x,7+y], [1+x,17+y], 2)


# Hide the mouse cursor
pygame.mouse.set_visible(0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key.
            # If so, adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3

        # --- Game logic should go here
 
        # -- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(backgroundColor)

        # Draw the graphics here
        #pygame.draw.rect(screen, RED, [55, 50, 20, 25], 0)
        #pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

        # Select the font to use size, bold, italics
        #font = pygame.font.SysFont('Calibri', 25, True, False)

        # Render the text. "True" means anti-aliased text.
        # Black is the color.  The variable BLACK was defined
        # above as a list of [0, 0, 0]
        # Note: this line creates an image of the letters,
        # but does not put it on the screen yet.
        #text = font.render("Yahtzee Score: " + str(35), True, BLACK)

        # Put the image of the text on the screen at 250x250
        #screen.blit(text, [250, 250])

        if rect_y > 450 or rect_y < 0:
            rect_change_y *= -1
        if rect_x > 650 or rect_x < 0:
            rect_change_x *= -1

        pygame.draw.rect(screen, GREEN, [rect_x, rect_y, 50, 50])
        pygame.draw.rect(screen, RED, [rect_x+10, rect_y+10, 30, 30])
        rect_x += rect_change_x
        rect_y += rect_change_y

        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]

        draw_stick_figure(screen, x_coord, y_coord)
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(80)

# Close the window and quit.
pygame.quit()
            
