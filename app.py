# The following code was obtained from the URL:
#   https://realpython.com/pygame-a-primer/ 

# Simple pygame program


# Import and initialize the pygame library

import pygame

# Import pygame.locals for easier access to key coordinates

# Updated to conform to flake8 and black standards

from pygame.locals import (

    K_UP,

    K_DOWN,

    K_LEFT,

    K_RIGHT,

    K_ESCAPE,

    KEYDOWN,

    QUIT,

)

pygame.init()

# Object pos

x_pos,y_pos = 415,15

# object position change in case of key stroke event
delta_x, delta_y = 10,10

# Variable for checking if a collision occurred

collision = False

# Set up the drawing window

screen = pygame.display.set_mode([500, 500])

# create a surface object, image is drawn on it
image = pygame.image.load(r'maze.png');
image = pygame.transform.scale(image,(500,500))

# Setting color at a given pixel where collision was not being detected

x = 215

while x <= 315:
    image.set_at((x,275),(0,0,255,0))
    x += 10

x = 315

while x <= 435:
    image.set_at((x,365),(0,0,255,0))
    x+= 10


x = 315
while x <= 375:
    image.set_at((x,315),(0,0,255,0))
    x += 10

x= 55
while x <= 115:
    image.set_at((x,215),(0,0,255,0))
    x+= 10

x = 445
while x <= 485:
    image.set_at((x,315),(0,0,255,0))
    x+=10
# Run until the user asks to quit

# Here we will have a boolean variable which will be used 
# for the condition that will keep our while loop running

running = True

# Boolean variable to check for collision

collision = False

while running:
    
    # Check for collision


    # Did the user click the window close button?

    for event in pygame.event.get():
        
        # When the user clicks the close button
        # the window will close and the program will
        # quit, by setting the running variable to false
        # By doing this our while loop will be terminated
        # along with our program

        if event.type == pygame.QUIT:

            running = False

        if event.type == KEYDOWN:
            
            if event.key == K_UP and image.get_at((x_pos,y_pos-10)) == (255,255,255):
                print("Up was pressed")
                y_pos -= 10

            elif image.get_at((x_pos,y_pos-10)) != (255,255,255):
                collision == True

            if event.key == K_DOWN and image.get_at((x_pos,y_pos+10)) == (255,255,255):
                print("Down was pressed")
                y_pos += 10
            
            elif image.get_at((x_pos,y_pos+10)) == (255,255,255):
                collision = True

            if event.key == K_RIGHT and image.get_at((x_pos+10,y_pos))==(255,255,255):

                print("Right was pressed");
                x_pos += 10

            elif image.get_at((x_pos+10,y_pos)) == (255,255,255):
                collision =True

            if event.key == K_LEFT and image.get_at((x_pos-10,y_pos)) == (255,255,255):
                print("Left was pressed");
                x_pos -= 10

            elif image.get_at((x_pos-10,y_pos)) == (255,255,255):
                collision = True

        if event.type == pygame.KEYUP:
            print("Key was released")


    # Fill the background with white
    # This is done by setting all of our RGB
    # values to 255

    screen.fill((255, 255, 255))

    # Copying the image surface
    # to display surface object at
    # (0,0) coordinate

    screen.blit(image,(0,0))
    

    # Draw a solid blue circle in the center
    # The first parameter is screen, which refers to the 
    # window where we will draw our circle, the second parameter
    # will be a tuple of three values that correspond to our RGB
    # values, the thrid parameter will be the coordinates of the center of my figure
    # The last parameter is the radius of my circle

    print("Color: ",image.get_at((x_pos,y_pos)))
    print("Position: ",(x_pos,y_pos))
    pygame.draw.circle(screen, (0, 0, 255), (x_pos, y_pos),10)
    

    # Flip the display, updates content in display

    pygame.display.flip()

    #if collision == True:
     #   running = False

# Done! Time to quit.

pygame.quit()
