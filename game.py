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
                    # draw red circle
                    pygame.draw.circle(screen, RED, (x+block_size/2, y+block_size/2), block_size/2-circle_margin)
                # if there is a 2
                elif self.board[y_block][x_block] == 2:
                    # draw yellow circle
                    pygame.draw.circle(screen, YELLOW, (x+block_size/2, y+block_size/2), block_size/2-circle_margin)
                # if there is a 3
                elif self.board[y_block][x_block] == 3:
                    # draw red circle
                    pygame.draw.circle(screen, RED_LIGHT, (x+block_size/2, y+block_size/2), block_size/2-circle_margin)
                    self.board[y_block][x_block] = 0 #reset board pos
                # if there is a 4
                elif self.board[y_block][x_block] == 4:
                    # draw yellow circle
                    pygame.draw.circle(screen, YELLOW_LIGHT, (x+block_size/2, y+block_size/2), block_size/2-circle_margin)
                    self.board[y_block][x_block] = 0 #reset board pos
                else:
                    # draw BACKGROUND circle
                    pygame.draw.circle(screen, BACKGROUND, (x+block_size/2, y+block_size/2), block_size/2-circle_margin)

                #debug text
                # text = pygame.font.SysFont('Calibri', 20, True, False)
                # text_render = text.render(f"{y_block}, {x_block}", True, (255, 255, 255))

                # screen.blit(text_render, (x, y))

                rect = pygame.Rect(x, y, block_size, block_size)
                pygame.draw.rect(screen, BACKGROUND, rect, 1)

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