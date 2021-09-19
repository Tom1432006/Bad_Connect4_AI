#!usr/bin/env python3

import pygame
import math
from random import randint
from time import sleep
import json

######################## Game  #######################

class Game:
    width = 0
    height = 0
    state = ""
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    def __init__(self, width=7, height=6):
        self.width = len(self.board)
        self.height = len(self.board[0])

    def generate_board(self, board):
        for x in range(0, screen_width, block_size):
            for y in range(0, screen_height, block_size):
                y_block = int(y/block_size)
                x_block = int(x/block_size)

                # if there is a 1
                if self.board[y_block][x_block] == 1:
                    # draw PLAYER1_CLR circle
                    pygame.draw.circle(screen, PLAYER1_CLR, (x+block_size/2, y+block_size/2), block_size/2-circle_margin)
                # if there is a 2
                elif self.board[y_block][x_block] == 2:
                    # draw PLAYER2_CLR circle
                    pygame.draw.circle(screen, PLAYER2_CLR, (x+block_size/2, y+block_size/2), block_size/2-circle_margin)
                # if there is a 3
                elif self.board[y_block][x_block] == 3:
                    # draw PLAYER1_CLR circle
                    pygame.draw.circle(screen, PLAYER1_CLR_LIGHT, (x+block_size/2, y+block_size/2), block_size/2-circle_margin)
                    self.board[y_block][x_block] = 0 #reset board pos
                # if there is a 4
                elif self.board[y_block][x_block] == 4:
                    # draw PLAYER2_CLR circle
                    pygame.draw.circle(screen, PLAYER2_CLR_LIGHT, (x+block_size/2, y+block_size/2), block_size/2-circle_margin)
                    self.board[y_block][x_block] = 0 #reset board pos
                else:
                    # draw BACKGROUND_CIRCLE circle
                    pygame.draw.circle(screen, BACKGROUND_CIRCLE, (x+block_size/2, y+block_size/2), block_size/2-circle_margin)

                #debug text
                # text = pygame.font.SysFont('Calibri', 20, True, False)
                # text_render = text.render(f"{y_block}, {x_block}", True, (255, 255, 255))

                # screen.blit(text_render, (x, y))

                rect = pygame.Rect(x, y, block_size, block_size)
                pygame.draw.rect(screen, BACKGROUND_CIRCLE, rect, 1)

    def reset(self):
        self.board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
        ]
        return False

######################## Player #######################

class Player:
    index = 1
    def __init__(self, index):
        self.index = index
        print(self.index)

    def make_move(self, board, mouse_pos, premake=False):
        row = math.floor(mouse_pos/block_size)
        for y in range(len(board)):
            if board[y][row] == 1 or board[y][row] == 2:
                break
            position = y

        if 'position' not in locals():
            return False

        if premake:
            board[position][row] = self.index+2 #add 3 or 4 to board
        else:
            board[position][row] = self.index
        
        return [int(position), int(row)]

    def make_random_move(self, board):
        row = randint(0, 6)
        for x in range(len(board)):
            if board[x][row] == 1 or board[x][row] == 2:
                break
            position = x

        if 'position' not in locals():
            return False
        
        board[position][row] = self.index

    def check_win(self, board, game):
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == self.index:
                        # #debug text
                        # text = pygame.font.SysFont('Calibri', 20, True, False)
                        # text_render = text.render(f"{y}, {x}", True, (255, 255, 255))
                        # screen.blit(text_render, (x*block_size, y*block_size))
                    try:
                        if y > 2:
                            # vertical
                            if board[y-1][x] == self.index and board[y-2][x] == self.index and board[y-3][x] == self.index:
                                game.state = f"Spieler {self.index} hat gewonnen"
                                return True
                        
                        if x > 2 and y-1 <= 6 and y-2 <= 6 and y-3 <= 6 and x-1 <= 6 and x-2 <= 6 and x-3 <= 6:
                            #diagonal left
                            if board[y-1][x-1] == self.index and board[y-2][x-2] == self.index and board[y-3][x-3] == self.index:
                                game.state = f"Spieler {self.index} hat gewonnen"
                                return True
                        # # horizontal
                        # if x > 4 and board[y][x-1] == self.index and board[y][x-2] == self.index and board[y][x-3] == self.index:
                        #     self.print_wining_tiles(x, y, x-1, y, x-2, y, x-3, y)
                        #     print(board[y][x-1], x-1,  board[y][x-2], x-2,  board[y][x-3], x-3)
                        #     game.state = f"Spieler {self.index} hat gewonnen"
                        #     return True
                        if x < 4 and y-1 <= 6 and y-2 <= 6 and y-3 <= 6 and x+1 <= 6 and x+2 <= 6 and x+3 <= 6:
                            #diagonal right
                            if board[y-1][x+1] == self.index and board[y-2][x+2] == self.index and board[y-3][x+3] == self.index:
                                game.state = f"Spieler {self.index} hat gewonnen"
                                return True
                    except Exception as e:
                        print(str(e) + f"{x}, {y}; {x+1}, {y-1}; {x+2}, {y-2}; {x+3}, {y-3}")

            layer = ''.join(str(x) for x in board[y])
            if f"{str(self.index)}{str(self.index)}{str(self.index)}{str(self.index)}" in layer:
                game.state = f"Spieler {self.index} hat gewonnen"
                return True

        return False

    def print_wining_tiles(self, x, y, x1, y1, x2, y2, x3, y3):
        rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
        pygame.draw.rect(screen, (0, 255, 0), rect, 2)

        rect1 = pygame.Rect(x1*block_size, y2*block_size, block_size, block_size)
        pygame.draw.rect(screen, (0, 255, 0), rect1, 2)

        rect2 = pygame.Rect(x2*block_size, y2*block_size, block_size, block_size)
        pygame.draw.rect(screen, (0, 255, 0), rect2, 2)

        rect3 = pygame.Rect(x3*block_size, y3*block_size, block_size, block_size)
        pygame.draw.rect(screen, (0, 255, 0), rect3, 2)

    def max(self, board, game, player):
        # Possible values for max_v are:
        # -1 - loss
        # 0  - a tie
        # 1  - win
        max_v = -100000 #set max value = more than worse

        row = None

        for x in range(len(board[0])):
            m = 0
            try:
                move_list = self.make_move(game.board, x*block_size)
                position = move_list[0]
                row = move_list[1]

                #add a bit of randomness
                m+= randint(0, 20)

                # check if there are 01110 pices
                for y in range(len(board)):
                    layer = ''.join(str(x) for x in board[y])
                    if f"0{self.index}{self.index}{self.index}0" in layer:
                        m += 120
                if self.check_win(board, game) == True:
                    m += 120

                
                for x2 in range(len(board[0])):
                    try:
                        move_list2 = (player.make_move(game.board, x2*block_size))
                        position2 = move_list2[0]
                        row2 = move_list2[1]
                        
                        for y in range(len(board)):
                            layer = ''.join(str(x) for x in board[y])
                            if f"0{player.index}{player.index}{player.index}0" in layer:
                                m -= 100
                        if player.check_win(board, game) == True:
                            print(x2, player.check_win(board, game))
                            m -= 100
                    
                        board[position2][row2] = 0
                    except Exception as e:
                        print(e, move_list2)

                print(m, max_v, m > max_v)
                if m > max_v:
                    print(x)
                    max_v = m
                    row_p = x

                board[position][row] = 0
            except Exception as e:
                print(e, move_list)

        print("bester move", row_p)
        return row_p

######################## Setup #######################
# initialize pygame modules
pygame.init()
pygame.font.init()

#region load json settings
with open("./settings.json") as f:
    settings = json.load(f)

color_scheme = settings["color_scheme"]
try:
    colors = settings[color_scheme]
except Exception as e:
    exit("This color scheme doesn't exist!")
#endregion

#region define all neccesairy variables
block_size = 170
circle_margin = 7
screen_width  = block_size * 7
screen_height = block_size * 6
fps = 30
clock = pygame.time.Clock()
turn = 1
game_done = False
# define the pygame screen
screen = pygame.display.set_mode([screen_width, screen_height])
#endregion

# initialize all neccesairy Classes
game = Game()
player1 = Player(index=1)
player2 = Player(index=2)

# colors
try:
    for color in colors:
        if color["name"] == "player1":
            PLAYER1_CLR = tuple(map(int, color["value"].split(', ')))
            PLAYER1_CLR_LIGHT = tuple(map(int, color["light_value"].split(', ')))
        elif color["name"] == "player2":
            PLAYER2_CLR = tuple(map(int, color["value"].split(', ')))
            PLAYER2_CLR_LIGHT = tuple(map(int, color["light_value"].split(', ')))
        elif color["name"] == "background":
            BACKGROUND_CIRCLE = tuple(map(int, color["value"].split(', ')))
            BACKGROUND = tuple(map(int, color["light_value"].split(', ')))

    #try colors
    pygame.draw.circle(screen, PLAYER1_CLR, (0, 0), 0)
    pygame.draw.circle(screen, PLAYER1_CLR_LIGHT, (0, 0), 0)
    pygame.draw.circle(screen, PLAYER2_CLR, (0, 0), 0)
    pygame.draw.circle(screen, PLAYER2_CLR_LIGHT, (0, 0), 0)
    pygame.draw.circle(screen, BACKGROUND_CIRCLE, (0, 0), 0)
    pygame.draw.circle(screen, BACKGROUND, (0, 0), 0)
except Exception as e:
    exit("Something is wrong with your color scheme!")

# BACKGROUND = (0, 178, 0)
# BACKGROUND_CIRCLE = (0, 70, 0)
# PLAYER1_CLR = (203, 0, 0)
# PLAYER2_CLR = (250, 201, 1)
# PLAYER1_CLR_LIGHT = (203, 50, 50)
# PLAYER2_CLR_LIGHT = (250, 225, 100)


# give window a name
pygame.display.set_caption("4 Gewinnt")

# Game Loop
if __name__ == "__main__":
    while True:
        if not game_done:
            screen.fill(BACKGROUND)
            game.generate_board(game.board)

            #preview move
            if turn == 1:
                player1.make_move(game.board, pygame.mouse.get_pos()[0], True)
            elif turn == 2:
                player2.make_move(game.board, pygame.mouse.get_pos()[0], True)

            # ai
            if turn == 2:
                player2.make_move(game.board, player2.max(game.board, game, player1)*block_size)
                # print(player2.max(game.board, game, player1))
                game_done = player2.check_win(game.board, game)
                turn = 1
            

            # event handeling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game.reset()
                        turn = 1
                    if event.key == pygame.K_q:
                        pygame.quit()

                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()[0]
                    if turn == 1:
                        if player1.make_move(game.board, pos) == False:
                            continue
                        game_done = player1.check_win(game.board, game)
                        turn = 2    
                    # elif turn == 2:
                    #     if player2.make_move(game.board, pos) == False:
                    #         continue
                    #     game_done = player2.check_win(game.board, game)
                    #     turn = 1
        else:
            game.generate_board(game.board)
            #quit game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_done = game.reset()
                        turn = 1
                    if event.key == pygame.K_q:
                        pygame.quit()
            # win text
            win_font = pygame.font.SysFont('Arial', 30, True, False)
            text_win = win_font.render(game.state + ". R = nochmal; q = schließen.", True, (255, 255, 255))

            screen.blit(text_win, [10, 10])

        pygame.display.flip()
        clock.tick(fps)

pygame.quit()