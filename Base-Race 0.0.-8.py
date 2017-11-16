'''
base race non-functional build
'''

# IMPORTS #
import pygame
from pygame.locals import *

# SETUPS #
pygame.init()

# screen size
screen = (1920,1080)

# sizing things
blockSize = 32
playerRadius = 8

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
                if key[pygame.K_ESCAPE]:
                    return
main()
pygame.quit()