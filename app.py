from playsound import playsound
import time
from network import Network

# This function will be used to checck if the player is currently steping on a mine

def check_for_mine(mine_coor, x, y):

    # The following for loop will iterate through
    for item in mine_coor:
        if item == (x,y):
            playsound('explosion.wav')
            return True

    return False





# This function checks for and deactivates the mines of another player
def check_perimeter_for_mine(mine_coor, x, y):
    perimeter = [(x-10,y), (x+10,y), (x,y-10), (x,y+10), (x-10,y-10), (x+10,y-10), (x-10,y+10),(x+10,y+10)]
    deactivate_mines = []
    for coor in perimeter:
        for item in mine_coor:
            if coor == item:
                deactivate_mines.append(coor)
                mine_coor.remove(coor)
    return deactivate_mines








# The function checks for walls and keeps the playerr from walking through walls
def check_for_collision(canvas,x,y,direction):
    
    if direction == 'UP':
        if canvas.get_at((x,y-10)) == (255,255,255):
            return False
        else:
            return True

    if direction == 'DOWN':
        if canvas.get_at((x,y+10)) == (255,255,255):
            return False
        else:
            return True

    if direction == 'LEFT':
        if canvas.get_at((x-10,y)) == (255,255,255):
            return False
        else:
            return True

    if direction == 'RIGHT':
        if canvas.get_at((x+10,y)) == (255,255,255):
            return False
        else:
            return True









def moveUp(canvas,x,y):

    if check_for_collision(canvas,x,y,'UP') == False:
        y -= 10;        
        return y

    else:
        return y
        








def moveDown(canvas,x,y):

    if check_for_collision(canvas,x,y,'DOWN') == False:
        y+=10
        return y
    else:
        return y









def moveLeft(canvas,x,y):

    if check_for_collision(canvas, x, y, 'LEFT') == False:
        x-=10
        return x
    else:
        return x








def moveRight(canvas,x,y):

    if check_for_collision(canvas, x, y, 'RIGHT') == False:
        x+= 10
        return x
    else:
        return x




def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


# The following code was obtained from the URL:


# Simple pygame program


# Import and initialize the pygame library

import pygame
import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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

x_pos_b,y_pos_b = 415, 15
x_pos_r,y_pos_r = 75, 425

# object position change in case of key stroke event
delta_x, delta_y = 10,10

# Variable for checking if a collision occurred

collision = False

# Set up the drawing window

screen = pygame.display.set_mode([500, 500])

# create a surface object, image is drawn on it
image = pygame.image.load(r'maze.png');
image = pygame.transform.scale(image,(500,500))

# win/lose screen

redwin = pygame.image.load('redwins.png');
redwin = pygame.transform.scale(redwin,(500,500))
bluewin = pygame.image.load('bluewins.png')
bluewin = pygame.transform.scale(bluewin,(500,500))

bomb = pygame.image.load('bombs/bomb1.jpeg')
bomb = pygame.transform.scale(bomb,(50,50))

# Mine coordinates

#mine_coor = [(415,205),(265,215),(85,275),(35,405),(225,385),(345,95),(335,165)]
mine_coor_b = []
mine_coor_r = []

#   101 -> E (jam mine)
#   307 -> right alt (jam mine)
#   119 -> W (move up)
#   115 -> S (move down)
#   97 -> A (move left)
#   100 -> D (move right)



wasd = [119,115,97,100]



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
start = time.time()

time.clock()

elapsed = 0
old_elapsed = 0

red_deactivated = False
blue_deactivated = False
mine  = []

n = Network()
startPos = read_pos(n.getPos())


while running:
    elapsed = time.time() - start    
    # Check for collision

    p2Pos = read_pos(n.send(make_pos((x_pos_b, y_pos_b))))

    x_pos_b = p2Pos[0]
    y_pos_b = p2Pos[1]
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
            
            if event.key == K_UP:
                y_pos_b = moveUp(image,x_pos_b,y_pos_b)
                pygame.draw.circle(screen, (0, 0, 255), (x_pos_b, y_pos_b),10)


            if event.key == K_DOWN:
                y_pos_b = moveDown(image,x_pos_b,y_pos_b) 
                pygame.draw.circle(screen, (0, 0, 255), (x_pos_b, y_pos_b),10)

            if event.key == K_RIGHT:
                x_pos_b = moveRight(image, x_pos_b, y_pos_b)
                pygame.draw.circle(screen, (0, 0, 255), (x_pos_b, y_pos_b),10)

            if event.key == K_LEFT:
                x_pos_b = moveLeft(image, x_pos_b,y_pos_b)
                pygame.draw.circle(screen, (0, 0, 255), (x_pos_b, y_pos_b),10)
        
            
            if event.key == 119:
                y_pos_r = moveUp(image,x_pos_r,y_pos_r)

            if event.key == 115:
                y_pos_r = moveDown(image,x_pos_r,y_pos_r)

            if event.key == 97:
                x_pos_r = moveLeft(image,x_pos_r, y_pos_r)

            if event.key == 100:
                x_pos_r = moveRight(image, x_pos_r, y_pos_r)
            
            # X was pressed 
            if event.key == 120:
                mine_coor_r.append((x_pos_r,y_pos_r))
            
            # Right Control key was presssed
            if event.key == 305:
                mine_coor_b.append((x_pos_b,y_pos_b))
            

            # CHeck if red player pressed E,
            # He will deactivate the mines deployed by blue 
            # player for 5 seconds

            if event.key == 101:
                red_deactivated = True
                mines = check_perimeter_for_mine(mine_coor_b,x_pos_r,y_pos_r)
                for item in mines:
                    mine.append(item)
                if mine != []:
                    old_elapsed = elapsed
                    print(old_elapsed)
            
            # CHeck if blue player pressed right alt,
            # if so blue player will deactivate red player's mines for five
            # seconds

            if event.key == 307:
                blue_deactivated = True
                mines = check_perimeter_for_mine(mine_coor_r, x_pos_b, y_pos_b)
                for item in mines:
                    mine.append(item)
                
                if mine != []:
                     
                    old_elapsed = elapsed
                    print(old_elapsed)

    # Here we will reactivate mines that were deactivated 5 seconds age
    if elapsed >= old_elapsed+5 and old_elapsed != 0:
        print("Hello I'm yelo")
        if red_deactivated == True:
            red_deativated = False
            for item in mine:
                mine_coor_b.append(item)
                mine.remove(item)

        if blue_deactivated == True:
            blue_deactivated = False
            for item in mine:
                mine_coor_r.append(item)
                mine.remove(item)
                
            
    #print(elapsed, old_elapsed)

#        if event.type == pygame.KEYUP:
#            print("Key was released")

    
    # Fill the background with white
    # This is done by setting all of our RGB
    # values to 255

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

    #print("Color: ",image.get_at((x_pos_b,y_pos_b)))
    #print("Circle Position: ",(x_pos_b,y_pos_b))
    
    if check_for_mine(mine_coor_r,x_pos_b,y_pos_b) == True:
        screen.blit(bomb,(x_pos_b-10,y_pos_b-10))
        print("Blue lost")
        screen.fill((255,255,255))
        screen.blit(redwin,(0,0))
        pygame.display.update()
        break

    if check_for_mine(mine_coor_b, x_pos_r, y_pos_r) == True:
        print("Red lost")
        screen.fill((255,255,255))
        screen.blit(bluewin,(0,0))
        pygame.display.update()
        break



    if y_pos_b >= 445:
        print("Blue won!");
        playsound('win.wav')
        screen.fill((255,255,255))
        screen.blit(bluewin,(0,0))
        pygame.display.update()
        break

    if y_pos_r <= 15:
        print("Red won!")
        playsound('win.wav')
        screen.fill((255,255,255))
        screen.blit(redwin,(0,0))
        pygame.display.update()
        break


    pygame.draw.circle(screen, (0, 0, 255), (x_pos_b, y_pos_b),10)
    pygame.draw.circle(screen, (255, 0, 0), (x_pos_r, y_pos_r), 10)

    # Flip the display, updates content in display

    pygame.display.flip()
    
        
    #if collision == True:
     #   running = False

# Done! Time to quit.

pygame.quit()
