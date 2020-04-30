from playsound import playsound
import time
import threading

import random

circle_radius = 10
map_index = random.randint(0,2)

if map_index == 0:
    image_file = 'maze.png'
elif map_index == 1:
    image_file = 'maze2.png'
elif map_index == 2:
    image_file = 'Maze4.png'

import socket
#from network import Network



#I'm using this to define the walkthrough ability
phasing = False;
phaseStart = 0;
phasingReady = True;

#variables for the shoot ability
projectile = False;
shootReady = True;
shootStart = 0;
clickX = 0;
clickY = 0;
slopeX = 0;
slopeY = 0;
projX = 0
projY = 0

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname(socket.gethostname())
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)


n = Network()
print(n.send("Client connected at " + str(n.server)))

# This function will be used to checck if the player is currently steping on a mine

def check_for_mine(mine_coor, x, y):

    # The following for loop will iterate through
    for item in mine_coor:
        
#        if (item[0] - x) <= 25 and (item[1] - y) <= 25:
#            playsound('tick.wav')

        if item == (x,y):
            pygame.draw.circle(screen,(0,0,255),(x_pos_b, y_pos_b),circle_radius)
            pygame.draw.circle(screen, (255,0,0),(x_pos_r,y_pos_r),circle_radius)
            pygame.draw.circle(screen, (255,0,0), (x,y), 10)
            pygame.draw.circle(screen, (250,250,0), (x,y), 10)
            pygame.display.flip()

            pygame.draw.circle(screen,(0,0,255),(x_pos_b, y_pos_b),circle_radius)
            pygame.draw.circle(screen, (255,0,0),(x_pos_r,y_pos_r),circle_radius)
            pygame.draw.circle(screen, (255,0,0), (x,y), 20)
            pygame.draw.circle(screen, (250,250,0), (x,y), 10)
            pygame.display.flip()

            pygame.draw.circle(screen,(0,0,255),(x_pos_b, y_pos_b),circle_radius)
            pygame.draw.circle(screen, (255,0,0),(x_pos_r,y_pos_r),circle_radius)
            pygame.draw.circle(screen, (255,0,0), (x,y), 25)
            pygame.draw.circle(screen, (250,250,0), (x,y), 15)
            pygame.display.flip()

            pygame.draw.circle(screen,(0,0,255),(x_pos_b, y_pos_b),circle_radius)
            pygame.draw.circle(screen, (255,0,0),(x_pos_r,y_pos_r),circle_radius)
            pygame.draw.circle(screen, (255,0,0), (x,y), 30)
            pygame.draw.circle(screen, (250,250,0), (x,y), 20)
            pygame.display.flip()

            pygame.draw.circle(screen,(0,0,255),(x_pos_b, y_pos_b),circle_radius)
            pygame.draw.circle(screen, (255,0,0),(x_pos_r,y_pos_r),circle_radius)
            pygame.draw.circle(screen, (255,0,0), (x,y), 35)
            pygame.draw.circle(screen, (250,250,0), (x,y), 25)
            pygame.display.flip()
            
            pygame.draw.circle(screen,(0,0,255),(x_pos_b, y_pos_b),circle_radius)
            pygame.draw.circle(screen, (255,0,0),(x_pos_r,y_pos_r),circle_radius)
            pygame.draw.circle(screen, (255,0,0), (x,y), 30)
            pygame.draw.circle(screen, (250,250,0), (x,y), 20)
            pygame.display.flip()

            pygame.draw.circle(screen,(0,0,255),(x_pos_b, y_pos_b),circle_radius)
            pygame.draw.circle(screen, (255,0,0),(x_pos_r,y_pos_r),circle_radius)
            pygame.draw.circle(screen, (255,0,0), (x,y), 25)
            pygame.draw.circle(screen, (250,250,0), (x,y), 15)
            pygame.display.flip()

            pygame.draw.circle(screen,(0,0,255),(x_pos_b, y_pos_b),circle_radius)
            pygame.draw.circle(screen, (255,0,0),(x_pos_r,y_pos_r),circle_radius)
            pygame.draw.circle(screen, (255,0,0), (x,y), 15)
            pygame.draw.circle(screen, (250,250,0), (x,y), 10)
            pygame.display.flip()

            pygame.draw.circle(screen,(0,0,255),(x_pos_b, y_pos_b),circle_radius)
            pygame.draw.circle(screen, (255,0,0),(x_pos_r,y_pos_r),circle_radius)
            pygame.draw.circle(screen,(0,0,0),(x,y),10) 
            pygame.draw.circle(screen, (0,0,0), (x,y), 10)
            pygame.display.flip()

            playsound('explosion.wav')
            return True

    return False

#def setPhasingTrue():
 #   phasing = True;
  #  print("phasing is " + str(phasing));

#def setPhasingFalse():
 #   phasing = False;
  #  print("phasing is " + str(phasing));
    


# This function checks for and deactivates the mines of another player
def check_perimeter_for_mine(mine_coor, x, y):
    perimeter = [(x-25,y), (x+25,y), (x,y-25), (x,y+25), (x-25,y-25), (x+25,y-25), (x-25,y+25),(x+25,y+25)]
    deactivate_mines = []
    for coor in perimeter:
        for item in mine_coor:
            if (coor[0] - item[0]) <= 25 and (coor[1] - item[1]) <= 25:
                deactivate_mines.append(item)
                mine_coor.remove(item)
    return deactivate_mines








# The function checks for walls and keeps the playerr from walking through walls
def check_for_collision(canvas,x,y,direction):
    
    if direction == 'UP':
        if canvas.get_at((x,y-10)) == (255,255,255) or phasing == True:
            return False#if white or phasing, no collision
        else:
            return True

    if direction == 'DOWN':
        if canvas.get_at((x,y+10)) == (255,255,255) or phasing == True:
            return False
        else:
            return True

    if direction == 'LEFT':
        if canvas.get_at((x-10,y)) == (255,255,255) or phasing == True:
            return False
        else:
            return True

    if direction == 'RIGHT':
        if canvas.get_at((x+10,y)) == (255,255,255) or phasing == True:
            return False
        else:
            return True


#projectile functions

#give this 2 pts, it will return the distance between them
def distance(x1,y1,x2,y2):
    slope = abs((y2-y1)/(x2-x1));
    return slope;
        #checks if player is hit by a laser, can be hit by your own laser
    
def checkPlayerLaserCollision(canvas,projx,projy,pposX,pposY):
    #this checks the distance between the laser and the player, could detect through walls but the objects would be too far apart
    if distance(abs(projx),abs(projy),abs(pposX),abs(pposY)) >= 5:
        #print(distance)
        return True#if laser hits a player
    
    #print(distance)
    return False#if laser does not hit a player
       
        #check if laser hits a wall
def checkLaserWallCollision(canvas,x,y):
    #this shitstorm checks if the entire radius of the laser hits something, otherwise a fast laser could just go through walls
    hit = 0
    for i in range(5): #this makes an x around the laser center
        if canvas.get_at((int(x) + i,int(y) +i)) == (0,0,0) or canvas.get_at((int(x) - i,int(y) +i)) == (0,0,0) or canvas.get_at((int(x) + i,int(y) -i)) == (0,0,0) or canvas.get_at((int(x) - i,int(y) -i)) == (0,0,0):
            #print("laser collided at " + str(x) + " and " +str(y))
            return True#if laser hits a wall
    return False






def moveUp(canvas,x,y):
    #print("phasing is " + str(phasing));
    if check_for_collision(canvas,x,y,'UP') == False:
        y -= 3;        
        return y

    else:
        return y
        








def moveDown(canvas,x,y):
    #print("phasing is " + str(phasing));
    if check_for_collision(canvas,x,y,'DOWN') == False:
        y+=3
        return y
    else:
        return y









def moveLeft(canvas,x,y):

    if check_for_collision(canvas, x, y, 'LEFT') == False:
        x-=3
        return x
    else:
        return x








def moveRight(canvas,x,y):
    #print("phasing is " + str(phasing));
    if check_for_collision(canvas, x, y, 'RIGHT') == False:
        x+= 3
        return x
    else:
        return x











# The following code was obtained from the URL:


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

    K_1

)
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)


# Object pos
x_pos_b,y_pos_b = 415,15
x_pos_r,y_pos_r = 75,425


# object position change in case of key stroke event
delta_x, delta_y = 10,10

# Variable for checking if a collision occurred

collision = False

# Set up the drawing window

screen = pygame.display.set_mode([500, 500])

# create a surface object, image is drawn on it




image = pygame.image.load(image_file);
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
if image_file == 'maze.png':
    x_pos_b,y_pos_b = 415,15
    x_pos_r,y_pos_r = 75,425
    red_goal = 10
    blue_goal = 430

    x = 215

    while x <= 315:
        image.set_at((x,275),(0,0,0,0))
        x += 10

    x = 315

    while x <= 435:
        image.set_at((x,365),(0,0,0,0))
        x+= 10


    x = 315
    while x <= 375:
        image.set_at((x,315),(0,0,0,0))
        x += 10

    x= 55
    while x <= 115:
        image.set_at((x,215),(0,0,0,0))
        x+= 10

    x = 445
    while x <= 485:
        image.set_at((x,315),(0,0,0,0))
        x+=10
elif image_file == "maze2.png":
    x_pos_b, y_pos_b = 225,15

    red_goal = 10
    x_pos_r, y_pos_r = 345,475 
    blue_goal = 480

elif image_file == 'maz3.png':

    x = 33
    y = 190

    while y <= 261:
        image.set_at((x,y),(255,255,255))
        y+= 1

    x = 174
    y = 177
    while x <= 184:
        y = 177
        while y <= 270:
            image.set_at((x,y),(255,255,255))
            y+=1
        x +=1
    
    x = 150
    y = 402
    while y <= 411:
        x = 150
        while x <= 250:
            image.set_at((x,y),(255,255,255))
            x += 1
        y += 1
    x_pos_r, y_pos_r = 75,485
    x_pos_b,y_po_b = 375,25
    red_goal = 5
    blue_goal = 490
    circle_radius = 7

elif image_file == 'Maze4.png':
    blue_goal = 492
    red_goal =2
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
pygame.mixer.music.load('Labyrinth.mp3')
pygame.mixer.music.play(-1)
#update function
while running:
    elapsed = time.time() - start    
    # Check for collision

    #print(x_pos_b,y_pos_b)
    # Did the user click the window close button?

    #this will be able to check if the user is holding a key to move
    keysPressed = pygame.key.get_pressed()
    
    if keysPressed[pygame.K_UP]:
        y_pos_b = moveUp(image,x_pos_b,y_pos_b)
        pygame.draw.circle(screen, (0, 0, 255), (x_pos_b, y_pos_b),10)
        
        
    if keysPressed[pygame.K_DOWN]:
        y_pos_b = moveDown(image,x_pos_b,y_pos_b)
        pygame.draw.circle(screen, (0, 0, 255), (x_pos_b, y_pos_b),10)
        
    if keysPressed[pygame.K_LEFT]:
        x_pos_b = moveLeft(image,x_pos_b,y_pos_b)
        pygame.draw.circle(screen, (0, 0, 255), (x_pos_b, y_pos_b),10)
    
    if keysPressed[pygame.K_RIGHT]:
        x_pos_b = moveRight(image,x_pos_b,y_pos_b)
        pygame.draw.circle(screen, (0, 0, 255), (x_pos_b, y_pos_b),10)
        
        
    
    for event in pygame.event.get():
        
        # When the user clicks the close button
        # the window will close and the program will
        # quit, by setting the running variable to false
        # By doing this our while loop will be terminated
        # along with our program

        if event.type == pygame.QUIT:
            running = False

            
        if event.type == pygame.MOUSEBUTTONDOWN and shootReady == True:
            if event.button == 1:
                projectile = True;
                clickX, clickY = pygame.mouse.get_pos();
                #print(clickX)
                #print(clickY)
                #x and y slope vars
                slopeX = (clickX - x_pos_b)/20
                slopeY = (clickY - y_pos_b)/20
                #position of the projectile
                projX = x_pos_b + (slopeX / 10)
                projY = y_pos_b + (slopeY / 10)
                
                pygame.draw.circle(screen, (0,255,0), (int(projX), int(projY)),10)
                #pygame.draw.circle(screen, (0,255,0), (int(projX), int(projY)),5)    
            
            
        if event.type == KEYDOWN:
            
            #this is the phasing/walkthrough ability
            if event.key == K_1 and phasingReady == True:
                phasing = True;
                phasingReady = False;
                phaseStart = elapsed;
                #print("phasing is " + str(phasing));
            
            if event.key == K_UP:
                y_pos_b = moveUp(image,x_pos_b,y_pos_b)
                pygame.draw.circle(screen, (0, 0, 255), (x_pos_b, y_pos_b),circle_radius)


            if event.key == K_DOWN:
                y_pos_b = moveDown(image,x_pos_b,y_pos_b) 
                pygame.draw.circle(screen, (0, 0, 255), (x_pos_b, y_pos_b),circle_radius)

            if event.key == K_RIGHT:
                x_pos_b = moveRight(image, x_pos_b, y_pos_b)
                pygame.draw.circle(screen, (0, 0, 255), (x_pos_b, y_pos_b),circle_radius)

            if event.key == K_LEFT:
                x_pos_b = moveLeft(image, x_pos_b,y_pos_b)
                pygame.draw.circle(screen, (0, 0, 255), (x_pos_b, y_pos_b),circle_radius)
        
            
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
                playsound('mine-deployed.wav')
                mine_coor_r.append((x_pos_r,y_pos_r))
            
            # Right Control key was presssed
            if event.key == 305:
                playsound('mine-deployed.wav')
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
                    #print(old_elapsed)
            
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
              #this is the end of the event for loop          

            
    # Here we will reactivate mines that were deactivated 5 seconds ago
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
                
    #here we will reset the phasing variable so you cant just walk through walls all day
    if elapsed >= phaseStart + 1:
        phasing = False;
        shootReady = True;
        
    #cooldown timer for phasing
    if elapsed >= phaseStart + 5:
        phasingReady = True;
        
    
    #print(elapsed, old_elapsed)

#        if event.type == pygame.KEYUP:
#            print("Key was released")

    
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

    #print("Color: ",image.get_at((x_pos_b,y_pos_b)))
    #print("Circle Position: ",(x_pos_b,y_pos_b))
    
    if check_for_mine(mine_coor_r,x_pos_b,y_pos_b) == True:
        #screen.blit(bomb,(x_pos_b-10,y_pos_b-10))
        pygame.draw.circle(screen, (0,0,0), (x_pos_b,y_pos_b), 15)
        pygame.draw.circle(screen, (255,0,0), (x_pos_b,y_pos_b), 5)
        pygame.display.flip()
        print("Blue was exploded")
        print("Blue lost")
        screen.fill((255,255,255))
        screen.blit(redwin,(0,0))
        pygame.display.update()
        break

    if check_for_mine(mine_coor_b, x_pos_r, y_pos_r) == True:
        pygame.draw.circle(screen, (0,0,0), (x_pos_r,y_pos_r), 15)
        pygame.draw.circle(screen, (255,0,0), (x_pos_r,y_pos_r), 5)
        pygame.display.flip()
        print("Red was exploded")
        print("Red lost")
        screen.fill((255,255,255))
        screen.blit(bluewin,(0,0))
        pygame.display.update()
        break




    if y_pos_b >= blue_goal:

        print("Blue escaped")

        print("Blue won!");
        playsound('win.wav')
        screen.fill((255,255,255))
        screen.blit(bluewin,(0,0))
        pygame.display.update()
        break


    if y_pos_r <= red_goal:

        print("Red escaped")

        print("Red won!")
        playsound('win.wav')
        screen.fill((255,255,255))
        screen.blit(redwin,(0,0))
        pygame.display.update()
        break

    #was red shot by a laser?   
    
    if checkPlayerLaserCollision(screen,projX, projY, x_pos_r,y_pos_r) == True and projectile == True:
        pygame.mixer.music.stop()
        print("Blue lasered Red")
        print("Blue won!");
        playsound('win.wav')
        screen.fill((255,255,255))
        screen.blit(bluewin,(0,0))
        pygame.display.update()
        break
       
       #was blue shot by a laser?   
    if checkPlayerLaserCollision(screen,projX, projY,x_pos_b,y_pos_b) == True and projectile == True:
        pygame.mixer.music.stop()
        print("Red lasered Blue")
        print("Red won!");
        playsound('win.wav')
        screen.fill((255,255,255))
        screen.blit(redwin,(0,0))
        pygame.display.update()
        break
        
        
             #here im making a loop that will move the projectile a certain amount
    #per frame, then let the rest of the frame execute
    if(projectile == True) and checkLaserWallCollision(screen,projX+slopeX,projY+slopeY) == False:
        #move the projectile in the direction the user clicked
        pygame.draw.circle(screen, (0,255,0), (int(projX), int(projY)),7)#checking if I will hit a wall if the laser keeps going
        projX = projX + slopeX
        projY = projY + slopeY
        

    pygame.draw.circle(screen, (0, 0, 255), (x_pos_b, y_pos_b),circle_radius)
    pygame.draw.circle(screen, (255, 0, 0), (x_pos_r, y_pos_r), circle_radius)

    # Flip the display, updates content in display

    pygame.display.flip()
    
        
    #if collision == True:
     #   running = False

# Done! Time to quit.

pygame.quit()
