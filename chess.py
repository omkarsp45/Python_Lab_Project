# Building Two Player Chess Game using Pygame

import pygame
pygame.init()


board_size = 8
width , height = 800 , 830
block_size = 100
running = True

# Python Window Setup
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption("Satranj Ka Khel")
icon = pygame.image.load("ProjectImages/logo.png")
pygame.display.set_icon(icon)

# Turn 1-> WhiteSelect
# Turn 2-> WhiteMove
# Turn 3-> BlackSelect 
# Turn 4-> BlackMove
turn = 1

# Index of selected location
selected = -100

# for storing available moves for each pieces 
available_moves = []

# Font 
font = pygame.font.Font(None, 36)

# Drawing Chess Board
def draw_chess_board():
    for i in range(board_size):
        for j in range(board_size):
            if (i+j)%2 == 0 :
                colour = (235,235,235)
            else:
                colour = (55,55,55)    
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

# Pieces Lists
b_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook', 
            'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']

w_pieces = ['pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 
            'rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']

# Indexing of each piece to draw pieces
b_locations = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
              (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]

w_locations = [(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),
              (0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7)]

# Drawing Chess Pieces 
def draw_chess_pieces():
    for i in range(len(w_pieces)):
        if w_pieces[i]== 'pawn':
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
            screen.blit(black_pawn , (b_locations[i][0]*100+20 , b_locations[i][1]*100+30))
        elif b_pieces[i]== 'rook':
            screen.blit(black_rook , (b_locations[i][0]*100+15 , b_locations[i][1]*100+20))
        elif b_pieces[i]== 'knight':
            screen.blit(black_knight , (b_locations[i][0]*100+15 , b_locations[i][1]*100+20))
        elif b_pieces[i]== 'bishop':
            screen.blit(black_bishop , (b_locations[i][0]*100+15 , b_locations[i][1]*100+20))
        elif b_pieces[i]== 'queen':
            screen.blit(black_queen , (b_locations[i][0]*100+10 , b_locations[i][1]*100+15))
        elif b_pieces[i]== 'king':
            screen.blit(black_king , (b_locations[i][0]*100+10 , b_locations[i][1]*100+15))

def pawn_moves(location , turn ):
    moves_list = []
    if turn == 'black':
        if (location[0],location[1]+1) not in w_locations and (location[0],location[1]+1) not in b_locations : 
            moves_list.append((location[0],location[1]+1))
            if (location[0],location[1]+2) not in w_locations and (location[0],location[1]+2) not in b_locations and location[1]==1: 
                moves_list.append((location[0],location[1]+2))  
        if (location[0]+1,location[1]+1) in w_locations :
            moves_list.append((location[0]+1,location[1]+1)) 
        if (location[0]-1,location[1]+1) in w_locations :
            moves_list.append((location[0]-1,location[1]+1))        
    else:
        if (location[0],location[1]-1) not in w_locations and (location[0],location[1]-1) not in b_locations : 
            moves_list.append((location[0],location[1]-1))
            if (location[0],location[1]-2) not in w_locations and (location[0],location[1]-2) not in b_locations and location[1]==6: 
                moves_list.append((location[0],location[1]-2))  
        if (location[0]+1,location[1]-1) in b_locations :
            moves_list.append((location[0]+1,location[1]-1))    
        if (location[0]-1,location[1]-1) in b_locations :
            moves_list.append((location[0]-1,location[1]-1)) 
    return moves_list

def rook_moves(location , turn ):
    moves_list = []
    if turn == 'white':
        for i in range(1,8):
            if (location[0],location[1]-i) not in w_locations:
                moves_list.append((location[0],location[1]-i))
                if (location[0],location[1]-i) in b_locations :
                    break
            else:
                break
        for i in range(1,8):
            if (location[0],location[1]+i) not in w_locations :
                moves_list.append((location[0],location[1]+i))
                if (location[0],location[1]+i) in b_locations :
                    break
            else:
                break
        for i in range(1,8):
            if (location[0]-i,location[1]) not in w_locations :
                    moves_list.append((location[0]-i,location[1]))
                    if (location[0]-i,location[1]) in b_locations :
                        break
            else:
                break        
        for i in range(1,8):
            if (location[0]+i,location[1]) not in w_locations :
                moves_list.append((location[0]+i,location[1]))
                if (location[0]+i,location[1]) in b_locations :
                    break
            else:
                break
    else:
        for i in range(1,8):
            if (location[0],location[1]-i) not in b_locations :
                moves_list.append((location[0],location[1]-i))
                if (location[0],location[1]-i) in w_locations :
                    break
            else:
                break
        for i in range(1,8):
            if (location[0],location[1]+i) not in b_locations :
                moves_list.append((location[0],location[1]+i))
                if (location[0],location[1]+i) in w_locations :
                    break
            else:
                break
        for i in range(1,8):
            if (location[0]-i,location[1]) not in b_locations :
                    moves_list.append((location[0]-i,location[1]))
                    if (location[0]-i,location[1]) in w_locations :
                        break
            else:
                break        
        for i in range(1,8):
            if (location[0]+i,location[1]) not in b_locations :
                moves_list.append((location[0]+i,location[1]))
                if (location[0]+i,location[1]) in w_locations :
                    break
            else:
                break

    return moves_list

def bishop_moves(location , turn):
    moves_list = []
    if turn == 'white':
        for i in range(1,8):
            if (location[0]-i,location[1]-i) not in w_locations :
                moves_list.append((location[0]-i,location[1]-i))
                if (location[0]-i,location[1]-i) in b_locations :
                    break
            else:
                break
        for i in range(1,8):
            if (location[0]+i,location[1]+i) not in w_locations :
                moves_list.append((location[0]+i,location[1]+i))
                if (location[0]+i,location[1]+i) in b_locations :
                    break
            else:
                break
        for i in range(1,8):
            if (location[0]-i,location[1]+i) not in w_locations :
                    moves_list.append((location[0]-i,location[1]+i))
                    if (location[0]-i,location[1]+i) in b_locations :
                        break
            else:
                break        
        for i in range(1,8):
            if (location[0]+i,location[1]-i) not in w_locations :
                moves_list.append((location[0]+i,location[1]-i))
                if (location[0]+i,location[1]-i) in b_locations :
                    break
            else:
                break
    else:
        for i in range(1,8):
            if (location[0]-i,location[1]-i) not in b_locations :
                moves_list.append((location[0]-i,location[1]-i))
                if (location[0]-i,location[1]-i) in w_locations :
                    break
            else:
                break
        for i in range(1,8):
            if (location[0]+i,location[1]+i) not in b_locations :
                moves_list.append((location[0]+i,location[1]+i))
                if (location[0]+i,location[1]+i) in w_locations :
                    break
            else:
                break
        for i in range(1,8):
            if (location[0]-i,location[1]+i) not in b_locations :
                    moves_list.append((location[0]-i,location[1]+i))
                    if (location[0]-i,location[1]+i) in w_locations :
                        break
            else:
                break        
        for i in range(1,8):
            if (location[0]+i,location[1]-i) not in b_locations :
                moves_list.append((location[0]+i,location[1]-i))
                if (location[0]+i,location[1]-i) in w_locations :
                    break
            else:
                break
        
    return moves_list

def queen_moves(location , turn ):
    all_moves = []
    all_moves += bishop_moves(location , turn )
    all_moves += rook_moves(location , turn)
    return all_moves

def knight_moves(location , turn ):
    moves_list = []
    dummy = [(2,1),(2,-1),(-2,-1),(-2,1),(1,2),(1,-2),(-1,-2),(-1,2)]
    if turn == 'black':
        for i in range(8):
            if (location[0]+dummy[i][0],location[1]+dummy[i][1]) not in b_locations:    
                moves_list.append((location[0]+dummy[i][0],location[1]+dummy[i][1]))
    else:
        for i in range(8):
            if (location[0]+dummy[i][0],location[1]+dummy[i][1]) not in w_locations:    
                moves_list.append((location[0]+dummy[i][0],location[1]+dummy[i][1]))
    return moves_list

def king_moves(location , turn ):
    moves_list =[]
    dummy = [(0,1),(0,-1),(-1,-1),(-1,1),(1,0),(1,1),(-1,0),(1,-1)]
    if turn == 'white':
        for i in range(8):
            if (location[0]+dummy[i][0],location[1]+dummy[i][1]) not in w_locations:    
                moves_list.append((location[0]+dummy[i][0],location[1]+dummy[i][1]))
    else:
        for i in range(8):
            if (location[0]+dummy[i][0],location[1]+dummy[i][1]) not in b_locations:    
                moves_list.append((location[0]+dummy[i][0],location[1]+dummy[i][1]))
    return moves_list 

# Function that finds valid moves of each piece on boards
def val_moves(pieces , locations , turn):
    moves = []
    all_pieces_moves = []
    for i in range(len(pieces)):
        piece_location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves = pawn_moves(piece_location , turn)
        if piece == 'rook':
            moves = rook_moves(piece_location , turn )
        if piece == 'bishop':
            moves = bishop_moves(piece_location , turn )
        if piece == 'queen':
            moves = queen_moves(piece_location , turn)
        if piece == 'knight':
            moves = knight_moves(piece_location , turn)
        if piece == 'king':
            moves = king_moves(piece_location , turn)
        all_pieces_moves.append(moves)
    return all_pieces_moves

def check():
    white_king_index = w_pieces.index('king') if 'king' in w_pieces else -1
    black_king_index = b_pieces.index('king') if 'king' in b_pieces else -1

    if white_king_index != -1:
        white_king_location = w_locations[white_king_index]
        for i in range(len(black_options)):
            if white_king_location in black_options[i]:
                text = font.render("White is in Check", True, (255, 255, 255))
                screen.blit(text, (10, 800))       
                return ""
            else:
                text = font.render("White is in Check", True, (0, 0, 0))
                screen.blit(text, (10, 800))

    if black_king_index != -1:
        black_king_location = b_locations[black_king_index]
        for i in range(len(white_options)):
            if black_king_location in white_options[i]:
                text = font.render("Black is in Check", True, (255, 255, 255))
                screen.blit(text, (10, 800))
                return ""
            else:
                text = font.render("Black is in Check", True, (0, 0, 0))
                screen.blit(text, (10, 800))    
    return "No"

def check_mate(color , location):
    if color == "white":
        Modified_List = []
        for i in range(len(w_pieces)):
            piece_location = w_locations[i]
            piece = w_pieces[i]
            if piece == 'pawn':
                moves = pawn_moves(piece_location , "white")
            if piece == 'rook':
                moves = rook_moves(piece_location , "white" )
            if piece == 'bishop':
                moves = bishop_moves(piece_location , "white" )   
            if piece == 'queen':
                moves = queen_moves(piece_location , "white")     
            if piece == 'knight':
                moves = knight_moves(piece_location , "white")   
            if piece == 'king':
                moves = king_moves(piece_location , "white")    
            for j in range(len(moves)):
                    w_locations[i]=moves[j]
                    if just_check() == "No":
                        Modified_List.append(moves[j])
        global available_moves
        available_moves = Modified_List
        if len(Modified_List) == 0 :
            text = font.render("White CheckMate", True, (255, 255, 255))
            screen.blit(text, (500, 800))       
            pygame.quit()
            return
        else:
            text = font.render("White CheckMate", True, (0, 0, 0))
            screen.blit(text, (500, 800))
    if color == "black":
        Modified_List = []
        for i in range(len(b_pieces)):
            piece_location = b_locations[i]
            piece = b_pieces[i]
            if piece == 'pawn':
                moves = pawn_moves(piece_location , "black")
            if piece == 'rook':
                moves = rook_moves(piece_location , "black" )
            if piece == 'bishop':
                moves = bishop_moves(piece_location , "black" )   
            if piece == 'queen':
                moves = queen_moves(piece_location , "black")     
            if piece == 'knight':
                moves = knight_moves(piece_location , "black")   
            if piece == 'king':
                moves = king_moves(piece_location , "black")    
            for j in range(len(moves)):
                    b_locations[i]=moves[j]
                    if just_check() == "No":
                        Modified_List.append(moves[j])
        if len(Modified_List) == 0 :
            text = font.render("Black CheckMate", True, (255, 255, 255))
            screen.blit(text, (500, 800))       
            pygame.quit()
            return
        else:
            text = font.render("Black CheckMate", True, (0, 0, 0))
            screen.blit(text, (500, 800))

def all_valid_moves():
    if turn <= 2 :
        options = white_options
    else:
        options = black_options 
    toReturn = options[selected]
    return toReturn       

def draw_color(moves):
    if turn <= 2:
        color = (255,21,0)
    else:
        color = (76,0,255)
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)

white_options = val_moves(w_pieces , w_locations , 'white')
black_options = val_moves(b_pieces , b_locations , 'black')

# Game Loop  
while running:
    draw_chess_board() # Draw Chess Board

    draw_chess_pieces() # Draw Chess Pieces

    check() # Check for check or checkmate

    if selected != -100 :
        available_moves = all_valid_moves() 
        draw_color(available_moves)

    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif Event.type == pygame.MOUSEBUTTONDOWN and Event.button == 1: # 1 : left click 
            x = Event.pos[0]
            y = Event.pos[1]
            clicked_coordinate = (x//100 , y//100)
            if turn <= 2:
                if clicked_coordinate in w_locations:
                    selected = w_locations.index(clicked_coordinate)
                    turn = 2
                if clicked_coordinate in available_moves and selected != -100:
                    w_locations[selected] = clicked_coordinate
                    if clicked_coordinate in b_locations:
                        piece_index = b_locations.index(clicked_coordinate)
                        b_pieces.pop(piece_index)
                        b_locations.pop(piece_index)
                    turn = 3
                    selected = -100
                    available_moves = []
                white_options = val_moves(w_pieces , w_locations , 'white')
                black_options = val_moves(b_pieces , b_locations , 'black')   
            else :
                if clicked_coordinate in b_locations:
                    selected = b_locations.index(clicked_coordinate)
                    turn = 4
                if clicked_coordinate in available_moves and selected != -100:
                    b_locations[selected] = clicked_coordinate
                    if clicked_coordinate in w_locations:
                        piece_index = w_locations.index(clicked_coordinate)
                        w_pieces.pop(piece_index)
                        w_locations.pop(piece_index)
                    turn = 1
                    selected = -100
                    available_moves = []
                white_options = val_moves(w_pieces , w_locations , 'white')
                black_options = val_moves(b_pieces , b_locations , 'black')

    pygame.display.flip()

pygame.quit()