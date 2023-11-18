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
screen = pygame.display.set_mode([width,height] , pygame.RESIZABLE)
# Game Name
pygame.display.set_caption("Satranj Ka Khel")
# Game Logo
icon = pygame.image.load("ProjectImages/logo.png")
pygame.display.set_icon(icon)

# Optional FPS ajduste(no such need of fps manager here since game is not animated type)
speed = pygame.time.Clock()


# Drawing Chess Board
def draw_chess_board():
    for i in range(board_size):
        for j in range(board_size):
            if (i+j)%2 == 0 : 
                colour = (255,255,255)
            else:
                colour = (54,51,51)    
            pygame.draw.rect(screen , colour , (i*block_size , j*block_size , block_size , block_size))


# Loading Pieces Images and Adjusting its dimension
# white pieces
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

# black pieces
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

# Checking(Adjusting) for correct position to place pieces
    # screen.blit(black_king , (100+10,100+15))
    # screen.blit(white_king , (100+10,200+15))
    # screen.blit(white_rook , (200+15,200+20))
    # screen.blit(white_knight , (200+15,100+20))
    # screen.blit(black_pawn , (100+20,300+30))

# Pieces Lists
w_pieces = ['pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 
            'rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']

b_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook', 
            'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

# Indexing of each piece to draw pieces
b_location = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
              (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]

w_locations = [(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),
              (0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7)]

# Drawing Chess Pieces 
def draw_chess_pieces():
    for i in range(len(w_pieces)):
        if w_pieces[i]=='pawn':
            screen.blit(white_pawn , (w_locations[i][0]*100+20 , w_locations[i][1]*100+30))
        elif w_pieces[i]== 'rook':
            screen.blit(white_rook , (w_locations[i][0]*100+15 , w_locations[i][1]*100+20))
        elif w_pieces[i]== 'knight':
            screen.blit(white_knight , (w_locations[i][0]*100+15 , w_locations[i][1]*100+20))
        elif w_pieces[i]== 'bishop':
            screen.blit(white_bishop , (w_locations[i][0]*100+15 , w_locations[i][1]*100+20))
        elif w_pieces[i]== 'queen':
            screen.blit(white_queen , (w_locations[i][0]*100+10 , w_locations[i][1]*100+15))
        elif w_pieces[i]== 'king':
            screen.blit(white_king , (w_locations[i][0]*100+10 , w_locations[i][1]*100+15))

    for i in range(len(b_pieces)):
        if b_pieces[i]=='pawn':
            screen.blit(black_pawn , (b_location[i][0]*100+20 , b_location[i][1]*100+30))
        elif b_pieces[i]== 'rook':
            screen.blit(black_rook , (b_location[i][0]*100+15 , b_location[i][1]*100+20))
        elif b_pieces[i]== 'knight':
            screen.blit(black_knight , (b_location[i][0]*100+15 , b_location[i][1]*100+20))
        elif b_pieces[i]== 'bishop':
            screen.blit(black_bishop , (b_location[i][0]*100+15 , b_location[i][1]*100+20))
        elif b_pieces[i]== 'queen':
            screen.blit(black_queen , (b_location[i][0]*100+10 , b_location[i][1]*100+15))
        elif b_pieces[i]== 'king':
            screen.blit(black_king , (b_location[i][0]*100+10 , b_location[i][1]*100+15))


# Game Starts From Here -->>
while running:
    for Event in pygame.event.get():
        if Event.type == pygame.QUIT: # Functionality to close button
            pygame.quit()    # Just deinitializes library(can get error in further pygame instructions).
            sys.exit()

        elif Event.type == pygame.MOUSEBUTTONDOWN and Event.button == 1:
            x = Event.pos[0]
            y = Event.pos[1]
            clicked_coordinate = (x//100 , y//100)  # floor div to find exact block coordinate

            # turn moves , selected piece logic -->  next target  
            

    draw_chess_board() # Draw Chess Board

    draw_chess_pieces() # Draw Chess Pieces

    speed.tick(30)      # Game will be run at 30fps.
    pygame.display.flip()


pygame.quit()
sys.exit()