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

# Optional FPS ajduste(no such need of fps manager here since game is not animated type)
speed = pygame.time.Clock()


# Drawing Chess Board
def chess_board():
    for i in range(board_size):
        for j in range(board_size):
            if (i+j)%2 == 0 : 
                colour = (54,51,51)
            else:
                colour = (255,255,255)    
            pygame.draw.rect(screen , colour , (i*block_size , j*block_size , block_size , block_size))


# Loading Pieces Images
white_pawn = pygame.image.load('ProjectImages/pieces/white_pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (60, 60))
white_rook = pygame.image.load('ProjectImages/pieces/white_rook.png')
white_rook = pygame.transform.scale(white_rook, (75, 75))
white_knight = pygame.image.load('ProjectImages/pieces/white_knight.png')
white_knight = pygame.transform.scale(white_knight, (75, 75))
white_bishop = pygame.image.load('ProjectImages/pieces/white_bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (75, 75))
white_queen = pygame.image.load('ProjectImages/pieces/white_queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_king = pygame.image.load('ProjectImages/pieces/white_king.png')
white_king = pygame.transform.scale(white_king, (80, 80))

black_pawn = pygame.image.load('ProjectImages/pieces/black_pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (60, 60))
black_rook = pygame.image.load('ProjectImages/pieces/black_rook.png')
black_rook = pygame.transform.scale(black_rook, (75, 75))
black_knight = pygame.image.load('ProjectImages/pieces/black_knight.png')
black_knight = pygame.transform.scale(black_knight, (75, 75))
black_bishop = pygame.image.load('ProjectImages/pieces/black_bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (75, 75))
black_queen = pygame.image.load('ProjectImages/pieces/black_queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_king = pygame.image.load('ProjectImages/pieces/black_king.png')
black_king = pygame.transform.scale(black_king, (80, 80))


# Game Starts From Here -->>
while running:
    for Events in pygame.event.get():
        if Events.type == pygame.QUIT: # Functionality to close button
            pygame.quit()    # Just deinitializes library(can get error in further pygame instructions).
            sys.exit()

    chess_board() # Draw Chess Board

    # Checking for correct position to place pieces
    screen.blit(black_king , (100+10,100+15))
    screen.blit(white_king , (100+10,200+15))
    screen.blit(white_rook , (200+15,200+20))
    screen.blit(white_knight , (200+15,100+20))
    screen.blit(black_pawn , (100+20,300+30))

    speed.tick(30)      # Game will be run at 30fps.
    pygame.display.flip()


pygame.quit()
sys.exit()