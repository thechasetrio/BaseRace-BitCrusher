'''
base race non-functional build
'''

# IMPORTS #
import pygame
from pygame.locals import *
from math import atan
# SETUPS #
pygame.init()

# screen size
screen = (1920,1080)

# sizing things
blockSize = 32
playerRadius = 8

# client to server variables
up = False
down = False
left = False
right = False
shoot = False
degree = 0

#COLORS#
BLUE = (0,170,255)
ORANGE = (255,170,0)
BEIGE = (255,240,200)
GREY = (170,170,170)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (140,210,70)

# sets up client-server connection
serverIp = input("Game Server IP: ")
port = 25565 # I like building brown bricks with minecraft
# walkers coolio client stuff

# start window
win = pygame.display.set_mode(screen,pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)

def main():
    # IMPORTANT MAIN LOOP #
    while True:
        for event in pygame.event.get():
            # events go here
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                # keystrokes go here
                key = pygame.key.get_pressed()
                # quit
                if key[pygame.K_ESCAPE]:
                    return
                # WASD
                if key[pygame.K_w]:
                    up = True
                if key[pygame.K_a]:
                    left = True
                if key[pygame.K_s]:
                    down = True
                if key[pygame.K_d]:
                    right = True
            # get shoot and degree throuhg inverse tangent and a try/except
            if event.type == pygame.MOUSEBUTTONDOWN:
                # mouse things go here
                mouse = pygame.mouse.get_pressed()
                # shooting
                if mouse[0]:
                    shoot = True
                    # shoot angle
                    mousePos = pygame.mouse.get_pos()
                    # gets degree measurement of shooting
                    try:
                        degree = math.degrees(math.atan(((screen[0] / 2) - mousePos[0])/((screen[1] / 2) - mousePos[1])))
                    # STOPS A DIVISION BY ZERO CRASH
                    except:
                        if ((screen[0] / 2) - mousePos[0]) >= 0:
                            degree = 0
                        else: 
                            degree = 180

main()
pygame.quit()