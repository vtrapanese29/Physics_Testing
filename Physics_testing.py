import pygame, sys
from pygame.locals import *
import random
import math

#time to mess with some physics

def player():
    Display.blit(PLAYER, (playerPos[0],playerPos[1]))
        
#acceleration
a_x = 0
a_y = 0

#velocity
v_x = 0
v_y = 0
speed = 3

#position
x = 0
y = 0
pos = (0, 0)

#Move Mapping?
move_map = {pygame.K_LEFT: (-1,0),
            pygame.K_RIGHT: (1,0),
            pygame.K_UP: (0,-1),
            pygame.K_DOWN: (0,1),}

def motion():
    global v_x
    global v_y
    if event.type == KEYDOWN:
        if (event.key == K_RIGHT):
            v_x = 2
        if event.key == K_LEFT:
            v_x = -2
        if event.key == K_DOWN:
            v_y = 2
        if event.key == K_UP:
            v_y = -2
    if event.type == KEYUP:
        if event.key == K_RIGHT:
            v_x = 0
        if event.key == K_LEFT:
            v_x = 0
        if event.key == K_DOWN:
            v_y = 0
        if event.key == K_UP:
            v_y = 0
       
#colors
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]

#some bullshit dimentions
MAPWIDTH = 500
MAPHEIGHT = 500

pygame.init()
Display = pygame.display.set_mode((MAPWIDTH, MAPHEIGHT))

#Can I add Font?
FONT = pygame.font.Font('OpenSans-Bold.ttf', 18)

#Player image 
PLAYER = pygame.image.load('player.png').convert_alpha()
playerPos = [x, y]
playerVel = [v_x, v_y]
playerAcc = [a_x, a_y]

done = False
clock = pygame.time.Clock()

#--MAIN GAME CODE--
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if sum(map(abs,playerVel)) == 3:
            playerVel = [p/(math.sqrt(2)) for p in playerVel]
        playerVel = [speed*p for p in playerVel]
        motion()
    playerPos[0] += v_x
    playerPos[1] += v_y
    
    #drawing code
    player()

    #frames
    pygame.display.flip()
    Display.fill(WHITE)
    clock.tick(60)
#game quit
pygame.quit()
