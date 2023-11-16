# Building Two Player Chess Game using Pygame

# Importing Modules
import pygame
import sys 

pygame.init()

# Variables
board_size = 8 
width , height = 800 , 800
block_size = 100
running = True

# Python Window Setup
# Chess Board
screen = pygame.display.set_mode([width,height])
# Game Name
pygame.display.set_caption("Satranj Ka Khel")
# Game Logo
icon = pygame.image.load("ProjectImages/logo.png")
pygame.display.set_icon(icon)

#Optional FPS ajduste(no such need of fps manager here since game is not animated type)
speed = pygame.time.Clock()

# Game Starts From Here -->>
while running:
    for Events in pygame.event.get():
        if Events.type == pygame.QUIT: # Functionality to close button
            pygame.quit()    # Just deinitializes library(can get error in further pygame instructions).
            sys.exit()

    speed.tick(30)      # Game will be run at 30fps.
    pygame.display.flip()


pygame.quit()
sys.exit()