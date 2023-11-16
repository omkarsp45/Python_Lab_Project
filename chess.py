# Building Two Player Chess Game using Pygame

import pygame
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


# Game Starts From Here -->>
while running:
    for Events in pygame.event.get():
        if Events.type == pygame.QUIT:
            pygame.quit() 

    pygame.display.flip()

